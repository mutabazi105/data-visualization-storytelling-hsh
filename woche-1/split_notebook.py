#!/usr/bin/env python3
"""
Script to split a large Jupyter notebook into multiple smaller notebooks.
Splits based on markdown headers (## Block 01, ## Block 02, etc.)

Usage:
    python split_notebook.py <input_notebook.ipynb> <output_directory>

Example:
    python split_notebook.py Main_Kopie_von_Intro_to_matplotlib.ipynb notebooks/
"""

import json
import sys
import os
import re
from pathlib import Path


def load_notebook(filepath):
    """Load a Jupyter notebook from file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)


def save_notebook(notebook, filepath):
    """Save a Jupyter notebook to file."""
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(notebook, f, indent=1, ensure_ascii=False)
    print(f"✅ Saved: {filepath}")


def create_empty_notebook():
    """Create an empty notebook structure."""
    return {
        "cells": [],
        "metadata": {
            "kernelspec": {
                "display_name": "Python 3",
                "language": "python",
                "name": "python3"
            },
            "language_info": {
                "name": "python",
                "version": "3.10.0"
            }
        },
        "nbformat": 4,
        "nbformat_minor": 4
    }


def find_block_markers(notebook, split_level='#'):
    """
    Find all block markers in the notebook based on heading level.
    
    Args:
        notebook: The notebook dict
        split_level: '#' for H1 (main sections), '##' for H2 (subsections)
    
    Looks for markdown cells with headings at the specified level.
    """
    markers = []
    
    for idx, cell in enumerate(notebook['cells']):
        if cell['cell_type'] == 'markdown':
            # Get the cell content
            source = ''.join(cell['source']) if isinstance(cell['source'], list) else cell['source']
            
            # Split by lines and check first line
            lines = source.strip().split('\n')
            if not lines:
                continue
                
            first_line = lines[0].strip()
            
            # Check if it matches the split level
            if split_level == '#':
                # Match H1: # Title (but not ## Title)
                if first_line.startswith('# ') and not first_line.startswith('## '):
                    markers.append({
                        'index': idx,
                        'block_num': len(markers) + 1,  # Auto-number
                        'title': first_line
                    })
            elif split_level == '##':
                # Match H2: ## Title (but not ### Title)
                if first_line.startswith('## ') and not first_line.startswith('### '):
                    markers.append({
                        'index': idx,
                        'block_num': len(markers) + 1,  # Auto-number
                        'title': first_line
                    })
    
    return markers


def split_notebook_by_blocks(notebook, markers):
    """Split notebook into multiple notebooks based on block markers."""
    blocks = {}
    cells = notebook['cells']
    
    # If no markers found, return the whole notebook as block 01
    if not markers:
        print("⚠️  No block markers found. Treating entire notebook as Block 01.")
        blocks[1] = cells
        return blocks
    
    # Sort markers by index
    markers = sorted(markers, key=lambda x: x['index'])
    
    # Split cells into blocks
    for i, marker in enumerate(markers):
        start_idx = marker['index']
        
        # Find end index (start of next block or end of notebook)
        if i < len(markers) - 1:
            end_idx = markers[i + 1]['index']
        else:
            end_idx = len(cells)
        
        block_num = marker['block_num']
        blocks[block_num] = cells[start_idx:end_idx]
        
        print(f"📦 Block {block_num:02d}: {marker['title']} ({end_idx - start_idx} cells)")
    
    return blocks


def generate_filename(block_num, block_title=None):
    """Generate a filename for a block."""
    # Try to extract a meaningful name from the title
    if block_title:
        # Remove markdown symbols and clean up
        clean_title = re.sub(r'[#*`]', '', block_title)
        clean_title = clean_title.strip().lower()
        
        # Extract key words
        words = clean_title.split()
        if len(words) > 1:
            # Take first 2-3 meaningful words
            meaningful_words = [w for w in words if len(w) > 3 and w not in ['block', 'teil', 'the', 'and', 'oder']]
            if meaningful_words:
                name_part = '_'.join(meaningful_words[:3])
                return f"{block_num:02d}_{name_part}.ipynb"
    
    # Default naming
    return f"{block_num:02d}_block.ipynb"


def main():
    if len(sys.argv) < 2:
        print("Usage: python split_notebook.py <input_notebook.ipynb> [output_directory] [split_level]")
        print("\nExamples:")
        print("  python split_notebook.py Main.ipynb notebooks/")
        print("  python split_notebook.py Main.ipynb notebooks/ #    # Split on H1 (# Title)")
        print("  python split_notebook.py Main.ipynb notebooks/ ##   # Split on H2 (## Title)")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_dir = sys.argv[2] if len(sys.argv) > 2 else 'notebooks/'
    split_level = sys.argv[3] if len(sys.argv) > 3 else '#'  # Default: split on H1
    
    # Validate split level
    if split_level not in ['#', '##']:
        print(f"⚠️  Invalid split level: {split_level}")
        print("   Valid options: '#' (H1) or '##' (H2)")
        split_level = '#'
        print(f"   Using default: {split_level}")
    
    # Check if input file exists
    if not os.path.exists(input_file):
        print(f"❌ Error: File not found: {input_file}")
        sys.exit(1)
    
    # Create output directory if it doesn't exist
    Path(output_dir).mkdir(parents=True, exist_ok=True)
    
    print(f"\n📖 Loading notebook: {input_file}")
    notebook = load_notebook(input_file)
    
    print(f"📊 Total cells: {len(notebook['cells'])}")
    
    # Find block markers
    print(f"\n🔍 Searching for block markers (split level: {split_level})...")
    markers = find_block_markers(notebook, split_level)
    
    if markers:
        print(f"✅ Found {len(markers)} blocks:")
        for marker in markers:
            print(f"   - Block {marker['block_num']:02d}: {marker['title']}")
    else:
        print("⚠️  No block markers found. Will create single notebook.")
    
    # Split notebook
    print("\n✂️  Splitting notebook...")
    blocks = split_notebook_by_blocks(notebook, markers)
    
    # Save each block as a separate notebook
    print("\n💾 Saving notebooks...")
    for block_num in sorted(blocks.keys()):
        # Create new notebook
        new_notebook = create_empty_notebook()
        new_notebook['cells'] = blocks[block_num]
        
        # Copy metadata from original
        if 'metadata' in notebook:
            new_notebook['metadata'].update(notebook['metadata'])
        
        # Generate filename
        marker = next((m for m in markers if m['block_num'] == block_num), None)
        filename = generate_filename(block_num, marker['title'] if marker else None)
        
        # Save
        output_path = os.path.join(output_dir, filename)
        save_notebook(new_notebook, output_path)
    
    print(f"\n✅ Done! Created {len(blocks)} notebooks in {output_dir}")
    print("\n📝 Summary:")
    for block_num in sorted(blocks.keys()):
        marker = next((m for m in markers if m['block_num'] == block_num), None)
        filename = generate_filename(block_num, marker['title'] if marker else None)
        print(f"   Block {block_num:02d} → {filename} ({len(blocks[block_num])} cells)")


if __name__ == '__main__':
    main()

# Made with Bob
