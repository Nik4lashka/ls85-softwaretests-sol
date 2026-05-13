# -*- coding: utf-8-sig -*-
"""
Baustein 06 – pytest
MUSTERLÖSUNG

Zeigt pytest-Stil, Fixtures und parametrisierte Tests.

Installation & Ausführen:
    pip install pytest
    pytest 06_pytest/code/loesung.py -v
"""

import pytest


# ============================================================
# Zu testende Klassen / Funktionen
# ============================================================

class Kontorechner:
    """Aus Baustein 05 – für pytest-Migration."""

    def __init__(self):
        self._kontostand = 0.0

    @property
    def kontostand(self) -> float:
        return self._kontostand

    def einzahlen(self, betrag: float) -> None:
        if betrag <= 0:
            raise ValueError(f"Einzahlung muss positiv sein, war: {betrag}")
        self._kontostand += betrag

    def abheben(self, betrag: float) -> None:
        if betrag <= 0:
            raise ValueError(f"Abhebungsbetrag muss positiv sein, war: {betrag}")
        if betrag > self._kontostand:
            raise ValueError(
                f"Unzureichendes Guthaben: {self._kontostand:.2f} < {betrag:.2f}"
            )
        self._kontostand -= betrag


class BenutzerkontoService:
    """Verwaltung von Benutzerkonten (vereinfacht)."""

    def __init__(self):
        self._benutzer = {}

    def benutzer_anlegen(self, name: str, passwort: str) -> None:
        if name in self._benutzer:
            raise ValueError(f"Benutzer '{name}' existiert bereits.")
        if len(passwort) < 8:
            raise ValueError("Passwort zu kurz (mind. 8 Zeichen).")
        self._benutzer[name] = passwort

    def anmelden(self, name: str, passwort: str) -> bool:
        return self._benutzer.get(name) == passwort

    def benutzer_loeschen(self, name: str) -> None:
        if name not in self._benutzer:
            raise ValueError(f"Benutzer '{name}' nicht gefunden.")
        del self._benutzer[name]

    def benutzeranzahl(self) -> int:
        return len(self._benutzer)


def berechne_note(punkte: int) -> int:
    """Notenberechnung aus Baustein 04."""
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


def validiere_menge(menge) -> bool:
    """Aus Baustein 04."""
    if not isinstance(menge, int):
        return False
    return 1 <= menge <= 999


def berechne_versandkosten(gewicht_kg: float, express: bool = False) -> float:
    """
    Berechnet Versandkosten anhand Gewicht und Express-Option.

    Preistabelle:
        Standard ≤ 5 kg:   3.90
        Standard > 5 kg:   6.90
        Express  ≤ 5 kg:   8.90
        Express  > 5 kg:  14.90

    Raises:
        ValueError: Wenn gewicht_kg <= 0.
        TypeError:  Wenn gewicht_kg kein float/int ist.
    """
    if not isinstance(gewicht_kg, (int, float)):
        raise TypeError(f"gewicht_kg muss numerisch sein, war: {type(gewicht_kg)}")
    if gewicht_kg <= 0:
        raise ValueError(f"Gewicht muss positiv sein, war: {gewicht_kg}")

    if express:
        return 8.90 if gewicht_kg <= 5 else 14.90
    else:
        return 3.90 if gewicht_kg <= 5 else 6.90


# ============================================================
# Aufgabe 1 – Von unittest zu pytest migrieren
#
# Vergleich:
# unittest: Klasse erbt von TestCase, self.assertEqual(...)
# pytest:   Nur Funktion + assert-Anweisung – weniger Boilerplate!
# ============================================================

def test_einzahlen_positiver_betrag():
    """Einzahlung von 100 setzt Kontostand auf 100 (pytest-Stil: kein self!)."""
    konto = Kontorechner()
    konto.einzahlen(100)
    assert konto.kontostand == 100.0


def test_abheben_kein_guthaben():
    """Abhebung ohne Guthaben wirft ValueError (pytest.raises)."""
    konto = Kontorechner()
    with pytest.raises(ValueError):
        konto.abheben(50)


# ============================================================
# Aufgabe 2 – Fixtures
#
# Warum Fixtures: Testvorbereitungs-Code einmal schreiben, in vielen
# Tests wiederverwenden. pytest erzeugt das Fixture für jeden Test neu
# (scope="function"), damit kein Teststatus übertragen wird.
# ============================================================

@pytest.fixture
def kontoservice():
    """
    Fixture: Fertig eingerichteter BenutzerkontoService mit einem Testbenutzer.

    Das Fixture wird für JEDEN Test neu erzeugt (scope="function" ist Standard).
    Dadurch ist jeder Test isoliert – Änderungen in Test A beeinflussen Test B nicht.
    """
    service = BenutzerkontoService()
    service.benutzer_anlegen("testuser", "Test1234!")
    return service


def test_anmelden_gueltig(kontoservice):
    """Gültiger Login mit bekanntem Benutzer → True."""
    assert kontoservice.anmelden("testuser", "Test1234!") is True


def test_anmelden_falsches_passwort(kontoservice):
    """Falsches Passwort → False (kein Fehler, nur False)."""
    assert kontoservice.anmelden("testuser", "FalschesPasswort") is False


def test_anmelden_unbekannter_benutzer(kontoservice):
    """Unbekannter Benutzer → False."""
    assert kontoservice.anmelden("unbekannt", "Test1234!") is False


def test_benutzer_doppelt_anlegen_wirft_fehler(kontoservice):
    """Benutzer der schon existiert → ValueError."""
    with pytest.raises(ValueError, match="existiert bereits"):
        kontoservice.benutzer_anlegen("testuser", "AnderesPW1!")


def test_benutzeranzahl_nach_loeschen(kontoservice):
    """Benutzeranzahl sinkt nach Löschen."""
    kontoservice.benutzer_anlegen("zweiter", "Passwort99!")
    assert kontoservice.benutzeranzahl() == 2
    kontoservice.benutzer_loeschen("testuser")
    assert kontoservice.benutzeranzahl() == 1


# ============================================================
# Aufgabe 3 – Parametrisierung: berechne_note
#
# Ohne Parametrisierung bräuchten wir 16+ separate Testfunktionen.
# Mit @pytest.mark.parametrize definieren wir Daten als Tabelle –
# pytest erzeugt daraus automatisch einzelne Testläufe.
# ============================================================

@pytest.mark.parametrize("punkte, erwartete_note", [
    # Alle Notengrenzen (Grenzwertanalyse)
    (100, 1),  # obere Grenze
    (92,  1),  # untere Grenze Note 1
    (91,  2),  # obere Grenze Note 2
    (81,  2),  # untere Grenze Note 2
    (80,  3),  # obere Grenze Note 3
    (67,  3),  # untere Grenze Note 3
    (66,  4),  # obere Grenze Note 4
    (50,  4),  # untere Grenze Note 4
    (49,  5),  # obere Grenze Note 5
    (30,  5),  # untere Grenze Note 5
    (29,  6),  # obere Grenze Note 6
    (0,   6),  # untere Grenze insgesamt
    # Je 1 Vertreter aus der Mitte jeder Klasse
    (96,  1),  # Mitte Note 1
    (85,  2),  # Mitte Note 2
    (73,  3),  # Mitte Note 3
    (58,  4),  # Mitte Note 4
    (40,  5),  # Mitte Note 5
    (15,  6),  # Mitte Note 6
])
def test_berechne_note(punkte, erwartete_note):
    """Parametrisierter Test – pytest generiert 18 einzelne Testläufe."""
    assert berechne_note(punkte) == erwartete_note


# ============================================================
# Aufgabe 3b – Parametrisierung: validiere_menge
# ============================================================

@pytest.mark.parametrize("menge, erwartet", [
    # Gültige Klasse
    (500,  True),   # Repräsentant Mitte
    (1,    True),   # Grenzwert: untere Grenze
    (999,  True),   # Grenzwert: obere Grenze
    # Ungültige Klasse: zu klein
    (0,    False),  # Grenzwert: eine unter Minimum
    (-5,   False),  # Repräsentant negativ
    # Ungültige Klasse: zu groß
    (1000, False),  # Grenzwert: eine über Maximum
    (5000, False),  # Repräsentant weit darüber
    # Ungültige Klasse: falscher Typ
    ("5",  False),
    (1.0,  False),
    (None, False),
])
def test_validiere_menge(menge, erwartet):
    """Parametrisierter Test für validiere_menge – alle Klassen und Grenzwerte."""
    assert validiere_menge(menge) == erwartet


# ============================================================
# Aufgabe 4 – pytest.raises mit match-Parameter
# ============================================================

def test_einzahlung_null_fehlermeldung():
    """Einzahlung von 0 → ValueError mit 'positiv' in der Nachricht."""
    konto = Kontorechner()
    with pytest.raises(ValueError, match="positiv"):
        konto.einzahlen(0)


def test_einzahlung_negativ_fehlermeldung():
    """Einzahlung von -10 → ValueError (match prüft Text der Exception)."""
    konto = Kontorechner()
    with pytest.raises(ValueError, match="positiv"):
        konto.einzahlen(-10)


def test_abhebung_ohne_guthaben_fehlermeldung():
    """Abhebung ohne Guthaben → ValueError mit 'Guthaben' in der Nachricht."""
    konto = Kontorechner()
    with pytest.raises(ValueError, match="Guthaben"):
        konto.abheben(100)


# ============================================================
# Aufgabe 5 – IHK: berechne_versandkosten
# ============================================================

@pytest.mark.parametrize("gewicht, express, erwartet", [
    (3.0,  False,  3.90),  # Standard, leicht
    (7.0,  False,  6.90),  # Standard, schwer
    (3.0,  True,   8.90),  # Express, leicht
    (7.0,  True,  14.90),  # Express, schwer
    # Grenzwerte
    (5.0,  False,  3.90),  # Standard, genau 5 kg
    (5.0,  True,   8.90),  # Express, genau 5 kg
    (5.01, False,  6.90),  # Standard, knapp über 5 kg
    (5.01, True,  14.90),  # Express, knapp über 5 kg
])
def test_berechne_versandkosten_gueltig(gewicht, express, erwartet):
    """Alle gültigen Gewichts-/Express-Kombinationen."""
    assert berechne_versandkosten(gewicht, express) == pytest.approx(erwartet)


def test_versandkosten_negatives_gewicht():
    """Negatives Gewicht → ValueError."""
    with pytest.raises(ValueError, match="positiv"):
        berechne_versandkosten(-1.0)


def test_versandkosten_falscher_typ():
    """String statt Zahl → TypeError."""
    with pytest.raises(TypeError):
        berechne_versandkosten("schwer")
