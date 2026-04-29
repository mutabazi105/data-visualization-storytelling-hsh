#!/usr/bin/env python3
"""
Fix notebook formatting:
1. Convert text-based notebook to proper JSON
2. Add JSON formatter for pretty dict/list display
3. Replace print(dict) with dict as last expression
"""

import json
import re

def create_proper_notebook_from_text(text_file, output_file):
    """Convert text-based notebook to proper Jupyter format"""
    
    with open(text_file, 'r') as f:
        content = f.read()
    
    # Split by markdown headers (##)
    sections = re.split(r'^## ', content, flags=re.MULTILINE)
    
    cells = []
    
    # Add title cell
    cells.append({
        "cell_type": "markdown",
        "metadata": {},
        "source": [
            "# Hannover Messe Survey Analysis - Modular Notebook\n",
            "\n",
            "This notebook analyzes student participation and engagement at the Hannover Messe fair.\n",
            "\n",
            "**Features:**\n",
            "- Supports manual sample data (14 students from Hannover Messe)\n",
            "- Supports Microsoft Forms CSV export import\n",
            "- Modular functions for data loading, cleaning, analysis, and visualization\n",
            "- Configurable column mapping for Microsoft Forms exports\n",
            "\n",
            "**Analysis includes:**\n",
            "- Attendance and networking behavior\n",
            "- Job positions discovered\n",
            "- Companies visited\n",
            "- Career fields explored\n",
            "- Overall specialization distribution"
        ]
    })
    
    # Add JSON formatter cell
    cells.append({
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": [
            "import IPython\n",
            "from IPython.display import JSON\n",
            "\n",
            "def custom_formatter(obj, p, cycle):\n",
            "    if isinstance(obj, (dict, list)):\n",
            "        return IPython.display.display(JSON(obj))\n",
            "\n",
            "# Register the formatter for the interactive shell\n",
            "ip = get_ipython()\n",
            "ip.display_formatter.formatters['text/plain'].for_type(dict, custom_formatter)"
        ]
    })
    
    # Process each section
    for section in sections[1:]:  # Skip first empty split
        lines = section.split('\n')
        title = lines[0].strip()
        
        # Add markdown cell for section title
        cells.append({
            "cell_type": "markdown",
            "metadata": {},
            "source": [f"## {title}"]
        })
        
        # Collect code lines
        code_lines = []
        in_code = False
        
        for line in lines[1:]:
            # Skip empty lines at start
            if not in_code and not line.strip():
                continue
            
            # Check if it's a code line (not starting with #, not empty after code started)
            if line.strip() and not line.startswith('##'):
                in_code = True
                code_lines.append(line)
        
        # Add code cell if we have code
        if code_lines:
            # Join lines and clean up
            code = '\n'.join(code_lines)
            
            # Fix: Replace print(messe_data) with just messe_data
            code = re.sub(r'print\((messe_data)\)', r'\1', code)
            
            cells.append({
                "cell_type": "code",
                "execution_count": None,
                "metadata": {},
                "outputs": [],
                "source": code.split('\n')
            })
    
    # Create notebook structure
    notebook = {
        "cells": cells,
        "metadata": {
            "kernelspec": {
                "display_name": "Python 3",
                "language": "python",
                "name": "python3"
            },
            "language_info": {
                "codemirror_mode": {
                    "name": "ipython",
                    "version": 3
                },
                "file_extension": ".py",
                "mimetype": "text/x-python",
                "name": "python",
                "nbconvert_exporter": "python",
                "pygments_lexer": "ipython3",
                "version": "3.9.0"
            }
        },
        "nbformat": 4,
        "nbformat_minor": 4
    }
    
    # Write to file
    with open(output_file, 'w') as f:
        json.dump(notebook, f, indent=1)
    
    print(f"✅ Created proper notebook: {output_file}")

def add_json_formatter_to_existing(notebook_file):
    """Add JSON formatter to existing notebook if not present"""
    
    with open(notebook_file, 'r') as f:
        nb = json.load(f)
    
    # Check if JSON formatter already exists
    has_formatter = False
    for cell in nb['cells']:
        if cell['cell_type'] == 'code':
            source = ''.join(cell['source'])
            if 'custom_formatter' in source and 'JSON' in source:
                has_formatter = True
                print(f"✅ {notebook_file} already has JSON formatter")
                break
    
    if not has_formatter:
        # Add formatter as second cell (after imports)
        formatter_cell = {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "import IPython\n",
                "from IPython.display import JSON\n",
                "\n",
                "def custom_formatter(obj, p, cycle):\n",
                "    if isinstance(obj, (dict, list)):\n",
                "        return IPython.display.display(JSON(obj))\n",
                "\n",
                "# Register the formatter for the interactive shell\n",
                "ip = get_ipython()\n",
                "ip.display_formatter.formatters['text/plain'].for_type(dict, custom_formatter)"
            ]
        }
        
        # Insert after first code cell (usually imports)
        insert_pos = 1
        for i, cell in enumerate(nb['cells']):
            if cell['cell_type'] == 'code':
                insert_pos = i + 1
                break
        
        nb['cells'].insert(insert_pos, formatter_cell)
        
        # Write back
        with open(notebook_file, 'w') as f:
            json.dump(nb, f, indent=1)
        
        print(f"✅ Added JSON formatter to {notebook_file}")
    
    # Fix print(dict) statements
    modified = False
    for cell in nb['cells']:
        if cell['cell_type'] == 'code':
            source = ''.join(cell['source'])
            
            # Replace print(messe_data) with messe_data
            new_source = re.sub(r'print\((messe_data)\)', r'\1', source)
            
            if new_source != source:
                cell['source'] = new_source.split('\n')
                modified = True
    
    if modified:
        with open(notebook_file, 'w') as f:
            json.dump(nb, f, indent=1)
        print(f"✅ Fixed print() statements in {notebook_file}")

if __name__ == '__main__':
    # Fix the text-based notebook
    print("Converting text-based notebook to proper JSON format...")
    create_proper_notebook_from_text(
        'student_data_structured.ipynb',
        'student_data_structured_fixed.ipynb'
    )
    
    # Fix the copy notebook
    print("\nUpdating copy notebook...")
    add_json_formatter_to_existing('student_data_structured copy.ipynb')
    
    print("\n✅ All notebooks fixed!")
    print("\nNext steps:")
    print("1. Open 'student_data_structured_fixed.ipynb' in Jupyter")
    print("2. Run all cells")
    print("3. Dictionaries will display as interactive JSON")
    print("4. Replace old 'student_data_structured.ipynb' with the fixed version if satisfied")

# Made with Bob
