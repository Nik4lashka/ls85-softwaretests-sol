# -*- coding: utf-8-sig -*-
"""
Baustein 01 – Grundlagen der Softwaretests
MUSTERLÖSUNG

Aufgabe 1: Fehler (Error), Defekt (Defect) und Versagen (Failure) unterscheiden.
"""


# ============================================================
# Aufgabe 1a) – Fehleranalyse
# ============================================================

def berechne_rabatt_fehlerhaft(preis: float, prozent: float) -> float:
    """
    FEHLERHAFTE Version – zur Demonstration der Begriffe.
    """
    # Defekt (Bug): Der Entwickler hat vergessen, durch 100 zu teilen.
    # Der Prozentsatz wird direkt als Faktor verwendet statt als Prozentwert.
    rabatt = preis * prozent  # <-- DEFEKT: muss preis * (prozent / 100) sein
    return preis - rabatt


# Error (falsche Handlung des Entwicklers):
#   Der Entwickler hat nicht bedacht, dass ein Prozentwert durch 100
#   geteilt werden muss, um ihn als Dezimalfaktor zu verwenden.
#   Das ist ein Denkfehler beim Schreiben des Codes.

# Defect (fehlerhafte Stelle im Code):
#   Zeile: rabatt = preis * prozent
#   Korrekt wäre: rabatt = preis * (prozent / 100)
#   Der Defekt ist die konkrete falsche Codezeile, die aus dem Error entstanden ist.

# Failure (was der Benutzer bemerken würde):
#   Ruft man berechne_rabatt_fehlerhaft(100.0, 20) auf, erhält man -1900.0
#   statt des erwarteten Ergebnisses 80.0.
#   Das Programm liefert falsche Ergebnisse – das Versagen ist zur Laufzeit sichtbar.


# ============================================================
# Aufgabe 1b) – Korrigierte Version
# ============================================================

def berechne_rabatt(preis: float, prozent: float) -> float:
    """
    Berechnet den Preis nach Rabattabzug.

    Warum durch 100 teilen: Ein Prozentwert von 20 entspricht dem Faktor 0.20.
    Die Formel lautet: Endpreis = Preis - (Preis * Prozent / 100)
    """
    # Division durch 100 wandelt Prozentwert in Dezimalfaktor um
    rabatt = preis * (prozent / 100)
    return preis - rabatt


# ============================================================
# Aufgabe 2 – Statisch vs. Dynamisch (Tabelle als Kommentar)
# ============================================================

# | Maßnahme                            | Statisch | Dynamisch |
# |-------------------------------------|----------|-----------|
# | Code Review durch einen Kollegen    |    X     |           |
# | Programm mit Testdaten ausführen    |          |     X     |
# | Syntaxprüfung durch den Editor      |    X     |           |
# | Walkthroughs im Team                |    X     |           |
# | Unit-Tests laufen lassen            |          |     X     |
# | Checklisten für Codestruktur        |    X     |           |
#
# Warum reicht statisches Testen allein nicht aus (2 Sätze):
# Statische Verfahren prüfen den Code nur auf Papier oder durch Lesen –
# dabei werden Fehler entdeckt, die erst zur Laufzeit mit echten Daten auftreten,
# nicht gefunden (z.B. Timing-Probleme, Speicherfehler, falsche Berechnungen bei
# bestimmten Eingaben). Erst das Ausführen des Programms (dynamisches Testen) zeigt,
# ob das System im Betrieb korrekt funktioniert.


# ============================================================
# Aufgabe 3 – Die sieben Grundprinzipien
# ============================================================

# Prinzip 2 – Vollständiges Testen ist unmöglich:
# Beispiel: Eine Webanwendung hat ein Eingabefeld für Benutzernamen.
# Theoretisch gibt es unendlich viele mögliche Zeichenketten – alle zu testen
# wäre selbst mit einem Rechner nicht möglich. Deshalb wählen Tester
# repräsentative Stichproben (z.B. per Äquivalenzklassen, Baustein 04).

# Prinzip 4 – Defect Clustering (Fehler häufen sich):
# Beispiel aus dem Berufsalltag: In einem neuen Modul zur Rechnungsverarbeitung
# werden 80% aller gefundenen Bugs in nur 2 von 10 Funktionen gefunden.
# Erfahrene Tester konzentrieren daher Regressionstests auf die fehleranfälligen
# Bereiche (oft: neue, komplexe oder zuletzt geänderte Codestellen).

# Überraschendstes Prinzip:
# Prinzip 7 – "Keine Fehler" bedeutet nicht "gutes System".
# Überraschend, weil es intuitiv logisch erscheint: Wenn alle Tests grünt,
# ist das Produkt gut. Aber das System könnte zwar fehlerfrei, aber trotzdem
# nutzlos sein, wenn es die falschen Anforderungen korrekt umsetzt.


# ============================================================
# Manuelle Tests (ausführen mit: python loesung.py)
# ============================================================

if __name__ == "__main__":
    print("=== Demonstration: Error / Defect / Failure ===")
    print(f"Fehlerhaft: berechne_rabatt_fehlerhaft(100.0, 20) = "
          f"{berechne_rabatt_fehlerhaft(100.0, 20)}")  # Failure: -1900.0

    print("\n=== Korrigierte Funktion: berechne_rabatt ===")
    testfaelle = [
        (100.0, 20, 80.0),    # 100 Euro, 20% Rabatt → 80 Euro
        (200.0, 10, 180.0),   # 200 Euro, 10% Rabatt → 180 Euro
        (50.0,  0,  50.0),    # 50 Euro, kein Rabatt → 50 Euro
        (150.0, 50, 75.0),    # 150 Euro, 50% Rabatt → 75 Euro
    ]
    alle_korrekt = True
    for preis, prozent, erwartet in testfaelle:
        ergebnis = berechne_rabatt(preis, prozent)
        ok = "OK" if abs(ergebnis - erwartet) < 0.001 else "FEHLER"
        if ok == "FEHLER":
            alle_korrekt = False
        print(f"  berechne_rabatt({preis}, {prozent}) = {ergebnis} "
              f"(erwartet: {erwartet}) → {ok}")

    print(f"\nAlle Tests korrekt: {alle_korrekt}")
