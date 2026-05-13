# -*- coding: utf-8-sig -*-
"""
Baustein 04 – Äquivalenzklassen & Grenzwertanalyse
MUSTERLÖSUNG

Äquivalenzklassen: Alle Werte einer Klasse verhalten sich gleich →
es reicht ein repräsentativer Vertreter pro Klasse zu testen.

Grenzwertanalyse: Fehler entstehen besonders häufig an den Grenzen
(off-by-one: z.B. >= 18 statt > 18 verwechseln).
"""

import unittest


# ============================================================
# Aufgabe 1 – Mengenvalidierung
#
# Äquivalenzklassen:
#   AK1 (gültig):   1 ≤ menge ≤ 999  (ganzzahlig)
#   AK2 (ungültig): menge ≤ 0        (zu klein inkl. 0 und negativ)
#   AK3 (ungültig): menge ≥ 1000     (zu groß)
#   AK4 (ungültig): kein int-Typ     (z.B. str, float, None)
#
# Grenzwerte: 0, 1, 999, 1000
# ============================================================

def validiere_menge(menge) -> bool:
    """
    Prüft, ob eine Bestellmenge gültig ist.

    Regeln:
    - Typ: ganzzahlig (int)
    - Minimum: 1
    - Maximum: 999

    Warum isinstance-Check zuerst: Wenn menge kein int ist, würden
    die numerischen Vergleiche möglicherweise TypeError werfen.
    """
    # AK4: Typprüfung muss vor Wertebereichsprüfung erfolgen
    if not isinstance(menge, int):
        return False

    # AK2 + AK3: Wertebereich 1–999
    return 1 <= menge <= 999


# ============================================================
# Aufgabe 2 – Passwortprüfung
#
# Äquivalenzklassen pro Regel:
#   Länge:          AK1: 8–64 (gültig), AK2: < 8 (ungültig), AK3: > 64 (ungültig)
#   Großbuchstabe:  AK4: mind. 1 (gültig), AK5: keiner (ungültig)
#   Ziffer:         AK6: mind. 1 (gültig), AK7: keine (ungültig)
#   Leerzeichen:    AK8: kein (gültig), AK9: mind. 1 (ungültig)
# ============================================================

def pruefe_passwort(passwort: str) -> bool:
    """
    Prüft, ob ein Passwort den Anforderungen entspricht.

    Regeln:
    - Länge: 8–64 Zeichen
    - Mindestens ein Großbuchstabe
    - Mindestens eine Ziffer
    - Keine Leerzeichen

    Jede Bedingung prüft eine eigene Äquivalenzklasse.
    """
    # AK2/AK3: Längengrenzen
    if not (8 <= len(passwort) <= 64):
        return False

    # AK5: Mindestens ein Großbuchstabe
    if not any(c.isupper() for c in passwort):
        return False

    # AK7: Mindestens eine Ziffer
    if not any(c.isdigit() for c in passwort):
        return False

    # AK9: Kein Leerzeichen
    if " " in passwort:
        return False

    return True


# ============================================================
# Aufgabe 4 – Notenberechnung
#
# Äquivalenzklassen:
#   AK1 (gültig, Note 1): 92–100
#   AK2 (gültig, Note 2): 81–91
#   AK3 (gültig, Note 3): 67–80
#   AK4 (gültig, Note 4): 50–66
#   AK5 (gültig, Note 5): 30–49
#   AK6 (gültig, Note 6): 0–29
#   AK7 (ungültig):        < 0
#   AK8 (ungültig):        > 100
# ============================================================

def berechne_note(punkte: int) -> int:
    """
    Gibt die Note (1–6) für eine Punktzahl zurück.

    Raises:
        ValueError: Wenn punkte außerhalb [0, 100] liegt.

    Warum ValueError statt return: Ungültige Eingaben sind Programmfehler,
    keine erwarteten Zustände. Der Aufrufer muss sie behandeln.
    """
    # AK7 + AK8: Ungültige Werte abweisen
    if not isinstance(punkte, int) or punkte < 0 or punkte > 100:
        raise ValueError(f"Punkte müssen zwischen 0 und 100 liegen, war: {punkte}")

    # Notenberechnung von oben nach unten (höchste Punktzahl zuerst)
    if punkte >= 92:
        return 1
    elif punkte >= 81:
        return 2
    elif punkte >= 67:
        return 3
    elif punkte >= 50:
        return 4
    elif punkte >= 30:
        return 5
    else:
        return 6


# ============================================================
# Testklasse – Äquivalenzklassen und Grenzwerte systematisch testen
# ============================================================

class TestValidiereMenge(unittest.TestCase):
    """
    Testfälle decken alle 4 Äquivalenzklassen und alle 4 Grenzwerte ab.
    """

    # --- AK1: Gültige Klasse ---
    def test_ak1_repraesent_wert_mitte(self):
        """AK1 (gültig): Repräsentant = 500 (Mitte des Bereichs)."""
        self.assertTrue(validiere_menge(500))

    # --- AK2: Zu kleiner Wert ---
    def test_ak2_repraesent_negative_zahl(self):
        """AK2 (ungültig): Repräsentant = -5 (negativ)."""
        self.assertFalse(validiere_menge(-5))

    def test_ak2_repraesent_null(self):
        """AK2 (ungültig): Repräsentant = 0 (explizit verboten)."""
        self.assertFalse(validiere_menge(0))

    # --- AK3: Zu großer Wert ---
    def test_ak3_repraesent_1500(self):
        """AK3 (ungültig): Repräsentant = 1500 (weit über Maximum)."""
        self.assertFalse(validiere_menge(1500))

    # --- AK4: Falscher Typ ---
    def test_ak4_repraesent_string(self):
        """AK4 (ungültig): String statt int."""
        self.assertFalse(validiere_menge("viel"))

    def test_ak4_repraesent_float(self):
        """AK4 (ungültig): Float statt int (auch 1.0 ist kein int!)."""
        self.assertFalse(validiere_menge(1.0))

    def test_ak4_repraesent_none(self):
        """AK4 (ungültig): None-Eingabe."""
        self.assertFalse(validiere_menge(None))

    # --- Grenzwerte ---
    def test_gw1_grenzwert_0(self):
        """GW1: Grenzwert 0 → ungültig (eine Einheit unter dem Minimum)."""
        self.assertFalse(validiere_menge(0))

    def test_gw2_grenzwert_1(self):
        """GW2: Grenzwert 1 → gültig (untere Grenze)."""
        self.assertTrue(validiere_menge(1))

    def test_gw3_grenzwert_999(self):
        """GW3: Grenzwert 999 → gültig (obere Grenze)."""
        self.assertTrue(validiere_menge(999))

    def test_gw4_grenzwert_1000(self):
        """GW4: Grenzwert 1000 → ungültig (eine Einheit über dem Maximum)."""
        self.assertFalse(validiere_menge(1000))


class TestPruefePasswort(unittest.TestCase):
    """
    Jeder Test repräsentiert eine andere Äquivalenzklasse.
    """

    def test_ak1_gueltiges_passwort(self):
        """AK1+AK4+AK6+AK8: Alle Regeln erfüllt → True."""
        self.assertTrue(pruefe_passwort("Abc12345"))

    def test_ak2_zu_kurz(self):
        """AK2 (Länge < 8): Zu kurzes Passwort → False."""
        self.assertFalse(pruefe_passwort("Ab1"))

    def test_ak3_zu_lang(self):
        """AK3 (Länge > 64): Zu langes Passwort → False."""
        self.assertFalse(pruefe_passwort("A1" + "a" * 64))

    def test_ak5_kein_grossbuchstabe(self):
        """AK5: Kein Großbuchstabe → False."""
        self.assertFalse(pruefe_passwort("abc12345"))

    def test_ak7_keine_ziffer(self):
        """AK7: Keine Ziffer → False."""
        self.assertFalse(pruefe_passwort("ABCDefgh"))

    def test_ak9_mit_leerzeichen(self):
        """AK9: Enthält Leerzeichen → False."""
        self.assertFalse(pruefe_passwort("Abc 1234"))

    # Grenzwerte Länge
    def test_gw_laenge_8(self):
        """Grenzwert: genau 8 Zeichen (untere Grenze) → gültig."""
        self.assertTrue(pruefe_passwort("Abcdef1!"))

    def test_gw_laenge_64(self):
        """Grenzwert: genau 64 Zeichen (obere Grenze) → gültig."""
        pw = "A1" + "a" * 62  # 2 + 62 = 64 Zeichen
        self.assertTrue(pruefe_passwort(pw))

    def test_gw_laenge_7(self):
        """Grenzwert: 7 Zeichen (unter unterer Grenze) → ungültig."""
        self.assertFalse(pruefe_passwort("Abcd12"))

    def test_gw_laenge_65(self):
        """Grenzwert: 65 Zeichen (über oberer Grenze) → ungültig."""
        pw = "A1" + "a" * 63  # 65 Zeichen
        self.assertFalse(pruefe_passwort(pw))


class TestBerechneNote(unittest.TestCase):
    """
    Testfälle für alle Äquivalenzklassen und alle Notengrenzen (Grenzwerte).
    """

    # --- Gültige Klassen: je 2 Vertreter pro Note ---
    def test_ak1_note1_repraesent_96(self):
        """AK1 (Note 1): Repräsentant 96 (Mitte 92–100)."""
        self.assertEqual(berechne_note(96), 1)

    def test_ak2_note2_repraesent_85(self):
        """AK2 (Note 2): Repräsentant 85 (Mitte 81–91)."""
        self.assertEqual(berechne_note(85), 2)

    def test_ak3_note3_repraesent_73(self):
        """AK3 (Note 3): Repräsentant 73 (Mitte 67–80)."""
        self.assertEqual(berechne_note(73), 3)

    def test_ak4_note4_repraesent_58(self):
        """AK4 (Note 4): Repräsentant 58 (Mitte 50–66)."""
        self.assertEqual(berechne_note(58), 4)

    def test_ak5_note5_repraesent_40(self):
        """AK5 (Note 5): Repräsentant 40 (Mitte 30–49)."""
        self.assertEqual(berechne_note(40), 5)

    def test_ak6_note6_repraesent_15(self):
        """AK6 (Note 6): Repräsentant 15 (Mitte 0–29)."""
        self.assertEqual(berechne_note(15), 6)

    # --- Grenzwerte (Notengrenzen) ---
    def test_gw_0_note6(self):
        """GW: 0 → Note 6 (untere Grenze insgesamt)."""
        self.assertEqual(berechne_note(0), 6)

    def test_gw_29_note6(self):
        """GW: 29 → Note 6 (letzte Note 6)."""
        self.assertEqual(berechne_note(29), 6)

    def test_gw_30_note5(self):
        """GW: 30 → Note 5 (erste Note 5)."""
        self.assertEqual(berechne_note(30), 5)

    def test_gw_49_note5(self):
        """GW: 49 → Note 5 (letzte Note 5)."""
        self.assertEqual(berechne_note(49), 5)

    def test_gw_50_note4(self):
        """GW: 50 → Note 4 (erste Note 4)."""
        self.assertEqual(berechne_note(50), 4)

    def test_gw_66_note4(self):
        """GW: 66 → Note 4 (letzte Note 4)."""
        self.assertEqual(berechne_note(66), 4)

    def test_gw_67_note3(self):
        """GW: 67 → Note 3 (erste Note 3)."""
        self.assertEqual(berechne_note(67), 3)

    def test_gw_80_note3(self):
        """GW: 80 → Note 3 (letzte Note 3)."""
        self.assertEqual(berechne_note(80), 3)

    def test_gw_81_note2(self):
        """GW: 81 → Note 2 (erste Note 2)."""
        self.assertEqual(berechne_note(81), 2)

    def test_gw_91_note2(self):
        """GW: 91 → Note 2 (letzte Note 2)."""
        self.assertEqual(berechne_note(91), 2)

    def test_gw_92_note1(self):
        """GW: 92 → Note 1 (erste Note 1)."""
        self.assertEqual(berechne_note(92), 1)

    def test_gw_100_note1(self):
        """GW: 100 → Note 1 (obere Grenze insgesamt)."""
        self.assertEqual(berechne_note(100), 1)

    # --- Ungültige Klassen ---
    def test_ak7_negativ_wirft_fehler(self):
        """AK7 (ungültig: < 0): ValueError erwartet."""
        with self.assertRaises(ValueError):
            berechne_note(-1)

    def test_ak8_zu_hoch_wirft_fehler(self):
        """AK8 (ungültig: > 100): ValueError erwartet."""
        with self.assertRaises(ValueError):
            berechne_note(101)


if __name__ == "__main__":
    # Manuelle Ausgabe zur Visualisierung
    print("=== Grenzwertanalyse berechne_note ===")
    grenzwerte = [0, 29, 30, 49, 50, 66, 67, 80, 81, 91, 92, 100]
    for p in grenzwerte:
        print(f"  berechne_note({p:3d}) → Note {berechne_note(p)}")

    print("\n=== Ungültige Werte ===")
    for p in [-1, 101]:
        try:
            berechne_note(p)
        except ValueError as e:
            print(f"  berechne_note({p}) → ValueError: {e}")

    print("\n=== Unit-Tests ===")
    unittest.main(verbosity=2, exit=False)
