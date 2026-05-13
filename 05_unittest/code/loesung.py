# -*- coding: utf-8-sig -*-
"""
Baustein 05 – Python unittest
MUSTERLÖSUNG

Zeigt vollständige Testklassen mit setUp/tearDown und verschiedenen
Assertion-Methoden.

Ausführen:
    python -m unittest 05_unittest/code/loesung.py -v
"""

import unittest


# ============================================================
# Zu testende Klasse: Kontorechner
# ============================================================

class Kontorechner:
    """Vereinfachter Kontostand-Manager."""

    def __init__(self):
        self._kontostand = 0.0

    @property
    def kontostand(self) -> float:
        return self._kontostand

    def einzahlen(self, betrag: float) -> None:
        """
        Zahlt einen Betrag ein.
        Raises:
            ValueError: Wenn betrag <= 0.
        """
        if betrag <= 0:
            raise ValueError(f"Einzahlung muss positiv sein, war: {betrag}")
        self._kontostand += betrag

    def abheben(self, betrag: float) -> None:
        """
        Hebt einen Betrag ab.
        Raises:
            ValueError: Wenn betrag <= 0 oder Kontostand unzureichend.
        """
        if betrag <= 0:
            raise ValueError(f"Abhebungsbetrag muss positiv sein, war: {betrag}")
        if betrag > self._kontostand:
            raise ValueError(
                f"Unzureichendes Guthaben: {self._kontostand:.2f} < {betrag:.2f}"
            )
        self._kontostand -= betrag


# ============================================================
# Aufgabe 1 – Vollständige Testklasse für Kontorechner
# ============================================================

class TestKontorechner(unittest.TestCase):
    """
    Testklasse für Kontorechner.

    setUp() stellt sicher, dass jeder Test mit einem frischen Objekt
    startet – kein Teststatus überträgt sich auf den nächsten Test.
    """

    def setUp(self):
        """Wird VOR JEDER Testmethode aufgerufen (nicht nur einmal!)."""
        self.konto = Kontorechner()

    # --- Assertion 1: assertEqual ---

    def test_einzahlen_positiver_betrag(self):
        """Einzahlung erhöht den Kontostand korrekt (assertEqual)."""
        self.konto.einzahlen(100)
        self.assertEqual(self.konto.kontostand, 100.0)

    def test_einzahlen_mehrere_betraege(self):
        """Mehrere Einzahlungen werden addiert (assertEqual)."""
        self.konto.einzahlen(50)
        self.konto.einzahlen(30)
        self.assertEqual(self.konto.kontostand, 80.0)

    # --- Assertion 2: assertRaises (Variante 1: Callable) ---

    def test_einzahlen_null_wirft_fehler_variante1(self):
        """Einzahlung von 0 wirft ValueError – assertRaises als Callable."""
        # Variante 1: Funktion + Argument separat übergeben
        self.assertRaises(ValueError, self.konto.einzahlen, 0)

    # --- Assertion 3: assertRaises (Variante 2: Context Manager) ---

    def test_einzahlen_negativ_wirft_fehler_variante2(self):
        """Negativer Betrag wirft ValueError – assertRaises als Context Manager."""
        # Variante 2: with-Block – empfohlen, weil der Fehlerort klar ist
        with self.assertRaises(ValueError):
            self.konto.einzahlen(-50)

    # --- Assertion 4: assertEqual nach Abheben ---

    def test_abheben_guthaben_vorhanden(self):
        """Abhebung reduziert den Kontostand korrekt."""
        self.konto.einzahlen(200)
        self.konto.abheben(75)
        self.assertEqual(self.konto.kontostand, 125.0)

    def test_abheben_kein_guthaben(self):
        """Abhebung ohne Guthaben wirft ValueError."""
        with self.assertRaises(ValueError):
            self.konto.abheben(100)

    def test_abheben_exakt_kontostand(self):
        """Abhebung des gesamten Kontostands ist erlaubt (Grenzfall)."""
        self.konto.einzahlen(100)
        self.konto.abheben(100)
        self.assertEqual(self.konto.kontostand, 0.0)

    # --- Assertion 5: assertEqual Anfangszustand ---

    def test_kontostand_anfangswert(self):
        """Neues Konto hat Kontostand 0."""
        self.assertEqual(self.konto.kontostand, 0.0)

    # --- Assertion 6: assertTrue / assertFalse ---

    def test_kontostand_nach_einzahlung_positiv(self):
        """Kontostand nach Einzahlung ist größer als 0 (assertTrue)."""
        self.konto.einzahlen(1)
        self.assertTrue(self.konto.kontostand > 0)

    # --- Assertion 7: assertAlmostEqual (für Gleitkommazahlen) ---

    def test_einzahlung_kommazahl(self):
        """Kommazahlen: assertAlmostEqual vermeidet Gleitkomma-Probleme."""
        self.konto.einzahlen(0.1)
        self.konto.einzahlen(0.2)
        # 0.1 + 0.2 ist in Floating Point nicht exakt 0.3!
        # assertEqual würde hier fehlschlagen – assertAlmostEqual nicht.
        self.assertAlmostEqual(self.konto.kontostand, 0.3, places=10)

    # --- Assertion 8: assertIsInstance ---

    def test_kontostand_ist_float(self):
        """Rückgabetyp des Kontostands ist float (assertIsInstance)."""
        self.assertIsInstance(self.konto.kontostand, float)


# ============================================================
# Aufgabe 2 – Einkaufsliste implementieren und testen
# ============================================================

class Einkaufsliste:
    """Einfache Einkaufsliste mit Hinzufügen, Entfernen und Anzeigen."""

    def __init__(self):
        self._artikel = []

    def hinzufuegen(self, artikel: str) -> None:
        """Fügt einen Artikel zur Liste hinzu."""
        self._artikel.append(artikel)

    def entfernen(self, artikel: str) -> None:
        """
        Entfernt den ersten Treffer des Artikels.
        Raises:
            ValueError: Wenn der Artikel nicht in der Liste ist.
        """
        if artikel not in self._artikel:
            raise ValueError(f"Artikel '{artikel}' nicht in der Liste.")
        self._artikel.remove(artikel)

    def anzeigen(self) -> list:
        """Gibt eine Kopie der Artikelliste zurück."""
        return list(self._artikel)

    def ist_leer(self) -> bool:
        """Gibt True zurück, wenn die Liste leer ist."""
        return len(self._artikel) == 0

    def anzahl(self) -> int:
        """Gibt die Anzahl der Artikel zurück."""
        return len(self._artikel)


class TestEinkaufsliste(unittest.TestCase):
    """
    Testklasse für Einkaufsliste.

    setUp() erzeugt vor jedem Test eine frische Einkaufsliste.
    tearDown() zeigt, dass es nach jedem Test aufgerufen wird.
    """

    def setUp(self):
        """Neue Einkaufsliste für jeden Test – kein Zustand übertragen."""
        self.liste = Einkaufsliste()

    def tearDown(self):
        """Wird NACH JEDER Testmethode aufgerufen – hier zur Demonstration."""
        print(f"  [tearDown] Test abgeschlossen. Verbleibende Artikel: "
              f"{self.liste.anzeigen()}")

    def test_neue_liste_ist_leer(self):
        """Frisch erstellte Einkaufsliste ist leer."""
        self.assertTrue(self.liste.ist_leer())
        self.assertEqual(self.liste.anzahl(), 0)

    def test_artikel_hinzufuegen(self):
        """Hinzugefügter Artikel ist danach in der Liste."""
        self.liste.hinzufuegen("Milch")
        self.assertIn("Milch", self.liste.anzeigen())
        self.assertEqual(self.liste.anzahl(), 1)

    def test_artikel_entfernen(self):
        """Artikel kann nach dem Hinzufügen wieder entfernt werden."""
        self.liste.hinzufuegen("Brot")
        self.liste.entfernen("Brot")
        self.assertNotIn("Brot", self.liste.anzeigen())

    def test_nicht_vorhandenen_artikel_entfernen_wirft_fehler(self):
        """Entfernen eines nicht vorhandenen Artikels wirft ValueError."""
        with self.assertRaises(ValueError):
            self.liste.entfernen("Butter")

    def test_anzahl_nach_mehreren_operationen(self):
        """Anzahl stimmt nach Hinzufügen und Entfernen."""
        self.liste.hinzufuegen("Eier")
        self.liste.hinzufuegen("Käse")
        self.liste.hinzufuegen("Joghurt")
        self.liste.entfernen("Käse")
        self.assertEqual(self.liste.anzahl(), 2)

    def test_liste_nach_leerung_leer(self):
        """Liste ist wieder leer, wenn alle Artikel entfernt wurden."""
        self.liste.hinzufuegen("Apfel")
        self.liste.entfernen("Apfel")
        self.assertTrue(self.liste.ist_leer())


# ============================================================
# Aufgabe 3 – Notenberechnung aus Baustein 04
# ============================================================

def berechne_note(punkte: int) -> int:
    """Notenberechnung aus Baustein 04 – hier für Testzwecke."""
    if not isinstance(punkte, int) or punkte < 0 or punkte > 100:
        raise ValueError(f"Punkte müssen zwischen 0 und 100 liegen, war: {punkte}")
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


class TestBerechneNote(unittest.TestCase):
    """Zeigt beide assertRaises-Varianten in der Praxis."""

    def test_note_1_bei_100_punkten(self):
        self.assertEqual(berechne_note(100), 1)

    def test_note_6_bei_0_punkten(self):
        self.assertEqual(berechne_note(0), 6)

    def test_ungueltige_punkte_negativ_context_manager(self):
        """Variante 2 (Context Manager) – empfohlen, Fehlerort klar."""
        with self.assertRaises(ValueError):
            berechne_note(-1)

    def test_ungueltige_punkte_zu_hoch_callable(self):
        """Variante 1 (Callable + Argument) – alternativ, kompakter."""
        self.assertRaises(ValueError, berechne_note, 101)

    def test_grenzwert_note_1_und_2(self):
        """Grenzwerte an der Note-1/Note-2-Grenze (92 vs. 91)."""
        self.assertEqual(berechne_note(92), 1)
        self.assertEqual(berechne_note(91), 2)


# ============================================================
# Einstiegspunkt
# ============================================================

if __name__ == "__main__":
    unittest.main(verbosity=2)
