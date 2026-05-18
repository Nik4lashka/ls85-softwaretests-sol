"""
Baustein 01 – Grundlagen der Softwaretests
Startvorlage – bearbeite diese Datei für deine Aufgaben.
"""


# ============================================================
# Aufgabe 1 – Fehlerhafte Funktion
# ============================================================

def berechne_rabatt(preis: float, prozent: float) -> float:
    """
    Berechnet den Preis nach Rabattabzug.

    Beispiel:
        berechne_rabatt(100.0, 20) soll 80.0 zurückgeben.
    """
    # Hier ist ein Defekt eingebaut – findest du ihn?
    rabatt = preis * prozent  # <-- Zeile mit Defekt
    return preis - rabatt


# Aufgabe 1a): Beantworte folgende Fragen als Kommentar:

#  Error (falsche Handlung des Entwicklers):
#* Bei der berechnung wird der preis * prozent gerechnet, prozent ist aber (bei dem Beispiel)
#* 20 und nicht 0.20

# Defect (fehlerhafte Stelle im Code):
#* rabatt = preis * prozent (es müsste prozent / 100 sein)

# Failure (was der Benutzer bemerken würde):
#* der Rabatt wäre wäre viel zu hoch und der return Wert zu niedrig (bzw. sogar negativ)


# Aufgabe 1b): Korrigiere die Funktion unten und füge print()-Tests hinzu.

def berechne_rabatt_korrigiert(preis: float, prozent: float) -> float:
    """
    Korrigierte Version von berechne_rabatt().
    TODO: Implementiere die korrekte Logik.
    """
    rabatt = preis * (prozent / 100)
    return preis - rabatt


# Manuelle Tests (werden in Baustein 05 durch echte Unit-Tests ersetzt)
if __name__ == "__main__":
    # TODO: Ergänze mindestens 3 eigene print()-Tests für berechne_rabatt_korrigiert().
    # Überlege selbst: Was sind sinnvolle Eingaben? Was erwartest du als Ergebnis?

    print("=== Test: berechne_rabatt (fehlerhaft) ===")
    print(berechne_rabatt(100.0, 20))  # Falsche Ausgabe erwartet

    print("\n=== Test: berechne_rabatt_korrigiert ===")
    print(berechne_rabatt_korrigiert(100.0, 20))

    print("\n=== Test: berechne_rabatt_korrigiert ===")
    print(berechne_rabatt_korrigiert(350.0, 9))

    print("\n=== Test: berechne_rabatt_korrigiert ===")
    print(berechne_rabatt_korrigiert(187, 11))


# ============================================================
# Aufgabe 2 – Statisch vs. dynamisch
# ============================================================

# Trage hier deine ausgefüllte Tabelle als Kommentar ein:
#
# | Maßnahme                            | Statisch | Dynamisch |
# |-------------------------------------|----------|-----------|
# | Code Review durch einen Kollegen    |    x     |           |
# | Programm mit Testdaten ausführen    |          |     x     |
# | Syntaxprüfung durch den Editor      |    x     |           |
# | Walkthroughs im Team                |    x     |           |
# | Unit-Tests laufen lassen            |          |     x     |
# | Checklisten für Codestruktur        |    x     |           |
#
# Warum reicht statisches Testen allein nicht aus?
#* Beim Manuellen Testen ist es immer möglich dass Fehler nicht auffallen - oft fehlt einem der
#* Einblick in den Code, wenn es nicht der eigene ist und man "nur mal eben drüber schaut"


# ============================================================
# Aufgabe 3 – Grundprinzipien (Antworten als Kommentar)
# ============================================================

# Prinzip 2 – Vollständiges Testen ist unmöglich:
# Beispiel aus dem Berufsalltag:
# TODO: Deine Antwort hier

# Prinzip 4 – Defect Clustering:
# Beispiel aus dem Berufsalltag:
# TODO: Deine Antwort hier

# Welches Prinzip überrascht dich? Warum?
# TODO: Deine Antwort hier
