# Projekt: Data Visualization & Storytelling 📊

Willkommen zu unserem 2-Wochen-Kurs! Hier lernen wir, wie man mit Daten Geschichten erzählt.

## 🎯 Unsere Ziele
1. **Daten verstehen**: Wir arbeiten mit echten Daten (z. B. Wetter in Hannover).
2. **Visualisierung**: Wir erstellen klare Diagramme mit `Matplotlib` und `Pandas`.
3. **Storytelling**: Wir finden eine Antwort auf eine spannende Frage.

## 📂 Struktur
- `/data`: Unsere Datensätze (.csv und .json).
- `/woche-1`: Hier findet ihr den Code aus den Kursstunden.
- `/woche-2`: Hier findet ihr den Code aus den Kursstunden.

- `/optional`: Fortgeschrittene Inhalte für später.

## 🛠 Was wir bisher gemacht haben

### 📚 Woche 1: Matplotlib Grundlagen

#### 01 - Figure & Axes Konzept
**Was ist das?** Die **Figure-Instanz** ist wie eine leere Leinwand in Matplotlib. Darauf zeichnen wir unsere Diagramme.

**Zwei Wege zum Plotten:**
- **pyplot** (`plt.plot()`) - Schnell und einfach, wie MATLAB
- **OO-Interface** (`fig, ax = plt.subplots()`) - Mehr Kontrolle

**Referenz:** Dies ist der erste Block aus dem Haupt-Notebook im `fundamentals/` Ordner (zum selber Editieren!).

---

#### 02 - Pyplot API (MATLAB-Style)
**Was ist das?** Die **pyplot API** ist das einfache Interface - `plt` managed automatisch Figure und Axes für uns!

**Wichtig:** Die `.plot()` Methode funktioniert auch direkt auf **Pandas DataFrames**!

**Beispiel:**
```python
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data/hannover_temp.csv')
plt.plot(df['datum'], df['temperatur'])  # Direkt aus DataFrame!
plt.show()
```

---

#### 03 - Working with actual data! 📊
**Ab hier arbeiten wir mit echten Daten aus CSV-Dateien!**

**Gruppenarbeit (Tag 3):**
- 📋 **Anleitung:** [`woche-1/Part1/03_anleitung.md`](woche-1/Part1/03_anleitung.md) - Schritt-für-Schritt Guide
- 🎯 **Fragen:** [`woche-1/03_fragen.md`](woche-1/03_fragen.md) - 5 Gruppen, 5 verschiedene Fragen
- 📊 **Datensätze:** Temperatur, Auto-Preise, Herzerkrankungen, etc.

**Verbindung:** Die Gruppenarbeit nutzt die Befehle aus Tag 1-2 und wendet sie auf echte Daten an!

---

### 📊 Woche 2: Storytelling & Datensammlung

#### Präsentationen mit dem Storytelling-Framework
**Jede Woche hat eine Präsentation!**

- 📄 **Workflow-PDF:** [`woche-1/06-workflow.pdf`](woche-1/06-workflow.pdf) - Visueller Workflow
- 📖 **Storytelling-Leitfaden (Dozent-Beispiel):** [`job_scraper/storytelling_leitfaden_b1.md`](job_scraper/storytelling_leitfaden_b1.md) - Ausgefüllt vom Dozenten als Beispiel
- ✍️ **Storytelling-Vorlage (für Teilnehmer):** [`week-1/storytelling_leitfaden_b1 copy.md`](week-1/storytelling_leitfaden_b1%20copy.md) - Zum Ausfüllen

**Framework:** Context (Intrigue) → Perceiving → Interpreting → Comprehending

---

#### Datensammlung: Von manuell bis automatisch
**Drei Wege, Daten zu sammeln:**

1. **Manuell (JSON):** Wie eine Einkaufsliste - einfach und schnell!
2. **Microsoft Forms:** Strukturierte Umfragen mit automatischem CSV-Export
3. **Python-Backend:** Job-Scraper-Anwendung (ähnliche Installation wie unser Kurs!)

## 📖 Leitfaden: Was ist ein guter Plot?

Bevor du dein Diagramm fertigstellst, prüfe diese Punkte:

1. **Titel**: Versteht man sofort, worum es geht?
2. **Achsen**: Sind `xlabel` und `ylabel` beschriftet?
3. **Legende**: Wenn es mehrere Linien gibt, weiß man, welche welche ist?
4. **Farben**: Sind die Farben hilfreich oder verwirrend?
5. **Story**: Welche Frage beantwortet dieser Plot? (z. B. "Ist es in Hannover wärmer als in Berlin?")

📄 **Vollständige Checkliste**: Siehe [`woche-1/04_checkliste.md`](woche-1/04_checkliste.md)

## 📚 Unsere Notebooks

### Woche 1: Grundlagen
1. **[Main_Kopie_von_Intro_to_matplotlib.ipynb](woche-1/Main_Kopie_von_Intro_to_matplotlib.ipynb)** - Erste Schritte mit Matplotlib

### Fortgeschritten:
- **[advanced-content/week-1/](advanced-content/week-1/)** - Erweiterte Notebooks
- **[advanced-content/week-2/](advanced-content/week-2/)** - Weitere Notebooks

## 📊 Unsere Datensätze

Im `data/` Ordner findest du:
- `hannover_temp.csv` - Temperaturdaten aus Hannover
- `car-sales.csv` - Autoverkaufsdaten
- `heart-disease.csv` - Gesundheitsdaten
- `student_performance.csv` - Studentenleistungen
- `online_retail_sample.csv` - Online-Shop Verkäufe

## 🎓 Storytelling Framework

Wir nutzen das **Context + Perceiving → Interpreting → Comprehending** Framework.

📄 **Vollständiger Leitfaden**: Siehe [`woche-2/05_story_framework.md`](woche-2/05_story_framework.md)

### Die 3 Schritte:

1. **PERCEIVING** (Was zeigt es?)
   - Wo ist groß, mittel, klein?
   - Wie vergleichen sich die Dinge?
   - Welche Beziehungen existieren?

2. **INTERPRETING** (Was bedeutet es?)
   - Was ist gut und was ist schlecht?
   - Ist es bedeutungsvoll oder unwichtig?
   - Ist es ungewöhnlich oder erwartet?

3. **COMPREHENDING** (Was bedeutet es für mich?)
   - Was sind die Hauptbotschaften?
   - Was habe ich gelernt?
   - Welche Aktionen kann ich machen?

## 🚀 Schnellstart

### Installation

#### Option 1: Mit pip (Standard)

```bash
# Python-Bibliotheken installieren
pip install pandas matplotlib jupyter

# Jupyter Notebook starten
jupyter notebook
```

#### Option 2: Mit uv (Schneller! ⚡)

`uv` ist ein **sehr schneller** Python Package Manager (10-100x schneller als pip!).

**Installation von uv:**
```bash
# macOS/Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

**Dann Bibliotheken installieren:**
```bash
# Mit uv installieren (viel schneller!)
uv pip install pandas matplotlib jupyter

# Jupyter Notebook starten
jupyter notebook
```

**Warum uv?**
- ⚡ 10-100x schneller als pip
- 📦 Gleiche Befehle wie pip (`uv pip install ...`)
- ✅ Funktioniert genauso wie pip

📄 **Vollständige Installations-Anleitung:** Siehe [`job_scraper/INSTALLATION.md`](job_scraper/INSTALLATION.md)

**Tipp:** In Woche 2 zeigen wir eine **Job-Scraping-Anwendung** mit Python-Backend. Die Installation ist ähnlich! (Siehe `job_scraper/`)

### Dein erstes Diagramm

```python
import pandas as pd
import matplotlib.pyplot as plt

# Daten laden
df = pd.read_csv('data/hannover_temp.csv')

# Plot erstellen
plt.plot(df['datum'], df['temperatur'], color='teal')
plt.title('Temperatur in Hannover')
plt.xlabel('Datum')
plt.ylabel('Temperatur (°C)')
plt.grid(True)
plt.show()
```

## 📝 Schritt-für-Schritt zum perfekten Plot

| Element | Was muss ich tun? | Matplotlib-Code (Beispiel) |
| :--- | :--- | :--- |
| **Daten** | X- und Y-Werte definieren | `plt.plot(x, y)` |
| **Farbe** | Eine klare Farbe wählen | `color='teal'` oder `'red'` |
| **Titel** | Eine Überschrift hinzufügen | `plt.title("Temperatur in Hannover")` |
| **Achsen** | Namen für X und Y geben | `plt.xlabel("Monat")`, `plt.ylabel("Grad Celsius")` |
| **Styling** | Gitter oder Linientyp | `plt.grid(True)`, `linestyle='--'` |

## 💡 Tipps für die "Story"-Stunde

Um eine gute Story zu erzählen, stelle dir diese **3 Fragen**:

1. **Beobachtung**: "Was ist das Extremste in deinen Daten?" (Höchste Temperatur, tiefster Punkt)
2. **Vergleich**: "Was ist der Unterschied zwischen A und B?"
3. **Warum?**: "Was glaubst du, warum sehen die Daten so aus?"

## 🔧 Manuelle Datensammlung (JSON)

JSON sieht aus wie eine Einkaufsliste:

```json
{
  "tag": "Montag",
  "stimmung": 8,
  "kaffee_getrunken": 3
}
```

Das ist einfacher als komplexe Tabellen!

## 📚 Für Fortgeschrittene

Wenn du mehr lernen möchtest, schau in den **`advanced-content/`** Ordner:

- **[advanced-content/week-1/](advanced-content/week-1/)** - Erweiterte Woche 1 Materialien
- **[advanced-content/week-2/](advanced-content/week-2/)** - Erweiterte Woche 2 Materialien
- **[advanced-content/fundamentals/](advanced-content/fundamentals/)** - Tiefere Grundlagen
- **[optional/advanced-uni-level/](optional/advanced-uni-level/)** - Universitätsniveau
- **[PROJEKT_BESCHREIBUNG.md](PROJEKT_BESCHREIBUNG.md)** - Vollständige Kursbeschreibung (für Dozenten)

## 📞 Hilfe & Unterstützung

- **Fragen?** Nutze die Office Hours
- **Probleme?** Schau in die Materialien: [`woche-1/`](woche-1/) und [`woche-2/`](woche-2/)
- **Mehr lernen?** Erkunde [`advanced-content/`](advanced-content/)

## 🎯 Deine Aufgabe

1. Öffne `woche-1/Main_Kopie_von_Intro_to_matplotlib.ipynb`
2. Wähle einen Datensatz aus `data/`
3. Erstelle eine Visualisierung
4. Beantworte die Story-Fragen (Perceiving → Interpreting → Comprehending)
5. Präsentiere deine Story!

## ✅ Checkliste für dein Projekt

- [ ] Datensatz ausgewählt
- [ ] Intrigue definiert (Warum erzähle ich das?)
- [ ] Plot erstellt mit Titel und Achsenbeschriftungen
- [ ] PERCEIVING: Was zeigt der Plot?
- [ ] INTERPRETING: Was bedeutet es?
- [ ] COMPREHENDING: Was habe ich gelernt?
- [ ] Story ist vollständig!

---

**Viel Erfolg mit dem Kurs!** 🎓📊✨

*Sprachniveau: B1 (Deutsch)*  
*Letzte Aktualisierung: April 2026*