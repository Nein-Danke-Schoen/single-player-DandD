### Aufgabe: **Ein einfaches Text‑Adventure**

Schreibe ein kleines Konsolen‑Programm, das ein interaktives Text‑Adventure simuliert. Der Spieler befindet sich in einem Labyrinth aus Räumen, kann sich bewegen, Gegenstände aufnehmen und einfache Rätsel lösen.

#### Anforderungen (ohne Plattform‑Abhängigkeiten)

1. **Raum‑Modell**
    
    - Jeder Raum hat einen Namen, eine Beschreibung und Verbindungen zu benachbarten Räumen (Norden, Süden, Osten, Westen).
    - Mindestens fünf verschiedene Räume sollen vorhanden sein, wobei mindestens ein Zyklus im Layout existiert (z. B. Raum A → Raum B → Raum C → Raum A).
2. **Spieler‑Status**
    
    - Der Spieler hat ein Inventar (Liste von Gegenständen).
    - Der aktuelle Standort wird gespeichert.
3. **Interaktion**
    
    - Befehle über die Konsole eingeben (z. B. `go north`, `take key`, `inventory`).
    - Das Programm soll Eingaben parsen, Fehlermeldungen bei ungültigen Befehlen ausgeben und den Spielzustand aktualisieren.
4. **Rätsel / Ziel**
    
    - Implementiere mindestens ein einfaches Rätsel (z. B. ein verschlossener Raum, der nur mit einem bestimmten Gegenstand geöffnet werden kann).
    - Das Spiel endet, wenn der Spieler das Ziel erreicht (z. B. ein „Schatz“-Raum).
5. **Robustheit**
    
    - Das Programm muss auf falsche Eingaben (Rechtschreibfehler, unbekannte Richtungen) reagieren, ohne abzustürzen.
    - Verwende klare Fehlermeldungen und zeige ggf. die aktuelle Raum­beschreibung erneut an.