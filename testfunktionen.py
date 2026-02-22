"""Demonstriert das Ausrüsten einer Waffe und gibt die Werte aus."""
def test_waffen():    
    held = Charakter()                     # neue Charakter‑Instanz
    print(f"Grundschaden des Helden: {held.grund_dmg}")

    # 1️⃣ Eisenschwert ausrüsten
    print("Wir rüsten das Eisenschwert aus …")
    held.ruestet_waffe(eisenschwert)
    print(f"Gesamtschaden nach Ausrüstung: {held.dmg}\n")

    # 2️⃣ Stahlschwert wechseln (optional)
    print("Jetzt wechseln wir zu Stahlschwert …")
    held.ruestet_waffe(stahlschwert)
    print(f"Neuer Gesamtschaden: {held.dmg}")