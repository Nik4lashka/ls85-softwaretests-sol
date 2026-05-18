"""
Baustein 03 – Testmethoden (Black-Box, White-Box, Grey-Box)
Startvorlage – bearbeite diese Datei für deine Aufgaben.
"""


# ============================================================
# Aufgabe 1 – Black-Box-Test (Implementierung absichtlich unten)
# ============================================================

# | TC-Nr | Eingabe (User/PW) | Erwartete Ausgabe | Kategorie        |
# | TC01  | admin / geheim123 | true              | Gültiger Login   |
# | TC02  | test / abcdefghij | false             | Ungültiger Login |
# | TC03  | niklas / niklas12 | false             | Ungültiger Login |
# | TC04  | kai / brozmann    | false             | Ungültiger Login |
# | TC05  | admin / geheim123 | true              | Gültiger Login   |
# | TC06  | kein / bockmehr   | false             | Ungültiger Login |

def authentifiziere_benutzer(benutzername: str, passwort: str) -> bool:
    """
    Prüft, ob Benutzername und Passwort gültig sind.

    Spezifikation (für Black-Box-Tests):
    - Benutzername: 3–20 Zeichen, nur Buchstaben, Zahlen, Unterstrich
    - Passwort: mindestens 8 Zeichen
    - Bekannte gültige Kombination: 'admin' / 'geheim123'
    - Gibt True zurück wenn gültig, False wenn ungültig

    Hinweis: Schau dir die Implementierung erst NACH dem Erstellen
    deiner Black-Box-Testfälle an!
    """
    # --- Implementierung (erst nach Aufgabe 1a lesen!) ---
    import re

    if not benutzername or not passwort:
        return False

    if not re.match(r'^[a-zA-Z0-9_]{3,20}$', benutzername):
        return False

    if len(passwort) < 8:
        return False

    gueltige_benutzer = {"admin": "geheim123", "testuser": "passwort1"}
    return gueltige_benutzer.get(benutzername) == passwort


# Aufgabe 1b) – Führe deine Testfälle hier aus:
if __name__ == "__main__":
    print("=== Aufgabe 1 – Black-Box-Tests: authentifiziere_benutzer ===")

    # TODO: Füge deine Testfälle aus der Tabelle ein
    # Beispiel (TC01):
    ergebnis = authentifiziere_benutzer("admin", "geheim123")
    print(f"TC01: admin/geheim123 → {ergebnis} (erwartet: True)")

    # TC02:
    ergebnis = authentifiziere_benutzer("test", "abcdefghij")
    print(f"TC01: test/abcdefghij → {ergebnis} (erwartet: False)")

    # TC03:
    ergebnis = authentifiziere_benutzer("niklas", "niklas12")
    print(f"TC01: niklas/niklas12 → {ergebnis} (erwartet: False)")

    # TC04:
    ergebnis = authentifiziere_benutzer("kai", "brozmann")
    print(f"TC01: kai/brozmann → {ergebnis} (erwartet: False)")

    # TC05:
    ergebnis = authentifiziere_benutzer("admin", "geheim123")
    print(f"TC01: admin/geheim123 → {ergebnis} (erwartet: True)")

    # TC06:
    ergebnis = authentifiziere_benutzer("kein", "bockmehr")
    print(f"TC01: kein/bockmehr → {ergebnis} (erwartet: False)")


# ============================================================
# Aufgabe 2 – White-Box-Test: Kontrollflussgraph & Coverage
# ============================================================

def kategorisiere_bestellung(betrag: float, ist_neukunde: bool, gutscheincode: str) -> str:
    """
    Kategorisiert eine Bestellung und gibt eine Priorität zurück.

    Erstelle den Kontrollflussgraphen dieser Funktion für Aufgabe 2.
    """
    if betrag <= 0:
        return "UNGUELTIG"

    if ist_neukunde:
        prioritaet = "HOCH"
    else:
        prioritaet = "NORMAL"

    if gutscheincode == "VIP2024":
        prioritaet = "HOCH"

    if betrag >= 500:
        if prioritaet == "HOCH":
            return "EXPRESS"
        else:
            return "PRIORITAET"

    return prioritaet


# Aufgabe 2b+c) – Testfälle für Statement und Branch Coverage:
if __name__ == "__main__":
    print("\n=== Aufgabe 2 – White-Box Coverage: kategorisiere_bestellung ===")

    ergebnis = kategorisiere_bestellung(0, False, "")
    print(f"TC01: 0/False/.. → {ergebnis} (erwartet: UNGUELTIG)")

    ergebnis = kategorisiere_bestellung(600, True, "")
    print(f"TC02: 600/True/.. → {ergebnis} (erwartet: EXPRESS)")

    ergebnis = kategorisiere_bestellung(600, False, "")
    print(f"TC03: 600/False/.. → {ergebnis} (erwartet: PRIORITAET)")

    ergebnis = kategorisiere_bestellung(100, False, "")
    print(f"TC04: 100/False/VIP2024 → {ergebnis} (erwartet: NORMAL)")
    # TODO: Ergänze weitere Testfälle für vollständige Branch Coverage

    #* Meiner Meinung nach ist das die Branch und Statement coverage (?)

    # Halte fest, welche Zeilen von welchem Testfall abgedeckt werden.
