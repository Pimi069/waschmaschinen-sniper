# -*- coding: utf-8 -*-
import os

# Deine Nischendaten
keyword = "Waschmaschine Lager defekt: Kosten & Selber reparieren"
content = """
<p>Deine Waschmaschine macht beim Schleudern ohrenbetäubenden Lärm? Wahrscheinlich ein Lagerschaden.</p>
<h2>Was kostet die Reparatur?</h2>
<p>Ein Profi verlangt oft 300-500 Euro. Doch das Ersatzteil kostet meist weniger als 40 Euro.</p>
<h3>Die Lösung:</h3>
<p>Mit dem richtigen Reparatur-Set und etwas Geduld sparst du hunderte Euro.</p>
"""
affiliate_link = "https://www.amazon.de/s?k=waschmaschine+lager+reparatur+set" # Platzhalter

# HTML Skelett
html_template = f"""
<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{keyword}</title>
    <style>
        body {{ font-family: sans-serif; line-height: 1.6; max-width: 800px; margin: auto; padding: 20px; background: #f4f4f4; }}
        .card {{ background: white; padding: 20px; border-radius: 8px; box-shadow: 0 2px 5px rgba(0,0,0,0.1); }}
        .btn {{ display: inline-block; background: #e67e22; color: white; padding: 10px 20px; text-decoration: none; border-radius: 5px; }}
    </style>
</head>
<body>
    <div class="card">
        <h1>{keyword}</h1>
        {content}
        <a href="{affiliate_link}" class="btn">Passende Ersatzteile auf Amazon finden</a>
    </div>
</body>
</html>
"""

# Datei speichern
with open("index.html", "w", encoding="utf-8") as f:
    f.write(html_template)

print("Webseite 'index.html' wurde erstellt!")
