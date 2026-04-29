# ✅ Checkliste: Was ist ein guter Plot?

## 🎯 Überblick

Diese Checkliste hilft dir, deine Diagramme zu bewerten und zu verbessern.

---

## 📋 Die Checkliste

### 1. Inhalt & Daten ✅

- [ ] **Sind die Daten korrekt?**
  - Keine Fehler beim Laden
  - Richtige Spalten verwendet
  - Keine fehlenden Werte (oder erklärt)

- [ ] **Ist der Plot-Typ passend?**
  - Line Chart für Zeitreihen
  - Scatter Plot für Zusammenhänge
  - Bar Chart für Vergleiche

- [ ] **Beantwortet der Plot eine Frage?**
  - Welche Frage?
  - Ist die Antwort klar erkennbar?

---

### 2. Beschriftungen 🏷️

- [ ] **Hat der Plot einen Titel?**
  - Ist der Titel aussagekräftig?
  - Versteht man sofort, worum es geht?
  - Beispiel: ❌ "Plot" → ✅ "Temperatur in Hannover (April 2026)"

- [ ] **Ist die X-Achse beschriftet?**
  - Mit Einheit (falls nötig)
  - Beispiel: "Datum", "Alter (Jahre)", "Kilometer"

- [ ] **Ist die Y-Achse beschriftet?**
  - Mit Einheit (falls nötig)
  - Beispiel: "Temperatur (°C)", "Preis (€)", "Anzahl"

- [ ] **Gibt es eine Legende?** (falls mehrere Linien/Gruppen)
  - Sind die Labels klar?
  - Ist die Legende gut platziert?

---

### 3. Farben & Styling 🎨

- [ ] **Sind die Farben gut sichtbar?**
  - Nicht zu hell, nicht zu dunkel
  - Guter Kontrast zum Hintergrund

- [ ] **Sind die Farben sinnvoll?**
  - Rot für "hoch/warm/gefährlich"
  - Blau für "niedrig/kalt/sicher"
  - Nicht zu viele verschiedene Farben (max. 5)

- [ ] **Ist die Linienstärke passend?**
  - Nicht zu dünn (schwer zu sehen)
  - Nicht zu dick (überladen)
  - Standard: `linewidth=2`

- [ ] **Sind Marker hilfreich?**
  - Bei wenigen Datenpunkten: Ja (`marker='o'`)
  - Bei vielen Datenpunkten: Nein (zu voll)

---

### 4. Lesbarkeit 👓

- [ ] **Ist das Gitter aktiviert?**
  - `plt.grid(True)` macht es leichter, Werte abzulesen
  - Aber: Nicht zu dominant

- [ ] **Sind die Achsen-Bereiche sinnvoll?**
  - Nicht zu viel Leerraum
  - Nicht abgeschnitten
  - Falls nötig: `plt.xlim()` und `plt.ylim()` verwenden

- [ ] **Ist die Schriftgröße gut?**
  - Titel: Größer als der Rest
  - Achsenbeschriftungen: Gut lesbar
  - Falls nötig: `fontsize=12` verwenden

- [ ] **Überlappen sich Elemente?**
  - Labels nicht überlappend
  - Legende nicht über Daten
  - Falls nötig: `plt.tight_layout()` verwenden

---

### 5. Story & Kontext 📖

- [ ] **Erzählt der Plot eine Geschichte?**
  - Was ist die Hauptaussage?
  - Ist sie sofort erkennbar?

- [ ] **Sind wichtige Punkte hervorgehoben?**
  - Maximum/Minimum markiert?
  - Besondere Ereignisse annotiert?
  - Beispiel: `plt.axvline()` für wichtige Daten

- [ ] **Gibt es unnötige Elemente?**
  - Weniger ist mehr!
  - Entferne alles, was nicht zur Story beiträgt

---

## 🚫 Häufige Fehler

### ❌ Fehler 1: Keine Beschriftungen
```python
# SCHLECHT
plt.plot(x, y)
plt.show()
```

```python
# GUT
plt.plot(x, y)
plt.title("Temperatur in Hannover")
plt.xlabel("Datum")
plt.ylabel("Temperatur (°C)")
plt.show()
```

---

### ❌ Fehler 2: Zu viele Farben
```python
# SCHLECHT - 10 verschiedene Farben!
colors = ['red', 'blue', 'green', 'yellow', 'purple', 
          'orange', 'pink', 'brown', 'gray', 'cyan']
```

```python
# GUT - Maximal 3-5 Farben
colors = ['blue', 'red', 'green']
```

---

### ❌ Fehler 3: Unleserliche Achsen
```python
# SCHLECHT - Daten überlappen
plt.plot(df['datum'], df['temperatur'])
# Datum-Labels überlappen sich!
```

```python
# GUT - Datum rotieren
plt.plot(df['datum'], df['temperatur'])
plt.xticks(rotation=45)
plt.tight_layout()
```

---

### ❌ Fehler 4: Keine Story
```python
# SCHLECHT - Was soll ich sehen?
plt.plot(x, y)
plt.title("Daten")
```

```python
# GUT - Klare Aussage
plt.plot(x, y)
plt.title("Temperatur steigt im April um 10°C")
plt.axhline(y=20, color='red', linestyle='--', label='Durchschnitt')
```

---

## 🎯 Bewertungs-System

### Punkte vergeben:

**Beschriftungen (0-3 Punkte):**
- 0 = Keine Beschriftungen
- 1 = Nur Titel
- 2 = Titel + Achsen
- 3 = Titel + Achsen + Legende

**Farben & Styling (0-3 Punkte):**
- 0 = Standard (schwarz)
- 1 = Eine Farbe gewählt
- 2 = Mehrere Farben, sinnvoll
- 3 = Farben + Linientypen + Marker

**Lesbarkeit (0-2 Punkte):**
- 0 = Schwer zu lesen
- 1 = Gitter aktiviert
- 2 = Gitter + gute Achsen-Bereiche

**Story (0-2 Punkte):**
- 0 = Keine klare Aussage
- 1 = Aussage erkennbar
- 2 = Aussage + Highlights

**Gesamt: 0-10 Punkte**
- 0-3: Noch viel zu tun
- 4-6: Guter Anfang
- 7-8: Sehr gut!
- 9-10: Perfekt! 🎉

---

## 🚀 Nächste Schritte

1. **Nutze diese Checkliste** für jeden Plot
2. **Gehe langsam durch** (siehe `04_leitfaden_langsam.md`)
3. **Verbessere Schritt für Schritt**
4. **Frage dich:** "Würde ich diesen Plot verstehen, wenn ich ihn zum ersten Mal sehe?"

---

## 📚 Siehe auch

- **Langsamer Leitfaden:** `04_leitfaden_langsam.md` (10 Min pro Schritt)
- **Parameter-Referenz:** `woche-2/04_matplotlib_parameter.md`
- **Story-Framework:** `woche-2/05_story_framework.md`

---

*Nutze diese Checkliste bei jedem Plot!* ✅