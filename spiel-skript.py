#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import yaml
from pathlib import Path
import random
import sys
from typing import Optional

class Waffen():
    """Definiert Waffen."""
    def __init__(self, dmg: int, name: str):
        self.dmg = dmg
        self.name = name

class Charakter:
    """Definiert einen Charakter mit HP, Grundschaden und einer ausgerüsteten Waffe."""
    def __init__(self, hp: int = 100, grund_dmg: int = 5, gewaelte_waffe: Optional[Waffen] = None):
        self.hp = hp
        self.grund_dmg = grund_dmg
        self.gewaelte_waffe = gewaelte_waffe

    @property 
    def dmg(self):
        """Gesamtschaden des Charakters, Grundschaden plus Waffenschaden"""
        if self.gewaelte_waffe:
            return self.grund_dmg + self.gewaelte_waffe.dmg
        return self.grund_dmg

    def ruestet_waffe(self, waffe: Waffen) -> None:
        """Rüstet die übergebene Waffe aus."""
        self.gewaelte_waffe = waffe

# -------------------------------------------------
# Waffeninstanzen anlegen
eisenschwert   = Waffen(5,  "Eisenschwert")
stahlschwert   = Waffen(10, "Stahlschwert")
himmelschwert  = Waffen(20, "Himmelschwert")

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
def alterMann(status):
    #Startet einen Dialog mit dem alten Mann jenachdem wo man sich befindet(Status)
    if status == 1:
        print("Der alte Mann schaut dich an...\nMhh ein Neuer, sieht man selten. Was willst du?")
    while True:
        try:
            user_wahl = input("Erzäle mir mehr über diesen Ort: 1\nGib mir ein Schwert: 2\nNichts ich gehe schon: 3\n").strip().lower()
            geschick = random.randint(1, 20)
            if user_wahl == "1":
                textausgabe = yamlopen()
                print(f"Du Rollst eine {geschick}")
                try:
                    if geschick <= 5:
                        text = textausgabe.get("altermannstartschlecht")
                        print(text)
                        return startraum()
                    elif geschick >= 5 and geschick <= 15:
                        text = textausgabe.get("altermannstartmittel")
                        print(text)
                        return startraum()
                    else:
                        text = textausgabe.get("altermannstartgut")
                        print(text)
                        return startraum()
                except Exception as e:
                    print(e)
                    continue
        except Exception as e:
            print("Bitte eine Valide Eingabe machen!!!")
    else:
        return startraum()

def startdialog(): 
    print("Wilkommen zu dieser kleinen D&D Kampange.")
    while True:
        Menu = input(f"Start\nEinstellungen\nBeenden\n").strip().lower()
        try:
            if Menu == "start":
                startraum()
                break
            elif Menu == "einstellungen":
                print("Zurzeit nicht vorhanden...\nKommt bestimmt irgendwann\n\n")
                #return einstellungen()
            else:
                print("Spiel wird beendet...")
                break
        except:
            print("Bitte eine valide Eingaben geben!!\n")

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