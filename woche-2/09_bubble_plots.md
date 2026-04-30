# 🫧 Bubble Plots (Blasendiagramme)

## Was ist ein Bubble Plot?

Ein **Bubble Plot** ist eine Erweiterung des Scatter Plots, der **drei Dimensionen** gleichzeitig zeigt:
- **X-Achse**: Erste Variable
- **Y-Achse**: Zweite Variable  
- **Bubble-Größe**: Dritte Variable

**Zusätzlich möglich:**
- **Farbe**: Vierte Variable (Kategorie oder Wert)
- **Transparenz**: Überlappungen sichtbar machen

---

## 📊 Wann nutze ich Bubble Plots?

### ✅ Gut für:
- **3-4 Variablen** gleichzeitig zeigen
- **Zusammenhänge** zwischen mehreren Dimensionen
- **Größenvergleiche** (z.B. Bevölkerung, Umsatz, Marktanteil)
- **Kategorien** durch Farbe unterscheiden

### ❌ Nicht gut für:
- **Genaue Werte** ablesen (schwierig bei Größen)
- **Viele Datenpunkte** (wird unübersichtlich)
- **Kleine Unterschiede** in der dritten Dimension
- **Zeitreihen** (besser: Line Chart)

---

## 🎯 Klassisches Beispiel: Gapminder

**Hans Rosling's berühmte Visualisierung:**
- **X-Achse**: GDP per Capita (Wohlstand)
- **Y-Achse**: Life Expectancy (Lebenserwartung)
- **Bubble-Größe**: Population (Bevölkerung)
- **Farbe**: Continent (Kontinent)

```python
import matplotlib.pyplot as plt
import numpy as np

# Beispiel-Daten (vereinfacht)
countries = ['Germany', 'USA', 'China', 'India', 'Brazil']
gdp = [48000, 65000, 10000, 2000, 9000]  # GDP per capita
life_exp = [81, 79, 77, 69, 75]  # Life expectancy
population = [83, 331, 1400, 1380, 212]  # in Millionen

# Bubble Plot erstellen
plt.figure(figsize=(10, 6))
plt.scatter(gdp, life_exp, s=population, alpha=0.6, 
            c=['blue', 'red', 'green', 'orange', 'yellow'],
            edgecolors='black', linewidth=1.5)

plt.xlabel('GDP per Capita ($)', fontsize=12)
plt.ylabel('Life Expectancy (years)', fontsize=12)
plt.title('Wealth, Health & Population by Country', fontsize=14, fontweight='bold')
plt.grid(True, alpha=0.3)

# Labels für Länder
for i, country in enumerate(countries):
    plt.annotate(country, (gdp[i], life_exp[i]), 
                fontsize=9, ha='center')

plt.tight_layout()
plt.show()
```

---

## 🔧 Technische Details

### Bubble-Größe berechnen

**Problem:** `s` Parameter in `plt.scatter()` ist die **Fläche**, nicht der Radius!

```python
# ❌ Falsch: Direkte Werte
plt.scatter(x, y, s=population)  # Zu große Unterschiede!

# ✅ Richtig: Skalieren
# Methode 1: Linear skalieren
min_size = 50
max_size = 1000
scaled_size = min_size + (population - min(population)) / (max(population) - min(population)) * (max_size - min_size)

# Methode 2: Proportional zur Fläche
# Wenn Wert = 100 → Fläche = 100
plt.scatter(x, y, s=values)

# Methode 3: Proportional zum Radius
# Wenn Wert = 10 → Radius = 10 → Fläche = π*10² = 314
plt.scatter(x, y, s=np.pi * (values ** 2))
```

### Farben für Kategorien

```python
# Kategorien definieren
categories = ['Europe', 'Asia', 'Americas', 'Asia', 'Americas']
colors = {'Europe': 'blue', 'Asia': 'red', 'Americas': 'green'}
bubble_colors = [colors[cat] for cat in categories]

plt.scatter(x, y, s=sizes, c=bubble_colors, alpha=0.6)
```

### Farben für kontinuierliche Werte

```python
# Vierte Dimension als Farbskala
fourth_dimension = [5, 8, 3, 9, 6]  # z.B. Temperatur

plt.scatter(x, y, s=sizes, c=fourth_dimension, 
            cmap='viridis', alpha=0.6)
plt.colorbar(label='Temperature (°C)')
```

---

## 📈 Praktisches Beispiel: Verkaufsdaten

```python
import matplotlib.pyplot as plt
import numpy as np

# Daten: Produkte analysieren
products = ['Laptop', 'Phone', 'Tablet', 'Watch', 'Headphones']
price = [1200, 800, 500, 400, 150]  # Preis in €
units_sold = [500, 2000, 1200, 800, 3000]  # Verkaufte Einheiten
revenue = [p * u for p, u in zip(price, units_sold)]  # Umsatz

# Kategorien
categories = ['Electronics', 'Electronics', 'Electronics', 'Wearables', 'Audio']
colors_map = {'Electronics': 'steelblue', 'Wearables': 'coral', 'Audio': 'mediumseagreen'}
colors = [colors_map[cat] for cat in categories]

# Bubble Plot
fig, ax = plt.subplots(figsize=(12, 7))

# Größe skalieren (Umsatz)
sizes = [r / 1000 for r in revenue]  # Skalierung für bessere Darstellung

scatter = ax.scatter(price, units_sold, s=sizes, c=colors, 
                     alpha=0.6, edgecolors='black', linewidth=2)

# Labels
for i, product in enumerate(products):
    ax.annotate(product, (price[i], units_sold[i]), 
                fontsize=10, ha='center', fontweight='bold')

# Achsen
ax.set_xlabel('Preis (€)', fontsize=12)
ax.set_ylabel('Verkaufte Einheiten', fontsize=12)
ax.set_title('Produkt-Performance: Preis vs. Verkäufe vs. Umsatz', 
             fontsize=14, fontweight='bold')
ax.grid(True, alpha=0.3)

# Legende für Kategorien
from matplotlib.patches import Patch
legend_elements = [Patch(facecolor=colors_map[cat], label=cat) 
                   for cat in colors_map.keys()]
ax.legend(handles=legend_elements, loc='upper right')

# Notiz für Bubble-Größe
ax.text(0.02, 0.98, 'Bubble-Größe = Umsatz', 
        transform=ax.transAxes, fontsize=10, 
        verticalalignment='top', style='italic',
        bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

plt.tight_layout()
plt.show()
```

**Was zeigt dieser Plot?**
- **Preis vs. Verkäufe**: Negative Korrelation (teurer = weniger verkauft)
- **Umsatz** (Bubble-Größe): Laptop hat hohen Umsatz trotz weniger Verkäufe
- **Kategorien** (Farbe): Unterschiedliche Produktgruppen

---

## ⚠️ Häufige Fehler

### 1. Zu viele Bubbles

```python
# ❌ Schlecht: 100+ Datenpunkte
plt.scatter(x_100, y_100, s=sizes_100)  # Chaos!

# ✅ Besser: Top 10-20 zeigen
top_20 = df.nlargest(20, 'revenue')
plt.scatter(top_20['x'], top_20['y'], s=top_20['size'])
```

### 2. Zu große Größenunterschiede

```python
# ❌ Schlecht: Extreme Werte
sizes = [10, 50, 5000]  # Kleinste Bubble unsichtbar!

# ✅ Besser: Logarithmische Skalierung
import numpy as np
sizes_log = np.log10(sizes) * 100
```

### 3. Überlappende Bubbles

```python
# ✅ Lösung 1: Transparenz
plt.scatter(x, y, s=sizes, alpha=0.5)  # Überlappungen sichtbar

# ✅ Lösung 2: Jitter (leichte Verschiebung)
x_jitter = x + np.random.normal(0, 0.1, len(x))
y_jitter = y + np.random.normal(0, 0.1, len(y))
plt.scatter(x_jitter, y_jitter, s=sizes, alpha=0.6)
```

### 4. Fehlende Legende für Größe

```python
# ✅ Größen-Legende hinzufügen
sizes_legend = [100, 500, 1000]  # Beispiel-Größen
labels_legend = ['Small', 'Medium', 'Large']

for size, label in zip(sizes_legend, labels_legend):
    plt.scatter([], [], s=size, c='gray', alpha=0.6, label=label)
plt.legend(title='Size', loc='upper left')
```

---

## 🎨 Design Best Practices

### 1. Farben sinnvoll nutzen

```python
# ✅ Kategorien: Unterschiedliche Farben
# ✅ Kontinuierlich: Farbskala (cmap)
# ❌ Zu viele Farben: Verwirrend!

# Beispiel: Colorblind-freundlich
import seaborn as sns
colors = sns.color_palette("colorblind", n_colors=3)
```

### 2. Größen lesbar machen

```python
# Regel: Kleinste Bubble sollte sichtbar sein (min 50)
#        Größte Bubble sollte nicht dominieren (max 1000)

min_size = 50
max_size = 1000
scaled = min_size + (values - values.min()) / (values.max() - values.min()) * (max_size - min_size)
```

### 3. Labels strategisch platzieren

```python
# Nur wichtige Bubbles labeln
top_5 = df.nlargest(5, 'revenue')
for idx in top_5.index:
    plt.annotate(df.loc[idx, 'name'], 
                (df.loc[idx, 'x'], df.loc[idx, 'y']),
                fontsize=10, fontweight='bold')
```

---

## 🔄 Bubble Plot vs. Scatter Plot

| Feature | Scatter Plot | Bubble Plot |
|---------|-------------|-------------|
| **Dimensionen** | 2 (X, Y) | 3-4 (X, Y, Size, Color) |
| **Komplexität** | Einfach | Mittel |
| **Verwendung** | Korrelation finden | Mehrere Variablen vergleichen |
| **Lesbarkeit** | Hoch | Mittel (bei zu vielen Bubbles niedrig) |
| **Best für** | Exploratory | Explanatory/Exhibitive |

---

## 📚 Weiterführende Ressourcen

### Online-Galerie
- **Python Graph Gallery**: https://python-graph-gallery.com/bubble-plot/
- **Matplotlib Examples**: https://matplotlib.org/stable/gallery/lines_bars_and_markers/scatter_demo2.html

### Inspiration
- **Gapminder**: https://www.gapminder.org/tools/
- **Hans Rosling TED Talk**: "The best stats you've ever seen"

### Code-Beispiele
```python
# Seaborn Alternative
import seaborn as sns
sns.scatterplot(data=df, x='x', y='y', size='size', 
                hue='category', sizes=(50, 1000), alpha=0.6)
```

---

## ✅ Checkliste: Guter Bubble Plot

Vor dem Veröffentlichen prüfen:

- [ ] **Nicht zu viele Bubbles** (max 20-30)
- [ ] **Größen skaliert** (kleinste sichtbar, größte nicht dominant)
- [ ] **Transparenz** bei Überlappungen (alpha=0.5-0.7)
- [ ] **Farben sinnvoll** (Kategorien oder Werteskala)
- [ ] **Legende vorhanden** (für Größe und Farbe)
- [ ] **Labels für wichtige Punkte**
- [ ] **Achsenbeschriftungen klar**
- [ ] **Titel beschreibt alle Dimensionen**

---

## 🎯 Zusammenfassung

**Bubble Plots sind perfekt, wenn du:**
- 3-4 Variablen gleichzeitig zeigen willst
- Größenvergleiche visualisieren möchtest
- Zusammenhänge zwischen mehreren Dimensionen suchst

**Aber Vorsicht:**
- Nicht für genaue Werte
- Nicht für viele Datenpunkte
- Größen müssen gut skaliert sein

> "A bubble plot is a scatter plot on steroids - use it wisely!"

---

*Basierend auf: Python Graph Gallery & Gapminder*  
*Sprachniveau: B1 (Deutsch)*  
*Letzte Aktualisierung: April 2026*