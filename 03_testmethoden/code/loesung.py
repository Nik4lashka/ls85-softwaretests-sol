# -*- coding: utf-8-sig -*-
"""
Baustein 03 – Testmethoden (Black-Box, White-Box)
MUSTERLÖSUNG

Zeigt Black-Box-Tests (nur Spezifikation bekannt) und
White-Box-Tests (Quellcode bekannt, Coverage-Analyse).
"""

import re
import unittest


# ============================================================
# Zu testende Funktionen (aus starter.py)
# ============================================================

def authentifiziere_benutzer(benutzername: str, passwort: str) -> bool:
    """
    BLACK-BOX-Sicht: Nur diese Spezifikation zählt für die Tests!
    - Benutzername: 3–20 Zeichen, nur Buchstaben/Zahlen/Unterstrich
    - Passwort: mindestens 8 Zeichen
    - Bekannte gültige Kombination: 'admin' / 'geheim123'
    """
    if not benutzername or not passwort:
        return False
    if not re.match(r'^[a-zA-Z0-9_]{3,20}$', benutzername):
        return False
    if len(passwort) < 8:
        return False
    gueltige_benutzer = {"admin": "geheim123", "testuser": "passwort1"}
    return gueltige_benutzer.get(benutzername) == passwort


def kategorisiere_bestellung(betrag: float, ist_neukunde: bool, gutscheincode: str) -> str:
    """
    WHITE-BOX-Sicht: Wir kennen den Code und analysieren alle Zweige.
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


# ============================================================
# BLACK-BOX-TESTS: authentifiziere_benutzer()
#
# Wir testen NUR über Eingaben und Ausgaben – der Code interessiert
# uns hier nicht. Grundlage ist ausschließlich die Spezifikation.
# ============================================================

class TestAuthentifizierungBlackBox(unittest.TestCase):
    """
    Black-Box-Tests: Testfälle werden aus der Spezifikation abgeleitet,
    nicht aus dem Code. Kein Kommentar zu Implementierungsdetails!
    """

    # --- Gültige Eingaben ---

    def test_tc01_gueltiger_login(self):
        """TC01: Bekannte gültige Kombination → True."""
        # Kategorie: Normalfall / gültige Äquivalenzklasse
        self.assertTrue(authentifiziere_benutzer("admin", "geheim123"))

    def test_tc02_anderer_gueltiger_benutzer(self):
        """TC02: Zweiter bekannter Benutzer → True."""
        self.assertTrue(authentifiziere_benutzer("testuser", "passwort1"))

    # --- Ungültiges Passwort ---

    def test_tc03_passwort_zu_kurz(self):
        """TC03: Passwort unter 8 Zeichen → False (ungültige ÄK: Länge < 8)."""
        self.assertFalse(authentifiziere_benutzer("admin", "kurz"))

    def test_tc04_falsches_passwort(self):
        """TC04: Richtiger Benutzer, falsches Passwort → False."""
        self.assertFalse(authentifiziere_benutzer("admin", "falschesPasswort123"))

    # --- Ungültiger Benutzername ---

    def test_tc05_benutzername_zu_kurz(self):
        """TC05: Benutzername kürzer als 3 Zeichen → False (ungültige ÄK: Länge < 3)."""
        self.assertFalse(authentifiziere_benutzer("ab", "geheim123"))

    def test_tc06_benutzername_mit_sonderzeichen(self):
        """TC06: Sonderzeichen im Benutzername → False (Spezifikation: nur [a-zA-Z0-9_])."""
        self.assertFalse(authentifiziere_benutzer("admin!", "geheim123"))

    def test_tc07_benutzername_zu_lang(self):
        """TC07: Benutzername über 20 Zeichen → False (ungültige ÄK: Länge > 20)."""
        self.assertFalse(authentifiziere_benutzer("a" * 21, "geheim123"))

    # --- Leere / None-Eingaben ---

    def test_tc08_leerer_benutzername(self):
        """TC08: Leerer String → False (Grenzwert: Länge 0)."""
        self.assertFalse(authentifiziere_benutzer("", "geheim123"))

    def test_tc09_leeres_passwort(self):
        """TC09: Leeres Passwort → False."""
        self.assertFalse(authentifiziere_benutzer("admin", ""))

    # --- Grenzwerte Benutzername-Länge ---

    def test_tc10_benutzername_genau_3_zeichen(self):
        """TC10: Benutzername mit genau 3 Zeichen (unterer Grenzwert) → valide Länge."""
        # Unbekannter Benutzer → False wegen Datenbank, aber die Validierung schlägt nicht fehl
        result = authentifiziere_benutzer("abc", "geheim123")
        self.assertFalse(result)  # Unbekannter User → False

    def test_tc11_unbekannter_benutzer(self):
        """TC11: Syntaktisch gültiger Benutzername, aber unbekannt → False."""
        self.assertFalse(authentifiziere_benutzer("maxmuster", "geheim123"))


# ============================================================
# WHITE-BOX-TESTS: kategorisiere_bestellung()
#
# Wir kennen den Code und leiten Testfälle aus dem Kontrollflussgraphen ab.
# Ziel: Alle Zweige (Branch Coverage) mindestens einmal durchlaufen.
#
# Kontrollflussgraph (Pseudocode):
#   K1: betrag <= 0? → ja → UNGUELTIG
#                    → nein ↓
#   K2: ist_neukunde? → ja → prioritaet = "HOCH"
#                     → nein → prioritaet = "NORMAL"
#   K3: gutscheincode == "VIP2024"? → ja → prioritaet = "HOCH"
#                                   → nein → (unveraendert)
#   K4: betrag >= 500? → ja: K5: prioritaet == "HOCH"? → ja → EXPRESS
#                                                       → nein → PRIORITAET
#                     → nein → return prioritaet
# ============================================================

class TestKategorisiereBestellungWhiteBox(unittest.TestCase):
    """
    White-Box-Tests: Testfälle decken gezielt alle Code-Zweige ab.
    Kommentare zeigen, welcher Pfad durch den Kontrollflussgraphen führt.
    """

    def test_wb01_negativer_betrag(self):
        """
        Pfad: K1 (ja) → UNGUELTIG
        Statement Coverage: Zeile 'return "UNGUELTIG"' abgedeckt.
        """
        self.assertEqual(kategorisiere_bestellung(-1, False, ""), "UNGUELTIG")

    def test_wb02_neukunde_kleiner_betrag(self):
        """
        Pfad: K1 (nein) → K2 (ja: HOCH) → K3 (nein) → K4 (nein) → return "HOCH"
        Zweige abgedeckt: K1-nein, K2-ja, K3-nein, K4-nein
        """
        self.assertEqual(kategorisiere_bestellung(100, True, ""), "HOCH")

    def test_wb03_kein_neukunde_kleiner_betrag(self):
        """
        Pfad: K1 (nein) → K2 (nein: NORMAL) → K3 (nein) → K4 (nein) → return "NORMAL"
        Neuer Zweig: K2-nein
        """
        self.assertEqual(kategorisiere_bestellung(100, False, ""), "NORMAL")

    def test_wb04_gutschein_kleiner_betrag(self):
        """
        Pfad: K1 (nein) → K2 (nein: NORMAL) → K3 (ja: HOCH) → K4 (nein) → return "HOCH"
        Neuer Zweig: K3-ja (Gutschein-Zweig abgedeckt)
        """
        self.assertEqual(kategorisiere_bestellung(100, False, "VIP2024"), "HOCH")

    def test_wb05_neukunde_grosser_betrag(self):
        """
        Pfad: K1 (nein) → K2 (ja: HOCH) → K3 (nein) → K4 (ja) → K5 (ja) → EXPRESS
        Neue Zweige: K4-ja, K5-ja
        """
        self.assertEqual(kategorisiere_bestellung(600, True, ""), "EXPRESS")

    def test_wb06_kein_neukunde_grosser_betrag(self):
        """
        Pfad: K1 (nein) → K2 (nein: NORMAL) → K3 (nein) → K4 (ja) → K5 (nein) → PRIORITAET
        Neuer Zweig: K5-nein
        Damit ist 100% Branch Coverage erreicht!
        """
        self.assertEqual(kategorisiere_bestellung(600, False, ""), "PRIORITAET")

    def test_wb07_grenzwert_betrag_genau_500(self):
        """
        Grenzwert: betrag == 500 → K4 (ja, da >= 500).
        Grenzwerttest ergänzt White-Box-Analyse.
        """
        self.assertEqual(kategorisiere_bestellung(500, True, ""), "EXPRESS")

    def test_wb08_grenzwert_betrag_499(self):
        """
        Grenzwert: betrag == 499 → K4 (nein).
        """
        self.assertEqual(kategorisiere_bestellung(499, False, ""), "NORMAL")


# ============================================================
# Vergleich Black-Box vs. White-Box (als Kommentar)
# ============================================================

# | Merkmal                   | Black-Box                        | White-Box                         |
# |---------------------------|----------------------------------|-----------------------------------|
# | Codekenntnis notwendig?   | Nein                             | Ja                                |
# | Aus wessen Perspektive?   | Benutzer / Kunde / Tester extern | Entwickler / interner Tester      |
# | Was wird geprüft?         | Ein-/Ausgabe laut Spezifikation  | Codestruktur, alle Zweige/Pfade   |
# | Typische Werkzeuge        | Testfälle aus Anforderungsdoku   | Coverage-Tools (pytest-cov etc.)  |
# | Vorteil                   | Testet was der Nutzer erwartet   | Lücken im Kontrollfluss erkennbar |
# | Nachteil                  | Kann interne Logik nicht prüfen  | Implementierungsabhängig          |


if __name__ == "__main__":
    unittest.main(verbosity=2)
