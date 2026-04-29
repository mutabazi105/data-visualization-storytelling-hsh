# 📓 Notebook Splitting Guide

## 🎯 Zweck

Das `split_notebook.py` Script teilt ein großes Jupyter Notebook automatisch in mehrere kleinere Notebooks auf, basierend auf Markdown-Überschriften.

---

## 🚀 Verwendung

### Basis-Verwendung

```bash
python split_notebook.py <input_notebook.ipynb> <output_directory>
```

### Beispiel

```bash
# Main-Notebook in separate Blöcke aufteilen
python split_notebook.py optional/advanced-content/week-1/Main_Kopie_von_Intro_to_matplotlib.ipynb notebooks/

# Oder mit relativem Pfad
python split_notebook.py fundamentals/Main_Kopie_von_Intro_to_matplotlib.ipynb notebooks/
```

---

## 📋 Was macht das Script?

1. **Lädt das Notebook** - Liest die .ipynb Datei
2. **Sucht nach Block-Markern** - Findet Überschriften wie:
   - `## Block 01`
   - `## Block 02`
   - `# Block 1`
   - `## Teil 1`
   - etc.
3. **Teilt das Notebook** - Erstellt separate Notebooks für jeden Block
4. **Speichert die Notebooks** - Mit automatischen Dateinamen

---

## 📝 Unterstützte Block-Marker

Das Script erkennt folgende Muster in Markdown-Zellen:

```markdown
## Block 01
## Block 02
# Block 1
# Block 2
## 01. Einführung
## Teil 1
## Teil 2
```

**Wichtig:** Die Marker müssen in **Markdown-Zellen** stehen, nicht in Code-Zellen!

---

## 📂 Output

### Dateinamen

Das Script generiert automatisch Dateinamen:

| Block-Titel | Generierter Dateiname |
|-------------|----------------------|
| `## Block 01 - Matplotlib Basics` | `01_matplotlib_basics.ipynb` |
| `## Block 02 - Pandas Plotting` | `02_pandas_plotting.ipynb` |
| `## Block 03` | `03_block.ipynb` |

### Struktur

Jedes neue Notebook enthält:
- Alle Zellen von diesem Block bis zum nächsten Block
- Die Original-Metadaten (Kernel, etc.)
- Vollständige Jupyter Notebook Struktur

---

## 🔍 Beispiel-Output

```bash
$ python split_notebook.py Main_Kopie_von_Intro_to_matplotlib.ipynb notebooks/

📖 Loading notebook: Main_Kopie_von_Intro_to_matplotlib.ipynb
📊 Total cells: 150

🔍 Searching for block markers...
✅ Found 5 blocks:
   - Block 01: ## Block 01 - Matplotlib Grundlagen
   - Block 02: ## Block 02 - Pandas Integration
   - Block 03: ## Block 03 - Fortgeschrittene Plots
   - Block 04: ## Block 04 - Customization
   - Block 05: ## Block 05 - Projekt

✂️  Splitting notebook...
📦 Block 01: ## Block 01 - Matplotlib Grundlagen (30 cells)
📦 Block 02: ## Block 02 - Pandas Integration (25 cells)
📦 Block 03: ## Block 03 - Fortgeschrittene Plots (35 cells)
📦 Block 04: ## Block 04 - Customization (28 cells)
📦 Block 05: ## Block 05 - Projekt (32 cells)

💾 Saving notebooks...
✅ Saved: notebooks/01_matplotlib_grundlagen.ipynb
✅ Saved: notebooks/02_pandas_integration.ipynb
✅ Saved: notebooks/03_fortgeschrittene_plots.ipynb
✅ Saved: notebooks/04_customization.ipynb
✅ Saved: notebooks/05_projekt.ipynb

✅ Done! Created 5 notebooks in notebooks/

📝 Summary:
   Block 01 → 01_matplotlib_grundlagen.ipynb (30 cells)
   Block 02 → 02_pandas_integration.ipynb (25 cells)
   Block 03 → 03_fortgeschrittene_plots.ipynb (35 cells)
   Block 04 → 04_customization.ipynb (28 cells)
   Block 05 → 05_projekt.ipynb (32 cells)
```

---

## ⚠️ Wichtige Hinweise

### Wenn keine Block-Marker gefunden werden

Wenn das Script keine Block-Marker findet:
```
⚠️  No block markers found. Treating entire notebook as Block 01.
```

Das gesamte Notebook wird als `01_block.ipynb` gespeichert.

### Voraussetzungen

- Python 3.6 oder höher
- Keine zusätzlichen Bibliotheken nötig (nur Standard-Library)

### Backup

**Wichtig:** Das Original-Notebook wird NICHT verändert!
- Das Script liest nur
- Alle neuen Notebooks werden im Output-Verzeichnis erstellt
- Das Original bleibt unverändert

---

## 🛠️ Anpassungen

### Eigene Block-Marker hinzufügen

Bearbeite die `patterns` Liste in der Funktion `find_block_markers()`:

```python
patterns = [
    r'##\s*Block\s*(\d+)',      # ## Block 01
    r'#\s*Block\s*(\d+)',       # # Block 1
    r'##\s*(\d+)\.',            # ## 01.
    r'#\s*Teil\s*(\d+)',        # # Teil 1
    r'##\s*Teil\s*(\d+)',       # ## Teil 1
    r'##\s*Kapitel\s*(\d+)',    # ## Kapitel 1 (NEU)
]
```

### Dateinamen-Format ändern

Bearbeite die Funktion `generate_filename()` für eigene Namenskonventionen.

---

## 📚 Verwendung im Kurs

### Für Dozenten

```bash
# 1. Main-Notebook aufteilen
python split_notebook.py optional/advanced-content/week-1/Main_Kopie_von_Intro_to_matplotlib.ipynb notebooks/

# 2. Notebooks umbenennen (optional)
mv notebooks/01_matplotlib_grundlagen.ipynb notebooks/01_intro_matplotlib.ipynb
mv notebooks/02_pandas_integration.ipynb notebooks/02_pandas_plotting.ipynb

# 3. Für Teilnehmer bereitstellen
# Die Notebooks sind jetzt in notebooks/ und bereit für den Kurs!
```

### Für Teilnehmer

Die aufgeteilten Notebooks sind einfacher zu verstehen:
- ✅ Kleinere, fokussierte Notebooks
- ✅ Klare Themen pro Notebook
- ✅ Einfacher zu navigieren
- ✅ Besser für schrittweises Lernen

---

## 🐛 Troubleshooting

### Problem: "File not found"
```bash
❌ Error: File not found: Main_Kopie_von_Intro_to_matplotlib.ipynb
```

**Lösung:** Prüfe den Pfad zum Notebook:
```bash
ls -la optional/advanced-content/week-1/Main_Kopie_von_Intro_to_matplotlib.ipynb
```

### Problem: Keine Blöcke gefunden
```
⚠️  No block markers found.
```

**Lösung:** 
1. Öffne das Notebook in Jupyter
2. Füge Markdown-Zellen mit Block-Markern hinzu:
   ```markdown
   ## Block 01 - Einführung
   ```
3. Speichere das Notebook
4. Führe das Script erneut aus

### Problem: Falsche Dateinamen

**Lösung:** Passe die `generate_filename()` Funktion an oder benenne die Dateien manuell um.

---

## ✅ Checkliste

Vor dem Ausführen:
- [ ] Python 3.6+ installiert
- [ ] Pfad zum Input-Notebook korrekt
- [ ] Output-Verzeichnis existiert (oder wird erstellt)
- [ ] Backup des Original-Notebooks (optional, aber empfohlen)

Nach dem Ausführen:
- [ ] Alle Notebooks erstellt
- [ ] Dateinamen sinnvoll
- [ ] Notebooks öffnen sich in Jupyter
- [ ] Inhalt ist korrekt aufgeteilt

---

## 📞 Support

Bei Problemen:
1. Prüfe die Fehlermeldung
2. Siehe Troubleshooting-Sektion
3. Öffne ein Issue auf GitHub

---

*Letzte Aktualisierung: April 2026*  
*Version: 1.0*