"""
Baustein 05 – Python unittest
Startvorlage – bearbeite diese Datei für deine Aufgaben.

Ausführen:
    python -m unittest 05_unittest/code/starter.py -v
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
# Aufgabe 1 – Testklasse für Kontorechner
# ============================================================

class TestKontorechner(unittest.TestCase):

    def setUp(self):
        """Wird vor jeder Testmethode ausgeführt."""
        self.konto = Kontorechner()

    # --- Einzahlen ---

    def test_einzahlen_positiver_betrag(self):
        """TODO: Prüfe, dass eine Einzahlung von 100 den Kontostand auf 100 setzt."""
        self.konto.einzahlen(100)
        self.assertEqual(self.konto._kontostand, 100)

    def test_einzahlen_mehrere_betraege(self):
        """TODO: Prüfe, dass mehrere Einzahlungen korrekt addiert werden."""
        self.konto.einzahlen(100)
        self.konto.einzahlen(50)
        self.assertEqual(self.konto._kontostand, 150)


    def test_einzahlen_null_wirft_fehler(self):
        """TODO: Prüfe, dass Einzahlung von 0 einen ValueError wirft."""
        with self.assertRaises(ValueError):
            self.konto.einzahlen(0)

    def test_einzahlen_negativ_wirft_fehler(self):
        """TODO: Prüfe, dass negativer Betrag einen ValueError wirft."""
        with self.assertRaises(ValueError):
            self.konto.einzahlen(-1)

    # --- Abheben ---

    def test_abheben_guthaben_vorhanden(self):
        """TODO: Einzahlen und dann korrekt abheben."""
        self.konto.einzahlen(100)
        self.konto.abheben(50)
        self.assertEqual(self.konto._kontostand, 50)

    def test_abheben_kein_guthaben(self):
        """TODO: Abhebung ohne Guthaben wirft ValueError."""
        with self.assertRaises(ValueError):
            self.konto.abheben(50)

    def test_abheben_exakt_kontostand(self):
        """TODO: Abhebung des gesamten Kontostands (Grenzfall)."""
        self.konto.einzahlen(100)
        self.konto.abheben(100)
        self.assertEqual(self.konto._kontostand, 0)

    def test_kontostand_anfangswert(self):
        """TODO: Neues Konto hat Kontostand 0."""
        self.assertEqual(self.konto._kontostand, 0)


# ============================================================
# Aufgabe 2 – Einkaufsliste implementieren und testen
# ============================================================

class Einkaufsliste:
    """TODO: Implementiere diese Klasse."""

    def __init__(self):
        pass  # TODO

    def hinzufuegen(self, artikel: str) -> None:
        """Fügt einen Artikel hinzu."""
        pass  # TODO

    def entfernen(self, artikel: str) -> None:
        """
        Entfernt einen Artikel.
        Raises:
            ValueError: Wenn der Artikel nicht vorhanden ist.
        """
        pass  # TODO

    def anzeigen(self) -> list:
        """Gibt alle Artikel als Liste zurück."""
        pass  # TODO

    def ist_leer(self) -> bool:
        """Gibt True zurück, wenn die Liste leer ist."""
        pass  # TODO

    def anzahl(self) -> int:
        """Gibt die Anzahl der Artikel zurück."""
        pass  # TODO


class TestEinkaufsliste(unittest.TestCase):

    def setUp(self):
        """TODO: Erstelle eine neue Einkaufsliste."""
        pass  # TODO: self.liste = Einkaufsliste()

    def tearDown(self):
        """Wird nach jeder Testmethode ausgeführt."""
        print(f"  [tearDown] Test abgeschlossen.")

    def test_neue_liste_ist_leer(self):
        """TODO"""
        pass

    def test_artikel_hinzufuegen(self):
        """TODO"""
        pass

    def test_artikel_entfernen(self):
        """TODO"""
        pass

    def test_nicht_vorhandenen_artikel_entfernen_wirft_fehler(self):
        """TODO"""
        pass

    def test_anzahl_nach_mehreren_operationen(self):
        """TODO"""
        pass


# ============================================================
# Aufgabe 3 – assertRaises Varianten
# ============================================================

# Importiere berechne_note aus Baustein 04 oder kopiere die Funktion hier:

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

    def test_note_1_bei_100_punkten(self):
        self.assertEqual(berechne_note(100), 1)

    def test_note_6_bei_0_punkten(self):
        self.assertEqual(berechne_note(0), 6)

    def test_ungueltige_punkte_negativ(self):
        """TODO: Teste mit -1 – nutze assertRaises als Context Manager."""
        # TODO: Variante 2 (with self.assertRaises(...))
        pass

    def test_ungueltige_punkte_zu_hoch(self):
        """TODO: Teste mit 101 – nutze assertRaises als Callable."""
        # TODO: Variante 1 (self.assertRaises(ValueError, berechne_note, 101))
        pass

    def test_grenzwert_note_2(self):
        """TODO: Teste Grenzwert 91 (letzte Note 2) und 92 (erste Note 1)."""
        # TODO: Deine Implementierung
        pass


# ============================================================
# Einstiegspunkt
# ============================================================

if __name__ == "__main__":
    unittest.main(verbosity=2)
