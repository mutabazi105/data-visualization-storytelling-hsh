# 📊 Data Visualization & Storytelling - 2 Wochen Kurs

## 🎯 Was machen wir in diesem Kurs?

Wir lernen, wie man **Daten visualisiert** und **Geschichten mit Daten erzählt**.

---

## 📅 Kursablauf (2 Wochen = 10 Werktage)

### **Woche 1 (Tag 1-5)**

#### **Tag 1-2: Erste Notebooks** 📓
- **Notebooks:**
  - `01_intro_matplotlib.ipynb` - Matplotlib Grundlagen
  - `02_pandas_plotting.ipynb` - Plotting mit Pandas
  - `01_was_haben_wir_gelernt.md` - Zusammenfassung
- **Problem:** Nicht so gut verstanden von den Teilnehmern
- **Lösung:** Mehr Zeit für Basics, langsameres Tempo

#### **Tag 3: Gruppenarbeit** 👥
- **Was:** In-Person Session mit echten Daten
- **Daten:** CSV-Dateien aus `data/` Ordner
- **Gruppen:** 5 Gruppen
- **Dateien:**
  - `02_anleitung.md` - Wie arbeiten wir in Gruppen?
  - `03_fragen.md` - Welche Frage beantwortest du?

---

## 📋 Die 5 Gruppenaufgaben

### 🌡️ Gruppe 1 – Temperatur Hannover (Einfach)

**Datensatz:** `data/hannover_temp.csv`

**Diagramm-Vorgabe:**
- **x-Achse:** Zeit (22. April bis 7. Mai 2026, täglich = 16 Tage)
- **y-Achse:** Temperatur (°C)

**❓ Fragen (genau diese beantworten!):**
1. Steigt oder sinkt die Temperatur insgesamt über den Zeitraum?
2. An welchem Datum ist die Temperatur am höchsten?
3. An welchem Datum ist die Temperatur am niedrigsten?
4. Gibt es starke Schwankungen oder verläuft die Temperatur eher ruhig?

---

### 🚗 Gruppe 2 – Auto-Verkäufe (Zusammenhang)

**Datensatz:** `data/car-sales.csv`

**Diagramm-Vorgabe:**
- **Typ:** Scatter Plot
- **x-Achse:** Odometer (Kilometer)
- **y-Achse:** Price (Preis)

**❓ Fragen:**
1. Wie entwickelt sich der Preis in Bezug auf die Kilometerzahl? (steigt / fällt / bleibt gleich)
2. Gibt es Autos mit besonders hohem oder niedrigem Preis?
3. Gibt es einen auffälligen Zusammenhang zwischen Kilometern und Preis?
4. Was könnte ein Autohändler aus diesem Diagramm lernen? (z. B. „Autos mit weniger Kilometern sind teurer")

---

### 🌡️ Gruppe 3 – Temperatur-Vergleich (Zwei Städte)

**Datensatz:** `data/hannover_temp.csv` + eine zweite Stadt (z.B. Berlin)

**Diagramm-Vorgabe:**
- **Typ:** Line Chart mit zwei Linien
- **x-Achse:** Zeit
- **y-Achse:** Temperatur (°C)
- **Zwei Messreihen:** z. B. Stadt A und Stadt B

**❓ Fragen:**
1. Welche Temperatur-Reihe ist insgesamt höher?
2. Gibt es Zeitpunkte, an denen sich die Temperaturen stark unterscheiden?
3. Gibt es Zeitpunkte, an denen die Temperaturen sehr ähnlich sind?
4. Welche Reihe zeigt stärkere Schwankungen?

---

### ❤️ Gruppe 4 – Heart Disease (Zusammenhang)

**Datensatz:** `data/heart-disease.csv`

**Diagramm-Vorgabe:**
- **Typ:** Scatter Plot
- **x-Achse:** age (Alter)
- **y-Achse:** chol (Cholesterin) **oder** trestbps (Blutdruck)

**❓ Fragen:**
1. Gibt es einen Zusammenhang zwischen Alter und Cholesterin/Blutdruck? (ja / nein / unklar)
2. Steigen die Cholesterin-/Blutdruck-Werte, wenn das Alter größer wird?
3. Gibt es Ausreißer (Punkte, die nicht ins Muster passen)?
4. Kann man aus diesem Diagramm sicher sagen: „Alter verursacht höheres Cholesterin"? (ja oder nein + ein Satz Begründung)

---

### 🌡️ Gruppe 5 – Temperatur (Auffälligkeiten & Story)

**Datensatz:** `data/hannover_temp.csv` (mit künstlicher Anomalie)

**Diagramm-Vorgabe:**
- **x-Achse:** Zeit (22. April bis 7. Mai 2026, täglich = 16 Tage)
- **y-Achse:** Temperatur (°C)
- **Besonderheit:** Datensatz enthält eine auffällige Veränderung (z. B. plötzlicher Temperaturabfall am 28. April)

**❓ Fragen:**
1. Gibt es einen plötzlichen Temperaturanstieg oder -abfall?
2. An welchem Datum passiert diese auffällige Veränderung?
3. Warum fällt dieser Punkt besonders auf? (nur beschreiben, z. B. „Die Temperatur fällt um 10°C an einem Tag")
4. Wie verhält sich die Temperatur vor und nach dieser Veränderung?

---

### **Woche 2 (Tag 6-10)**

#### **Tag 4: Plot-Bewertung** ⚠️
- **Problem:** Zu schnell besprochen!
- **Dateien:**
  - `04_leitfaden_langsam.md` ⭐ **WICHTIG!** Schritt-für-Schritt (10 Min pro Schritt)
  - `04_checkliste.md` - Was ist ein guter Plot?
  - `04_matplotlib_parameter.md` - Parameter-Referenz

#### **Tag 5: Story entwickeln** 📖
- **Was:** Alle sollen eine "Story" haben
- **Framework:** Perceiving → Interpreting → Comprehending
- **Dateien:**
  - `05_story_framework.md` - Wie erzähle ich eine Story?
  - `05_basics_wiederholung.ipynb` - Basics nochmal
  - `05_beobachtungen_vorlage.md` - Template für Beobachtungen

#### **Tag 6 (Freitag): Daten sammeln mit Forms** 📝
- **Was:** Microsoft Forms zeigen
- **Ziel:** Wie sammelt man eigene Daten?
- **Dateien:**
  - `woche-2/Part-1-Data-Integration/06_forms_anleitung.md` - Schritt-für-Schritt (falls vorhanden)
  - `forms_to_csv_adapter.py` - Tool zum Konvertieren (im Root)
  - `woche-2/Part-1-Data-Integration/06_beispiel_form.md` - Beispiel-Formular

#### **Tag 7 (Donnerstag): Manuelle Daten** ✍️
- **Was:** Daten manuell aufschreiben
- **Format:** JSON (unstrukturiert)
- **Dateien:**
  - `07_json_basics.md` - JSON wie eine Einkaufsliste
  - `07_beispiel_daten.json` - Beispiel
  - `07_json_zu_plot.ipynb` - Von JSON zum Plot

---

## 📁 GitHub Struktur (Vereinfacht mit Nummern)

```
projekt-datenviz/
│
├── README.md                           # Einstieg für Teilnehmer (B1)
├── PROJEKT_BESCHREIBUNG.md             # Diese Datei (Kursübersicht)
├── MIGRATION_GUIDE.md                  # Strukturdokumentation
├── NOTEBOOK_SPLITTING_GUIDE.md         # Tool-Anleitung
│
├── notebooks/                          # Haupt-Notebooks (Tag 1-2)
│   ├── 01_intro_matplotlib.ipynb
│   ├── 02_pandas_plotting.ipynb
│   └── 03_unser_projekt.ipynb
│
├── woche-1/                            # Woche 1 Materialien
│   ├── 01_was_haben_wir_gelernt.md     # Tag 1-2 Zusammenfassung
│   ├── 02_anleitung.md                 # Tag 3: Gruppenarbeit-Anleitung
│   ├── 03_fragen.md                    # Tag 3: Die 5 Gruppenaufgaben
│   ├── 04_leitfaden_langsam.md         # Tag 4: Plot-Bewertung LANGSAM ⭐
│   └── 04_checkliste.md                # Tag 4: Checkliste
│
├── woche-2/                            # Woche 2 Materialien
│   ├── 04_matplotlib_parameter.md      # Tag 4: Parameter-Referenz
│   ├── 05_story_framework.md           # Tag 5: Story-Framework
│   ├── 05_beobachtungen_vorlage.md     # Tag 5: Template (falls vorhanden)
│   ├── 06_beispiel_form.md             # Tag 6: Beispiel (RAW DATA)
│   ├── 07_1_csv_to_json.md             # Tag 7: CSV → JSON Integration
│   ├── 07_2_data_integration.md        # Tag 7: JSON → DataFrame
│   ├── 07_beispiel_daten.json          # Tag 7: Beispiel
│   └── 07_json_zu_plot.ipynb           # Tag 7: Notebook
│
├── data/                               # Alle Datensätze
│   ├── hannover_temp.csv
│   ├── car-sales.csv
│   ├── heart-disease.csv
│   ├── student_performance.csv
│   └── online_retail_sample.csv
│
├── docs/                               # Hilfen & Leitfäden
│   ├── checkliste_plot.md
│   ├── storytelling_leitfaden_b1.md
│   └── plot_types_and_briefs.md        # Plot-Typen & Briefs Tabelle
│
├── test/                               # Test-Output (Notebook-Splitting)
├── advanced-content/                   # Fortgeschrittene Inhalte
└── projekt_abschluss/                  # Abschlussprojekte
```

---

## 🎯 Hauptprobleme und Lösungen

### Problem 1: Notebooks nicht verstanden (Tag 1-2)
**Lösung:**
- Langsameres Tempo
- Mehr Erklärungen im Code
- `01_was_haben_wir_gelernt.md` mit Zusammenfassung

### Problem 2: Zu schnell bei Plot-Bewertung (Tag 4)
**Lösung:**
- `04_leitfaden_langsam.md` erstellen ⭐ **10 Minuten pro Schritt!**
- `04_checkliste.md` - Schritt-für-Schritt Checkliste
- Beispiele: Gute vs. schlechte Plots

### Problem 3: Story-Entwicklung unklar (Tag 5)
**Lösung:**
- Klares Framework: Perceiving → Interpreting → Comprehending
- `05_beobachtungen_vorlage.md` - Template für Beobachtungen
- `05_basics_wiederholung.ipynb` - Basics nochmal

---

## 📝 Wichtige Dateien (Schnellzugriff)

### Für Teilnehmer:
1. **`woche-1/03_fragen.md`** - Welche Frage beantwortest du?
2. **`woche-1/04_leitfaden_langsam.md`** - Schritt-für-Schritt Plot-Bewertung ⭐
3. **`woche-2/05_story_framework.md`** - Wie erzähle ich eine Story?
4. **`woche-2/07_json_basics.md`** - JSON einfach erklärt

### Für Dozenten:
1. **`woche-1/02_anleitung.md`** - Gruppenarbeit organisieren
2. **`woche-1/04_checkliste.md`** - Was ist ein guter Plot?
3. **`docs/storytelling_leitfaden_b1.md`** - Vollständiger Story-Leitfaden
4. **`docs/plot_types_and_briefs.md`** - Plot-Typen & Briefs Tabelle

---

## 🚀 Schnellstart

### Für Teilnehmer:

**Woche 1:**
```bash
# Tag 1-2: Notebooks öffnen
jupyter notebook notebooks/01_intro_matplotlib.ipynb
jupyter notebook notebooks/02_pandas_plotting.ipynb

# Tag 3: Gruppenarbeit
# 1. Lies: woche-1/02_anleitung.md
# 2. Lies: woche-1/03_fragen.md (wähle deine Gruppe)
# 3. Lade Daten aus: data/
```

**Woche 2:**
```bash
# Tag 4: Plot-Bewertung
# Lies LANGSAM: woche-1/04_leitfaden_langsam.md (10 Min pro Schritt!)

# Tag 5: Story entwickeln
# Nutze: woche-2/05_story_framework.md
# Nutze: woche-2/05_beobachtungen_vorlage.md

# Tag 6: Forms & Data Collection
# Folge: woche-2/Part-1-Data-Integration/06_beispiel_form.md

# Tag 7: JSON
# Öffne: woche-2/07_json_basics.md
# Öffne: woche-2/07_json_zu_plot.ipynb
```

---

## ✅ Checkliste für Dozenten

### Vor dem Kurs:
- [ ] Alle Notebooks testen
- [ ] CSV-Dateien in `data/` prüfen
- [ ] `woche-1/03_fragen.md` ausdrucken (5 Gruppen)
- [ ] `woche-1/04_leitfaden_langsam.md` ausdrucken ⭐ **WICHTIG!**

### Während des Kurses:

**Woche 1:**
- [ ] **Tag 1-2:** Langsames Tempo, viele Pausen, `01_was_haben_wir_gelernt.md` durchgehen
- [ ] **Tag 3:** Gruppen gut einteilen, `02_anleitung.md` + `03_fragen.md` verteilen
- [ ] **Tag 4:** **LANGSAM!** `04_leitfaden_langsam.md` Schritt-für-Schritt (10 Min/Schritt)
- [ ] **Tag 5:** `05_story_framework.md` erklären, Beispiele zeigen

**Woche 2:**
- [ ] **Tag 6:** RAW DATA zeigen (`06_beispiel_form.md`)
- [ ] **Tag 7:** CSV zu JSON Integration (`07_1_csv_to_json.md`)
- [ ] **Tag 7:** JSON zu DataFrame (`07_2_data_integration.md`)

---

## 🎓 Kursziel: Von Exploratory zu Exhibitive!

### Die 3 Brief-Typen:

1. **Exploratory** (Erkundend) - Daten verstehen
   - Beispiel: Heart Disease Analyse (Gruppe 4)
   - Woche 1, Tag 3

2. **Explanatory** (Erklärend) - Erkenntnisse kommunizieren
   - Beispiel: Temperatur-Vergleiche (Gruppen 1-3)
   - Woche 1, Tag 4-5

3. **Exhibitive** (Ausstellend) - Story erzählen ⭐ **KURSZIEL!**
   - Beispiel: Finale Projekt-Präsentationen
   - Woche 2, Tag 5-7

**Siehe:** `docs/plot_types_and_briefs.md` für vollständige Tabelle

---

## 📚 Weitere Ressourcen

- **Vollständiger Kurs:** `optional/advanced-uni-level/COURSE_STRUCTURE.md`
- **Migration Guide:** `MIGRATION_GUIDE.md`
- **Notebook-Splitting Tool:** `NOTEBOOK_SPLITTING_GUIDE.md`
- **Fortgeschritten:** `advanced-content/`

---

## 🛠 Tools

- **`split_notebook.py`** - Große Notebooks automatisch aufteilen (H1/H2 Support)
- **`forms_to_csv_adapter.py`** - Microsoft Forms → CSV (im Root)

---

*Sprachniveau: B1 (Deutsch)*  
*Kursdauer: 2 Wochen (10 Werktage)*  
*Letzte Aktualisierung: April 2026*