#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import yaml
from pathlib import Path
import random
import sys
from typing import Optional
from dataclasses import dataclass

@dataclass
class Waffen():
    """Definiert Waffen."""
    dmg: int
    name: str

@dataclass
class Items():
    """Definiert Gegenstände"""
    name: str
    hp: int
    dmg: int

@dataclass
class Charakter:
    """Definiert einen Charakter mit HP, Grundschaden und einer ausgerüsteten Waffe."""
    hp: int = 100
    grund_dmg: int = 5
    gewaelte_waffe: Optional[Waffen] = None
    gewaeltes_item: Optional[Items] = None

    @property 
    def dmg(self):
        """Gesamtschaden des Charakters, Grundschaden plus Waffenschaden und Itemschaden"""
        dmg = self.grund_dmg
        if self.gewaelte_waffe:
            dmg += self.gewaelte_waffe.dmg
        if self.gewaeltes_item:
            dmg += self.gewaeltes_item.dmg
        return dmg

    @property
    def gesamt_hp(self) -> int:
        """Gibt das Gesamtleben mit Item zurück"""
        total = self.hp
        if self.gewaeltes_item:
            hp += self.gewaeltes_item.hp
        return total

    def ruestet_waffe(self, waffe: Waffen) -> None:
        """Rüstet die übergebene Waffe aus."""
        self.gewaelte_waffe = waffe

    def ruestet_item(self, item: Items) -> None:
        """Rüstet das übergebene Item aus"""
        self.gewaeltes_item = item

# -------------------------------------------------
# Waffeninstanzen anlegen
rostigeseisenschwert    = Waffen(dmg=5,  name="Rostiges Eisenschwert")
eisenschwert            = Waffen(dmg=10, name="Eisenschwert")
stahlschwert            = Waffen(dmg=15, name="Stahlschwert")
himmelschwert           = Waffen(dmg=20, name="Himmelschwert")

# -------------------------------------------------
# Iteminstanzen anlegen
anfaengerring   = Items(name="Ring des Anfängers",  dmg=5,  hp=10)
silberring      = Items(name="Silberring",          dmg=10, hp=15)
ringdesschadens = Items(name="Ring des Schadens",   dmg=20, hp=0)
ringdeslebens   = Items(name="Ring des Lebens",     dmg=0,  hp=50)
thering         = Items(name="Der Ring",            dmg=50, hp=20)

# -------------------------------------------------
# NPC-Dialoge einlesen und weitergeben
# -------------------------------------------------
def yamlopen() -> dict:
    """ YAML Datei wird eingelesen und Variable loaded weitergegeben"""
    try:
        with open (Path(__file__).parent / "Assets" / "NPCdialoge.yaml") as datei:
            loaded = (yaml.safe_load(datei))
        if loaded:
            return loaded or {}
    except Exception as e:
        print(e)
        sys.exit(0)
# -------------------------------------------------
# NPC-Dialoge ausgeben
# -------------------------------------------------
def get_textblock(path: str, data: dict | None = None) -> str | None:
    """Sucht den Textblock gemäs dem Übergebenen Pfad"""
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

def textausgabe(textblock: str) -> str:
    """Gibt den gesuchten Textblock von gettextblock aus"""
    txt = get_textblock(textblock)
    if txt is not None:
        return txt
    else:
        print("Kein Text gefunden.", file=sys.stderr)

# -------------------------------------------------
# Menus bauen und aktivieren/deaktivieren
# -------------------------------------------------
def menu_builder(menuname):
    """Baut das jeweilige Menu dessen Namen übergeben wurde"""
    lines = [f"{k}: {v['text']}" for k, v in menuname.items() if v["active"]]
    return "\n".join(lines) + "\n> "

def menu_toggle(menuname, key: str):
    """Deaktiviert die jeweilige Option im Menu die Übergeben wurde"""
    if key in menuname:
        menuname[key]["active"] = False

# -------------------------------------------------
# NPC-Charaktere
# -------------------------------------------------

# Alter Mann 
menualtermannstatus1 = {
    "1": {"text": "Erzähle mir mehr über diesen Ort",   "active": True},
    "2": {"text": "Gib mir ein Schwert",                "active": True},
    "3": {"text": "Nichts, ich gehe schon",             "active": True},
}

def alterMann(status: int):
    #Startet einen Dialog mit dem alten Mann jenachdem wo man sich befindet(Status)
    if status == 1:
        print("Der alte Mann schaut dich an...\nMhh ein Neuer, sieht man selten. Was willst du?")
        while any(v["active"] for v in menualtermannstatus1.values()):
            choice = input(menu_builder(menualtermannstatus1)).strip()
            if choice not in menualtermannstatus1 or not menualtermannstatus1[choice]["active"]:
                print("Bitte wähle eine gültige, aktive Nummer.")
            if choice == "1":
                geschick = random.randint(1, 20)
                print(f"Du Rollst eine {geschick}")
                menu_toggle(menualtermannstatus1, "1")
                try:
                    if geschick <= 5:
                        print(textausgabe("AlterMann.Status_1.Auswahl_1.schlecht"))
                    elif geschick >= 5 and geschick <= 15:
                        print(textausgabe("AlterMann.Status_1.Auswahl_1.mittel"))
                    else:
                        print(textausgabe("AlterMann.Status_1.Auswahl_1.gut"))
                except Exception as e:
                    print(e)
            elif choice == "2":
                geschick = random.randint(1, 20)
                print(f"Du Rollst eine {geschick}")
                menu_toggle(menualtermannstatus1, "2")
                try:
                    if geschick <= 5:
                        print(textausgabe("AlterMann.Status_1.Auswahl_2.schlecht"))
                    elif geschick >= 5 and geschick <= 15:
                        print(textausgabe("AlterMann.Status_1.Auswahl_2.mittel"))
                        print("\nDu rüstest das rostige Eisenschwert aus...")
                        held.ruestet_waffe(rostigeseisenschwert)
                    else:
                        print(textausgabe("AlterMann.Status_1.Auswahl_2.gut"))
                        print("\nDu rüstest das Eisenschwert aus...")
                        held.ruestet_waffe(eisenschwert)
                except Exception as e:
                    print(e)
                    continue
            elif choice == "3":
                geschick = random.randint(1, 20)
                print(f"Du Rollst eine {geschick}")
                menu_toggle(menualtermannstatus1, "3")
                if geschick <=5:
                    print(textausgabe("AlterMann.Status_1.Auswahl_3.schlecht"))
                    return startraum(2)
                elif geschick >= 5 and geschick <= 15:
                    print(textausgabe("AlterMann.Status_1.Auswahl_3.mittel"))
                    return startraum(2)
                else:
                    print(textausgabe("AlterMann.Status_1.Auswahl_3.gut"))
                    try:
                        user_wahl = input("Möchtest du bei den zwei gestalten vorbeischauen? (j/n): ").strip().lower()
                        if user_wahl == "j":
                            print("Du gehst zu den beiden Gestalten hinüber...")
                            return zweigestalten(2)
                        else:
                            print("Du entfernst dich vom alten Mann und richtest deine Augen auf die Tür die in das Anwesen hineinführt.")
                            return startraum(2)
                    except Exception as e:
                        print(e)
                        continue
        print("Ich habe dir nichts zu sagen oder zu geben")
        return startraum(2)
    else:
        print("Du solltest noch gar nicht hier sein (besser: der Teil wurde noch nicht gemacht :3)...\nWie hast du das gemacht?\nAber naja, zurück mit dir in den Startraum!")
        return startraum(2)

# Zwei Gestalten
menuzweigestaltenstatus2  = {
    "1": {"text": "Wer seid ihr zwei?",                         "active": True},
    "2": {"text": "Könntet ihr mich eventuell unterstützen",    "active": True},
}

def zweigestalten(status: int):
    """Startet einen Dialog basierend darauf wo man gerade ist(Status)"""
    if status == 1:
        print("Du verziest dich besser...\nWenn nicht wird dir es gleich nicht mehr so gut gehen.\n\nDu entfernst du langsam wieder.")
        return startraum(2)
    elif status == 2:
        print("Mmmhhh, der alte mag dich wohl...\n'Was willst du?")
        user_wahl = input(menu_builder(menuzweigestaltenstatus2)).strip()
        while any(v["active"] for v in menuzweigestaltenstatus2.values()):
            if user_wahl == "1":
                menu_toggle(menuzweigestaltenstatus2, "1")
                geschick = random.randint(1, 20)
                print(f"Du rollst eine {geschick}")
                if geschick <= 5:
                    print(textausgabe("ZweiGestalten.Status_2.Auswahl_1.schlecht"))
                    print("\nDu entfernst dich wieder")
                    return startraum(2)
                elif geschick >5 and geschick <= 15:
                    print(textausgabe("ZweiGestalten.Status_2.Auswahl_1.mittel"))
                else:
                    print(textausgabe("ZweiGestalten.Status_2.Auswahl_1.gut"))
            elif user_wahl == "2":
                geschick = random.randint(1, 20)
                print(f"Du rollst eine {geschick}")
                menu_toggle(menuzweigestaltenstatus2, "2")
                if geschick <= 5:
                    print(textausgabe("ZweiGestalten.Status_2.Auswahl_2.schlecht"))
                elif geschick >5 and geschick <= 15:
                    print(textausgabe("ZweiGestalten.Status_2.Auswahl_2.mittel"))
                    held.ruestet_item(anfaengerring)
                    print("Du rüstest den Anfängerring aus...")
                else:
                    print(textausgabe("ZweiGestalten.Status_2.Auswahl_2.gut"))
                    held.ruestet_item(silberring)
                    print("Du rüstest den Silberring aus...")
                    continue
            else:
                print("Bitte eine valide Eingabe machen!!")
                return zweigestalten(2)
        print("Wir denken du solltest nun durch die Tür da gehen um deine Reise zu beginnen...")
        return startraum(2)
    else:
        print("Platzhalter")
        return startraum(2)       

einstellungen_anzeigen = True
startmenu = {
    "1":    {"text": "Start",           "active": True},
    "2":    {"text": "Einstellungen",   "active": True},
    "3":    {"text": "Beenden",         "active": True}
}

def startdialog():
    print("Willkommen zu dieser kleinen D&D Kampagne.") 
    while any(v["active"] for v in startmenu.values()):
        user_input = input(menu_builder(startmenu)).strip()
        try:
            if user_input == "1":
                status = 1
                startraum(status=1)
            elif user_input == "2":
                print("Zurzeit nicht vorhanden...\nKommt bestimmt irgendwann\n\n")
                menu_toggle(startmenu, "2")
            elif user_input == "3":
                print("Spiel wird beendet...")
                sys.exit(0)
            else:
                print("Bitte eine valide Eingaben geben!!\n")
        except Exception as e:
            print(f"Ein Fehler ist Aufgetreten:\n{e}")

startraummenu = {
    "0": {"text": "Was willst du tun?",                 "active": True},
    "1": {"text": "Zum alten Mann gehen",               "active": True},
    "2": {"text": "Zu den zwei Gestalten gehen",        "active": True},
    "3": {"text": "Durch die Türe gehen",               "active": True},
}

def startraum(status: int):
    if status == 1:
        print("""Du betrittst einen kleinen Raum. Er sieht heruntergekommen aus, in ihm siehst du zwei Tische. An dem linken sitzen zwei mürrisch aussehende Gestalten,\nan dem rechten sitzt ein alter Mann. Am ende des Raumes befindet sich eine Holztür\n\n""")
    while any(v["active"] for v in startraummenu.values()):
        try:
            user_wahl = input(menu_builder(startraummenu)).strip()
            if user_wahl == "1":
                print("Du gehst zum alten Mann...")
                return alterMann(1)
            elif user_wahl == "2":
                menu_toggle(startraummenu, "2")
                print("Du gehst zu den zwei Gestalten...")
                return zweigestalten(1)
            elif user_wahl == "3":
                print("Du gehst zur Türe und öffnest sie...")
                return raum2()
            elif user_wahl == "0":
                print("Nett gedacht, aber keine valide Eingabe, bitte nur 1-3 verwenden")
        except Exception as e:
            print(e)

def raum2():
    print("platzhalter")

def main():
    global held 
    held = Charakter()
    startdialog()

if __name__ == "__main__":
    main()