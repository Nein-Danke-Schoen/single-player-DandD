import yaml
from pathlib import Path
import sys

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

# -------------------------------------------------
# NPC-Dialoge einlesen und weitergeben
# -------------------------------------------------
def yamlopen() -> dict:
    """ YAML Datei wird eingelesen und Variable loaded weitergegeben"""
    try:
        with open (Path(__file__).parent / "Assets" / "NPCdialoge.yaml") as datei:
            loaded = (yaml.safe_load(datei))
        if loaded:
            return loaded
    except Exception as e:
        print(e)
        sys.exit(1)
# -------------------------------------------------
# NPC-Dialoge ausgeben
# -------------------------------------------------
def get_textblock(path: str, data: dict | None = None) -> str | None:
    if data is None:
        data = yamlopen()
    keys = path.split(".")
    current = data
    for key in keys:
        if isinstance(current, dict) and key in current:
            current = current[key]
        else:
            print(f"Pfad '{path}' nicht gefunden (fehlender Schlüssel: '{key}').",file=sys.stderr,)
            return None
    if isinstance(current, str):
        return current.strip()
    else:
        print(f"Der Endwert von '{path}' ist kein Text, sondern ein {type(current).__name__}.",file=sys.stderr,)
        return None

def textausgabe(textblock: str) -> None:
    txt = get_textblock(textblock)
    if txt is not None:
        return txt
    else:
        print("Kein Text gefunden.", file=sys.stderr)

def test():
    print(textausgabe("AlterMann.Status_1.Auswahl_1.gut"))
test()