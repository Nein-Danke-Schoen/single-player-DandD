import yaml
from pathlib import Path

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


"""Wie man yaml dateien einliest und spezifische dinge zurückgibt"""
def yamlopen():
    # YAML wird geöffnet
    with open (Path(__file__).parent / "NPCdialoge.yaml") as datei:
        try:
            # YAML wird komplett eingelesen
            loaded = (yaml.safe_load(datei))
        except yaml.YAMLError as exception:
            print(exception)
    if loaded:
        #YAML wird durch return an die nächste funktion weitergegeben
        return(loaded)
def speziyaml():    
    textausgabe = yamlopen()
    text = textausgabe.get(".....")  #hier einfügen welchen textblock man will
    print(text)
