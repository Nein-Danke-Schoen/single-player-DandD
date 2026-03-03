#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import yaml
from pathlib import Path
import random
import sys
from typing import Optional
from dataclasses import dataclass

held = charakter()

# -------------------------------------------------
# Menuvariabeln anlegen und verwalten
einstellungen_anzeigen = True

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
        if self.bewaehlte_waffe:
            dmg += self.gewaelte_waffe.dmg
        if self.bewaehltes_item:
            dmg += self.gewaeltes_item.dmg
        return dmg

    @property
    def gesmt_hp(self) -> int:
        """Gibt das Gesamtleben mit Item zurück"""
        total = self.hp
        if self.gewaeltes_item:
            hp += gewaeltes_item.hp
        return total

    def ruestet_waffe(self, waffe: Waffen) -> None:
        """Rüstet die übergebene Waffe aus."""
        self.gewaelte_waffe = waffe

    def ruestet_item(self, item: Items) -> None:
        """Rüstet das übergebene Item aus"""
        self.gewaeltes_item = item

# -------------------------------------------------
# Waffeninstanzen anlegen
rostigeseisenschwert    = Waffen(dmg=5, name="Rostiges Eisenschwert")
eisenschwert            = Waffen(dmg=10, name="Eisenschwert")
stahlschwert            = Waffen(dmg=15, name="Stahlschwert")
himmelschwert           = Waffen(dmg=20, name="Himmelschwert")

# -------------------------------------------------
# Iteminstanzen anlegen
ringdesschadens = Items(name="Ring des Schadens", dmg=0, hp=20)
ringdeslebens = Items(name="Ring des Lebens", dmg=50, hp=0)
thering = Items(name="Der Ring", dmg=50, hp=20)

# -------------------------------------------------
# NPC-Dialoge einlesen und weitergeben
def yamlopen():
    """ YAML Datei wird eingelesen und Variable loaded weitergegeben"""
    try:
        with open (Path(__file__).parent / "Assets" / "NPCdialoge.yaml") as datei:
            loaded = (yaml.safe_load(datei))
        if loaded:
            return(loaded)
    except Exception:
        print(Exception)
        sys.exit(1)
""" Beispiel zur ausgabe eines bestimmten Dialoges:
    textausgabe = yamlopen()
    text = textausgabe.get(".....")  #hier einfügen welchen textblock man will
    print(text)
"""

# -------------------------------------------------
# NPC-Charaktere
# Alter Mann 
menualtermannstatus1 = {
    "1": {"text": "Erzähle mir mehr über diesen Ort",   "active": True},
    "2": {"text": "Gib mir ein Schwert",                "active": True},
    "3": {"text": "Nichts, ich gehe schon",             "active": True},
}

def altermannstatus1():
    lines = [f"{k}: {v['text']}" for k, v in menualtermannstatus1.items() if v["active"]]
    return "\n".join(lines) + "\n> "

def altermannmenu1(key: str):
     if key in menualtermannstatus1:
        menualtermannstatus1[key]["active"] = False

def alterMann(status):
    #Startet einen Dialog mit dem alten Mann jenachdem wo man sich befindet(Status)
    if status == 1:
        print("Der alte Mann schaut dich an...\nMhh ein Neuer, sieht man selten. Was willst du?")
        textausgabe = yamlopen()
        while any(v["active"] for v in menualtermannstatus1.values()):
            choice = input(altermannstatus1()).strip()
            geschick = random.randint(1, 20)
            print(f"Du Rollst eine {geschick}")
            if choice not in menualtermannstatus1 or not menualtermannstatus1[choice]["active"]:
                print("Bitte wähle eine gültige, aktive Nummer.")
                continue
            if choice == "1":
                altermannmenu1("1")
                try:
                    if geschick <= 5:
                        print(textausgabe.get("altermannstart1schlecht"))
                    elif geschick >= 5 and geschick <= 15:
                        print(textausgabe.get("altermannstart1mittel"))
                    else:
                        print(textausgabe.get("altermannstart1gut"))
                except Exception as e:
                    print(e)
                    continue
                return alterMann(1)
            elif choice == "2":
                altermannmenu1("2")
                try:
                    if geschick <= 5:
                        print(textausgabe.get("altermannstart2schlecht"))
                    elif geschick >= 5 and geschick <= 15:
                        print(textausgabe.get("altermannstart2mittel"))
                        held.ruestet_waffe(rostigeseisenschwert)
                    else:
                        print(textausgabe.get("altermannstart2gut"))
                        held.ruestet_waffe(eisenschwert)
                except Exception as e:
                    print(e)
                return alterMann(1)
            elif choice == "3":
                altermannmenu1("3")
                if geschick <=5:
                    print(textausgabe.get("altermannstart3schlecht"))
                elif geschick >= 5 and geschick <= 15:
                    print(textausgabe.get("altermannstart3mittel"))
                else:
                    print(textausgabe.get("altermannstart3gut"))
                    try:
                        user_wahl = input("Möchtest du bei den zwei gestalten vorbeischauen? (j/n): ").strip().lower()
                        if user_wahl == "j":
                            print("Du gehst zu den beiden Gestalten hinüber...")
                            return gestalten(2)
                        else:
                            print("Du entfernst dich vom alten Mann und richtest deine Augen auf die Tür die in Das Anwesen hineinführt.")
                            return startraum()
                    except Exception as e:
                        print(e)
        print("Ich habe dir nichts zu sagen oder zu geben")
    else:
        print("Du solltest noch gar nicht hier sein (besser: der Teil wurde noch nicht gemacht :3)...\nWie hast du das gemacht?\nAber naja, zurück mit dir in den Startraum!")
        return startraum()

def menu_bauen():
    start_menu = ["Start", "Beenden"]
    if einstellungen_anzeigen:
        items.insert(1, "Einstellungen")
    return "\n".join(items) + "\n"

def startdialog():
    print("Willkommen zu dieser kleinen D&D Kampagne.") 
    while True:
        menu_text = start_menu
        user_input = input(menu_text).strip().lower()
        try:
            if user_input == "start":
                startraum()
                break
            elif user_input == "einstellungen":
                print("Zurzeit nicht vorhanden...\nKommt bestimmt irgendwann\n\n")
                einstellungen_anzeigen = False
            elif user_input == "beenden":
                print("Spiel wird beendet...")
                break
            else:
                print("Bitte eine valide Eingaben geben!!\n")
        except Exception as e:
            print(f"Ein Fehler ist Aufgetreten:\n{e}")

def startraum():
    print("""Du betrittst einen kleinen Raum. Er sieht heruntergekommen aus, in ihm siehst du zwei Tische. An dem linken sitzen zwei mürrisch aussehende Gestalten,
an dem rechten sitzt ein alte Mann. Am ende des Raumes befindet sich eine Holztür""")
    while True:
        try:
            user_wahl = input("Was willst du tun?\nZum alten Mann gehen: 1\nZu den zwei Gestalten gehen: 2\nDurch die Türe gehen: 3\n").strip()
            if user_wahl == "1":
                print("Du gehst zum alten Mann...")
                status = 1
                return alterMann(status)
            elif user_wahl == "2":
                print("Du gehst zu den zwei Gestalten...")
                return gestalten(start)
            else:
                print("Du gehst zur Türe und öffnest sie...")
                return raum2()
        except ValueError:
            print("Bitte eine valide Zahl eingeben!!!")

def main():
    startdialog()

if __name__ == "__main__":
    main()