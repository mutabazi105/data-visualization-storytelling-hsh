# 📝 Tag 7: Manuelle Datenerfassung mit JSON

## 🎯 Was machen wir heute?

Heute lernen wir, wie man **Daten manuell aufschreibt** - ohne Excel, ohne Forms, einfach mit einem Text-Editor!

---

## 🤔 Was ist JSON?

**JSON** = **J**ava**S**cript **O**bject **N**otation

Das klingt kompliziert, aber es ist eigentlich ganz einfach:

**JSON ist wie eine Einkaufsliste!**

### Beispiel: Einkaufsliste

```json
{
  "produkt": "Milch",
  "preis": 1.29,
  "menge": 2
}
```

Das ist alles! 🎉

---

## 📖 JSON Grundlagen

### Struktur

JSON hat immer diese Form:
```json
{
  "schlüssel": "wert",
  "anderer_schlüssel": 123,
  "noch_ein_schlüssel": true
}
```

### Regeln

1. **Geschweifte Klammern** `{ }` am Anfang und Ende
2. **Anführungszeichen** `" "` um Schlüssel und Text-Werte
3. **Doppelpunkt** `:` zwischen Schlüssel und Wert
4. **Komma** `,` zwischen Einträgen (aber NICHT nach dem letzten!)

---

## 💡 Beispiele

### Beispiel 1: Tägliche Stimmung

```json
{
  "tag": "Montag",
  "datum": "2026-04-28",
  "stimmung": 8,
  "kaffee_getrunken": 3,
  "stunden_geschlafen": 7.5,
  "wetter": "sonnig"
}
```

### Beispiel 2: Lernzeit

```json
{
  "datum": "2026-04-28",
  "fach": "Data Visualization",
  "lernzeit_minuten": 120,
  "verstanden": true,
  "notizen": "Matplotlib ist cool!"
}
```

### Beispiel 3: Temperatur-Beobachtung

```json
{
  "stadt": "Hannover",
  "datum": "2026-05-01",
  "uhrzeit": "14:00",
  "temperatur_celsius": 18.5,
  "wetter": "bewölkt",
  "wind": "leicht"
}
```

---

## 📊 Mehrere Einträge: JSON Array

Wenn du mehrere Tage aufschreiben willst:

```json
[
  {
    "tag": "Montag",
    "stimmung": 8,
    "kaffee": 3
  },
  {
    "tag": "Dienstag",
    "stimmung": 7,
    "kaffee": 2
  },
  {
    "tag": "Mittwoch",
    "stimmung": 9,
    "kaffee": 4
  }
]
```

**Wichtig:** 
- Eckige Klammern `[ ]` für mehrere Einträge
- Komma zwischen den Einträgen
- KEIN Komma nach dem letzten Eintrag!

---

## ✍️ Deine Aufgabe

### Schritt 1: Wähle ein Thema (5 Min)

Was möchtest du beobachten?

**Ideen:**
- Deine tägliche Stimmung
- Wie viel Kaffee/Tee du trinkst
- Wie lange du lernst
- Wie viele Schritte du gehst
- Temperatur draußen
- Wie viele Stunden du schläfst

**Mein Thema:**
```
Ich beobachte: _______________________________________________
```

### Schritt 2: Erstelle deine JSON-Datei (10 Min)

1. Öffne einen Text-Editor (Notepad, TextEdit, VS Code)
2. Schreibe deine erste Beobachtung:

```json
{
  "datum": "2026-04-28",
  "meine_beobachtung": 123,
  "notiz": "Hier deine Notiz"
}
```

3. Speichere als `meine_daten.json`

### Schritt 3: Füge mehr Daten hinzu (15 Min)

Sammle Daten für **mindestens 5 Tage**:

```json
[
  {
    "datum": "2026-04-28",
    "wert": 10
  },
  {
    "datum": "2026-04-29",
    "wert": 12
  },
  {
    "datum": "2026-04-30",
    "wert": 11
  },
  {
    "datum": "2026-05-01",
    "wert": 15
  },
  {
    "datum": "2026-05-02",
    "wert": 13
  }
]
```

### Schritt 4: JSON in Python laden (10 Min)

```python
import json
import pandas as pd
import matplotlib.pyplot as plt

# JSON-Datei laden
with open('meine_daten.json', 'r', encoding='utf-8') as f:
    daten = json.load(f)

# In DataFrame umwandeln
df = pd.DataFrame(daten)

# Anschauen
print(df)
```

### Schritt 5: Plotten! (10 Min)

```python
# Plot erstellen
plt.figure(figsize=(10, 6))
plt.plot(df['datum'], df['wert'], 
         color='teal', 
         marker='o', 
         linewidth=2)

plt.title('Meine Beobachtungen über 5 Tage')
plt.xlabel('Datum')
plt.ylabel('Wert')
plt.xticks(rotation=45)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()
```

---

## ⚠️ Häufige Fehler

### Fehler 1: Komma vergessen
```json
{
  "tag": "Montag"
  "stimmung": 8  ← FEHLER! Komma fehlt!
}
```

**Richtig:**
```json
{
  "tag": "Montag",
  "stimmung": 8
}
```

### Fehler 2: Komma nach letztem Eintrag
```json
{
  "tag": "Montag",
  "stimmung": 8,  ← FEHLER! Letztes Komma!
}
```

**Richtig:**
```json
{
  "tag": "Montag",
  "stimmung": 8
}
```

### Fehler 3: Anführungszeichen vergessen
```json
{
  tag: "Montag"  ← FEHLER! Schlüssel braucht " "
}
```

**Richtig:**
```json
{
  "tag": "Montag"
}
```

---

## 🔍 JSON validieren

Bevor du deine JSON-Datei in Python lädst, prüfe sie:

**Online-Tool:** https://jsonlint.com/

1. Kopiere deinen JSON-Code
2. Füge ihn auf jsonlint.com ein
3. Klicke "Validate JSON"
4. Wenn grün ✅ → Alles gut!
5. Wenn rot ❌ → Fehler beheben

---

## 💡 Vorteile von JSON

### ✅ Vorteile:
- Einfach zu schreiben
- Kein Excel nötig
- Funktioniert überall
- Gut für unstrukturierte Daten
- Kann Notizen enthalten

### ❌ Nachteile:
- Fehleranfällig (Kommas, Anführungszeichen)
- Nicht gut für große Datenmengen
- Keine automatische Validierung

---

## 📚 Vollständiges Beispiel

### Datei: `stimmung_woche.json`

```json
[
  {
    "datum": "2026-04-28",
    "tag": "Montag",
    "stimmung": 7,
    "kaffee": 3,
    "lernzeit_minuten": 120,
    "notiz": "Guter Start in die Woche"
  },
  {
    "datum": "2026-04-29",
    "tag": "Dienstag",
    "stimmung": 8,
    "kaffee": 2,
    "lernzeit_minuten": 90,
    "notiz": "Matplotlib verstanden!"
  },
  {
    "datum": "2026-04-30",
    "tag": "Mittwoch",
    "stimmung": 6,
    "kaffee": 4,
    "lernzeit_minuten": 60,
    "notiz": "Müde heute"
  },
  {
    "datum": "2026-05-01",
    "tag": "Donnerstag",
    "stimmung": 9,
    "kaffee": 2,
    "lernzeit_minuten": 150,
    "notiz": "Gruppenarbeit war super!"
  },
  {
    "datum": "2026-05-02",
    "tag": "Freitag",
    "stimmung": 10,
    "kaffee": 1,
    "lernzeit_minuten": 180,
    "notiz": "Projekt fertig! 🎉"
  }
]
```

### Python-Code: `json_zu_plot.py`

```python
import json
import pandas as pd
import matplotlib.pyplot as plt

# JSON laden
with open('stimmung_woche.json', 'r', encoding='utf-8') as f:
    daten = json.load(f)

# DataFrame erstellen
df = pd.DataFrame(daten)

# Plot erstellen
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

# Plot 1: Stimmung
ax1.plot(df['tag'], df['stimmung'], 
         color='teal', marker='o', linewidth=2)
ax1.set_title('Meine Stimmung diese Woche', fontsize=14, fontweight='bold')
ax1.set_xlabel('Tag')
ax1.set_ylabel('Stimmung (1-10)')
ax1.grid(True, alpha=0.3)

# Plot 2: Kaffee vs. Lernzeit
ax2.scatter(df['kaffee'], df['lernzeit_minuten'], 
            color='coral', s=100, alpha=0.6)
ax2.set_title('Kaffee vs. Lernzeit', fontsize=14, fontweight='bold')
ax2.set_xlabel('Kaffee (Tassen)')
ax2.set_ylabel('Lernzeit (Minuten)')
ax2.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('meine_woche.png', dpi=300, bbox_inches='tight')
plt.show()

# Story
print("\n📖 Meine Story:")
print(f"Beste Stimmung: {df.loc[df['stimmung'].idxmax(), 'tag']} ({df['stimmung'].max()}/10)")
print(f"Meiste Lernzeit: {df.loc[df['lernzeit_minuten'].idxmax(), 'tag']} ({df['lernzeit_minuten'].max()} Min)")
print(f"Durchschnittlich: {df['kaffee'].mean():.1f} Tassen Kaffee pro Tag")
```

---

## 🎯 Deine Aufgabe für heute

1. **Erstelle** eine JSON-Datei mit deinen eigenen Daten (mindestens 5 Einträge)
2. **Validiere** sie auf jsonlint.com
3. **Lade** sie in Python
4. **Erstelle** einen Plot
5. **Erzähle** deine Story!

**Zeit:** 60 Minuten

---

## ✅ Checkliste

- [ ] JSON-Datei erstellt
- [ ] Mindestens 5 Einträge
- [ ] Auf jsonlint.com validiert (grün ✅)
- [ ] In Python geladen
- [ ] Plot erstellt
- [ ] Story aufgeschrieben

---

## 🎉 Fertig!

Du kannst jetzt:
- ✅ Daten manuell aufschreiben (JSON)
- ✅ JSON in Python laden
- ✅ Deine eigenen Beobachtungen visualisieren

**Das ist super nützlich für:**
- Persönliche Projekte
- Kleine Experimente
- Schnelle Notizen
- Unstrukturierte Daten

---

*Sprachniveau: B1 (Deutsch)*  
*Dauer: 60 Minuten*  
*Tool: JSON + Python*