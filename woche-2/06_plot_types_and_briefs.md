# 📊 Plot-Typen und Briefs - Übersicht

## 🎯 Die 3 Brief-Typen

### 1. **Exploratory** (Erkundend)
**Ziel:** Daten verstehen, Muster finden, Hypothesen entwickeln
**Für:** Datenanalysten, Forscher, eigene Analyse
**Beispiel im Kurs:** Heart Disease Analyse (Gruppe 4)

### 2. **Explanatory** (Erklärend)
**Ziel:** Erkenntnisse kommunizieren, Zusammenhänge zeigen
**Für:** Präsentationen, Berichte, Stakeholder
**Beispiel im Kurs:** Temperatur-Vergleiche (Gruppen 1-3)

### 3. **Exhibitive** (Ausstellend)
**Ziel:** Beeindrucken, Aufmerksamkeit erregen, Story erzählen
**Für:** Öffentlichkeit, Marketing, Storytelling
**Beispiel im Kurs:** Finale Projekt-Präsentationen (Kursziel!)

---

## 📋 Plot-Typen Tabelle

| Plot-Typ | Brief-Typ | Verwendung | Kurs-Beispiel | Wann nutzen? |
|----------|-----------|------------|---------------|--------------|
| **Scatter Plot** | Exploratory | Zusammenhänge finden | Heart Disease (Alter vs. Cholesterin) | Wenn du Korrelationen suchst |
| **Line Chart** | Explanatory | Trends zeigen | Temperatur Hannover über Zeit | Wenn du Entwicklung zeigst |
| **Bar Chart** | Explanatory | Vergleiche zeigen | Verkäufe pro Monat | Wenn du Kategorien vergleichst |
| **Histogram** | Exploratory | Verteilung verstehen | Altersverteilung Patienten | Wenn du Häufigkeiten suchst |
| **Box Plot** | Exploratory | Statistiken vergleichen | Cholesterin-Werte nach Gruppe | Wenn du Ausreißer findest |
| **Heatmap** | Exploratory | Muster in Daten | Korrelations-Matrix | Wenn du viele Variablen hast |
| **Pie Chart** | Explanatory | Anteile zeigen | Marktanteile | Wenn du Prozente zeigst (max 5-7 Teile!) |
| **Area Chart** | Explanatory | Mengen über Zeit | Umsatz-Entwicklung | Wenn du Volumen zeigst |
| **Violin Plot** | Exploratory | Verteilung detailliert | Temperatur-Verteilung | Wenn du mehr als Boxplot brauchst |
| **Slope Chart** | Exhibitive | Veränderung dramatisch | Vorher/Nachher Vergleich | Wenn du Wandel zeigst |
| **Dumbbell Chart** | Exhibitive | Unterschiede betonen | Gehaltsunterschiede M/F | Wenn du Gaps zeigst |
| **Annotated Chart** | Exhibitive | Story erzählen | Temperatur mit Ereignissen | Wenn du Kontext gibst |
| **Small Multiples** | Explanatory | Viele Vergleiche | Temperatur alle Städte | Wenn du Muster über Gruppen zeigst |
| **Stacked Bar** | Explanatory | Teile vom Ganzen | Verkäufe nach Produkt & Region | Wenn du Zusammensetzung zeigst |
| **Grouped Bar** | Explanatory | Kategorien vergleichen | Verkäufe Q1 vs Q2 | Wenn du Gruppen vergleichst |

---

## 🎓 Für den Kurs: Welcher Plot für welche Gruppe?

### Gruppe 1-2: Temperatur-Vergleich (Städte)
- **Plot:** Line Chart (2 Linien)
- **Brief:** Explanatory
- **Warum:** Zeigt klaren Vergleich über Zeit

### Gruppe 3: Zwei Messreihen
- **Plot:** Line Chart oder Area Chart
- **Brief:** Explanatory
- **Warum:** Zeigt Unterschiede deutlich

### Gruppe 4: Heart Disease (Scatter)
- **Plot:** Scatter Plot
- **Brief:** Exploratory
- **Warum:** Sucht nach Zusammenhängen

### Gruppe 5: Temperatur-Auffälligkeiten
- **Plot:** Annotated Line Chart
- **Brief:** Exhibitive
- **Warum:** Erzählt eine Story (Kälteeinbruch!)

---

## 🚀 Progression im Kurs

### Woche 1: Exploratory → Explanatory
1. **Tag 1-2:** Basis-Plots lernen (Line, Scatter, Bar)
2. **Tag 3:** Exploratory Analyse (Gruppenarbeit)
3. **Tag 4-5:** Explanatory Plots verbessern

### Woche 2: Explanatory → Exhibitive
4. **Tag 6:** Story-Framework lernen
5. **Tag 7:** Daten sammeln
6. **Projekt:** Exhibitive Präsentation erstellen ⭐

**Kursziel:** Von Exploratory zu Exhibitive!

---

## 📖 Detaillierte Beschreibungen

### Exploratory Plots

#### Scatter Plot
```python
plt.scatter(df['age'], df['cholesterol'])
plt.xlabel('Alter')
plt.ylabel('Cholesterin')
plt.title('Zusammenhang Alter-Cholesterin')
```
**Gut für:** Korrelationen finden, Ausreißer entdecken
**Nicht gut für:** Präsentationen (zu "roh")

#### Histogram
```python
plt.hist(df['age'], bins=20)
plt.xlabel('Alter')
plt.ylabel('Häufigkeit')
plt.title('Altersverteilung')
```
**Gut für:** Verteilung verstehen, Normalverteilung prüfen
**Nicht gut für:** Genaue Werte ablesen

#### Box Plot
```python
df.boxplot(column='cholesterol', by='heart_disease')
plt.ylabel('Cholesterin')
plt.title('Cholesterin nach Herzerkrankung')
```
**Gut für:** Median, Quartile, Ausreißer sehen
**Nicht gut für:** Genaue Verteilungsform

---

### Explanatory Plots

#### Line Chart
```python
plt.plot(df['datum'], df['temperatur'], color='teal', linewidth=2)
plt.xlabel('Datum')
plt.ylabel('Temperatur (°C)')
plt.title('Temperatur in Hannover im Mai')
plt.grid(True, alpha=0.3)
```
**Gut für:** Trends zeigen, Entwicklung über Zeit
**Nicht gut für:** Viele Linien (max 3-4)

#### Bar Chart
```python
plt.bar(df['monat'], df['verkäufe'], color='steelblue')
plt.xlabel('Monat')
plt.ylabel('Verkäufe (€)')
plt.title('Monatliche Verkäufe 2026')
```
**Gut für:** Kategorien vergleichen, Unterschiede zeigen
**Nicht gut für:** Zeitreihen (besser: Line Chart)

#### Grouped Bar Chart
```python
x = np.arange(len(categories))
width = 0.35
plt.bar(x - width/2, values1, width, label='2025')
plt.bar(x + width/2, values2, width, label='2026')
plt.xticks(x, categories)
plt.legend()
```
**Gut für:** Mehrere Gruppen vergleichen
**Nicht gut für:** Mehr als 3 Gruppen (zu voll)

---

### Exhibitive Plots

#### Annotated Line Chart
```python
fig, ax = plt.subplots(figsize=(12, 6))
ax.plot(df['datum'], df['temperatur'], color='teal', linewidth=2)

# Annotation für Ereignis
ax.annotate('Kälteeinbruch!', 
            xy=('2026-04-28', 8), 
            xytext=('2026-04-30', 12),
            arrowprops=dict(arrowstyle='->', color='red', lw=2),
            fontsize=12, color='red', fontweight='bold')

ax.set_title('Unerwarteter Kälteeinbruch Ende April', fontsize=16, fontweight='bold')
```
**Gut für:** Story erzählen, Ereignisse hervorheben
**Nicht gut für:** Schnelle Analyse

#### Slope Chart
```python
fig, ax = plt.subplots(figsize=(8, 6))
for i in range(len(df)):
    ax.plot([0, 1], [df.loc[i, 'vorher'], df.loc[i, 'nachher']], 
            marker='o', linewidth=2)
ax.set_xticks([0, 1])
ax.set_xticklabels(['Vorher', 'Nachher'])
ax.set_title('Dramatische Veränderung', fontsize=16, fontweight='bold')
```
**Gut für:** Vorher/Nachher zeigen, Wandel dramatisieren
**Nicht gut für:** Viele Datenpunkte

#### Dumbbell Chart
```python
for i in range(len(df)):
    ax.plot([df.loc[i, 'min'], df.loc[i, 'max']], [i, i], 
            marker='o', markersize=10, linewidth=2)
ax.set_yticks(range(len(df)))
ax.set_yticklabels(df['kategorie'])
ax.set_title('Unterschiede zwischen Min und Max', fontsize=16, fontweight='bold')
```
**Gut für:** Ranges zeigen, Gaps betonen
**Nicht gut für:** Genaue Werte

---

## ✅ Checkliste: Welchen Plot wähle ich?

### Schritt 1: Was ist mein Ziel?
- [ ] **Exploratory:** Ich will Daten verstehen → Scatter, Histogram, Box
- [ ] **Explanatory:** Ich will etwas erklären → Line, Bar, Grouped Bar
- [ ] **Exhibitive:** Ich will beeindrucken → Annotated, Slope, Dumbbell

### Schritt 2: Was sind meine Daten?
- [ ] **Zeit-Daten:** Line Chart, Area Chart
- [ ] **Kategorien:** Bar Chart, Grouped Bar
- [ ] **Zwei Variablen:** Scatter Plot
- [ ] **Verteilung:** Histogram, Box Plot, Violin Plot
- [ ] **Vergleich:** Bar Chart, Slope Chart, Dumbbell

### Schritt 3: Wer ist mein Publikum?
- [ ] **Ich selbst:** Exploratory (einfach, schnell)
- [ ] **Team/Chef:** Explanatory (klar, präzise)
- [ ] **Öffentlichkeit:** Exhibitive (schön, Story)

---

## 🎯 Kursziel: Exhibitive Plots

Am Ende des Kurses sollt ihr:
1. ✅ Exploratory Plots erstellen können (Daten verstehen)
2. ✅ Explanatory Plots erstellen können (Ergebnisse zeigen)
3. ✅ **Exhibitive Plots erstellen können** (Story erzählen) ⭐

**Das ist das Ziel!** 🎉

---

## 📚 Weitere Ressourcen

- **Storytelling:** `docs/storytelling_leitfaden_b1.md`
- **Plot-Checkliste:** `docs/checkliste_plot.md`
- **Kurs-Beispiele:** `PROJEKT_BESCHREIBUNG.md`

---

*Basierend auf: Data Visualization Workflow & Best Practices*  
*Sprachniveau: B1 (Deutsch)*  
*Letzte Aktualisierung: April 2026*