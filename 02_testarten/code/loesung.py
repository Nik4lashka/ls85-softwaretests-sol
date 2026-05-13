# -*- coding: utf-8-sig -*-
"""
Baustein 02 – Testarten
MUSTERLÖSUNG

Zeigt Unit-Tests, manuelle Tests und erklärt wann welche Teststufe passt.
"""

import unittest
from typing import List, Dict


# ============================================================
# Aufgabe 1 – Teststufen-Tabelle (als Kommentar)
# ============================================================

# | Beschreibung                                            | Teststufe         |
# |---------------------------------------------------------|-------------------|
# | Testet einzelne Funktionen oder Methoden isoliert       | Unit-Test         |
# | Prüft das Zusammenspiel mehrerer Module                 | Integrationstest  |
# | Testet das gesamte System gegen die Anforderungen       | Systemtest        |
# | Auftraggeber prüft, ob seine Anforderungen erfüllt sind | Abnahmetest (UAT) |


# ============================================================
# Webshop-Komponenten (aus starter.py übernommen)
# ============================================================

def berechne_gesamtpreis(artikel: List[Dict], rabatt_prozent: float = 0) -> float:
    """
    Berechnet den Gesamtpreis eines Warenkorbs.

    Unit-Test-Kandidat: Diese Funktion ist isoliert testbar – keine externen
    Abhängigkeiten (keine Datenbank, keine Netzwerkkommunikation).
    """
    if not 0 <= rabatt_prozent <= 100:
        raise ValueError(f"Rabatt muss zwischen 0 und 100 liegen, war: {rabatt_prozent}")

    summe = sum(a["preis"] * a["menge"] for a in artikel)
    rabatt = summe * (rabatt_prozent / 100)
    return round(summe - rabatt, 2)


def finde_guenstigsten_artikel(artikel: List[Dict]) -> Dict:
    """
    Gibt den Artikel mit dem niedrigsten Einzelpreis zurück.

    Raises:
        ValueError: Wenn die Liste leer ist.
    """
    if not artikel:
        raise ValueError("Warenkorb ist leer.")
    return min(artikel, key=lambda a: a["preis"])


# ============================================================
# Aufgabe 2b) – Manuelle Tests (vor Unit-Tests mit print())
# ============================================================

# Testdaten
WARENKORB_NORMAL = [
    {"name": "USB-Hub", "preis": 29.99, "menge": 1},
    {"name": "Maus",    "preis": 19.99, "menge": 2},
]

WARENKORB_LEER = []


# ============================================================
# Vollständige Unit-Test-Klasse (was Schüler in Baustein 05 lernen)
# ============================================================

class TestBerechneGesamtpreis(unittest.TestCase):
    """
    Unit-Tests für berechne_gesamtpreis().

    WANN Unit-Test: Immer wenn eine einzelne Funktion/Methode isoliert
    geprüft werden kann, ohne andere Module zu brauchen.
    Unit-Tests sind schnell, stabil und zeigen präzise wo ein Fehler liegt.
    """

    def test_normaler_einkauf_ohne_rabatt(self):
        """Normaler Warenkorb ohne Rabatt → Summe aller Positionen."""
        # 29.99 * 1 + 19.99 * 2 = 69.97
        ergebnis = berechne_gesamtpreis(WARENKORB_NORMAL)
        self.assertAlmostEqual(ergebnis, 69.97, places=2)

    def test_einkauf_mit_10_prozent_rabatt(self):
        """10% Rabatt reduziert den Preis korrekt."""
        # 69.97 * 0.9 = 62.973 → gerundet 62.97
        ergebnis = berechne_gesamtpreis(WARENKORB_NORMAL, rabatt_prozent=10)
        self.assertAlmostEqual(ergebnis, 62.97, places=2)

    def test_leerer_warenkorb_gibt_null(self):
        """Leerer Warenkorb → 0.0, kein Fehler!

        Sonderfall: Eine leere Liste hat Summe 0. Das ist gültiges Verhalten,
        kein Fehler. Deshalb muss die Funktion 0.0 zurückgeben, nicht crashen.
        """
        ergebnis = berechne_gesamtpreis(WARENKORB_LEER)
        self.assertEqual(ergebnis, 0.0)

    def test_ungültiger_rabatt_wirft_fehler(self):
        """Rabatt > 100 → ValueError (Validierung an der Systemgrenze)."""
        with self.assertRaises(ValueError):
            berechne_gesamtpreis(WARENKORB_NORMAL, rabatt_prozent=150)

    def test_vollständiger_rabatt_gibt_null(self):
        """100% Rabatt → Preis ist 0."""
        ergebnis = berechne_gesamtpreis(WARENKORB_NORMAL, rabatt_prozent=100)
        self.assertEqual(ergebnis, 0.0)

    def test_einzelner_artikel(self):
        """Warenkorb mit nur einem Artikel."""
        warenkorb = [{"name": "Laptop", "preis": 999.99, "menge": 1}]
        self.assertAlmostEqual(berechne_gesamtpreis(warenkorb), 999.99, places=2)


class TestFindePguenstigstenArtikel(unittest.TestCase):
    """
    Unit-Tests für finde_guenstigsten_artikel().

    WANN Integrationstest (nicht hier!): Wenn die Funktion z.B. Preise aus
    einer Datenbank liest, müsste ein Integrationstest Datenbank + Funktion
    gemeinsam testen.
    """

    def test_findet_guenstigsten_aus_mehreren(self):
        """Standard-Fall: günstigsten Artikel zurückgeben."""
        artikel = [
            {"name": "Tastatur", "preis": 49.99},
            {"name": "Maus",     "preis": 19.99},
            {"name": "Monitor",  "preis": 299.00},
        ]
        ergebnis = finde_guenstigsten_artikel(artikel)
        self.assertEqual(ergebnis["name"], "Maus")

    def test_leere_liste_wirft_fehler(self):
        """Leere Liste → ValueError."""
        with self.assertRaises(ValueError):
            finde_guenstigsten_artikel([])


# ============================================================
# Aufgabe 2b) – Manuelle Tests mit print()
# ============================================================

if __name__ == "__main__":
    print("=== Manuelle Tests: berechne_gesamtpreis ===\n")

    # Test 1 – Normaler Einkauf ohne Rabatt
    ergebnis1 = berechne_gesamtpreis(WARENKORB_NORMAL)
    print(f"Test 1 – Kein Rabatt:     {ergebnis1} (erwartet: 69.97) "
          f"→ {'OK' if abs(ergebnis1 - 69.97) < 0.01 else 'FEHLER'}")

    # Test 2 – Einkauf mit 10% Rabatt
    ergebnis2 = berechne_gesamtpreis(WARENKORB_NORMAL, rabatt_prozent=10)
    print(f"Test 2 – 10% Rabatt:      {ergebnis2} (erwartet: 62.97) "
          f"→ {'OK' if abs(ergebnis2 - 62.97) < 0.01 else 'FEHLER'}")

    # Test 3 – Leerer Warenkorb (Sonderfall: kein ValueError, sondern 0.0)
    ergebnis3 = berechne_gesamtpreis(WARENKORB_LEER)
    print(f"Test 3 – Leerer Warenkorb: {ergebnis3} (erwartet: 0.0) "
          f"→ {'OK' if ergebnis3 == 0.0 else 'FEHLER'}")

    print("\n=== Unit-Tests ausführen ===")
    unittest.main(verbosity=2, exit=False)
