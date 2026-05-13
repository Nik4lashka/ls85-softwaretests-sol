# -*- coding: utf-8-sig -*-
"""
Baustein 07 – Test-Driven Development (TDD)
MUSTERLÖSUNG

TDD-Zyklus: 🔴 RED → 🟢 GREEN → 🔵 REFACTOR → zurück zu RED

Warenkorb-Beispiel zeigt den vollständigen TDD-Prozess.

Ausführen:
    pytest 07_tdd/code/loesung.py -v
"""

import pytest
import string
import random
import math


# ============================================================
# Aufgabe 1 – runden_auf_naechste_fuenf
#
# TDD-Protokoll (wie es in der Realität aussieht):
#
# Zyklus 1:
#   🔴 test_runden_3_ergibt_5 → ROT (Funktion existiert noch nicht)
#   🟢 return 5  (minimaler Code)
#   🔵 Kein Refactoring nötig
#
# Zyklus 2:
#   🔴 test_runden_7_ergibt_10 → ROT (return 5 passt nicht)
#   🟢 return math.ceil(zahl / 5) * 5  (allgemeiner)
#   🔵 Kein Refactoring nötig
#
# Zyklus 3:
#   🔴 test_runden_10_ergibt_10 → GRÜN (Formel passt schon)
#   🟢 Kein Code nötig
#
# Zyklus 4:
#   🔴 test_runden_0_ergibt_0 → GRÜN (0/5*5 = 0)
#
# Zyklus 5:
#   🔴 test_runden_negativ → Verhaltens-Definition nötig!
#      Entscheidung: Negative Zahlen → ValueError
#   🟢 if-Check hinzufügen
# ============================================================

def runden_auf_naechste_fuenf(zahl: int) -> int:
    """
    Rundet eine nicht-negative ganze Zahl auf das nächste Vielfache von 5 auf.

    Warum math.ceil: Wir wollen AUFRUNDEN (nicht kaufmännisch runden).
    math.ceil(3/5) = 1 → 1*5 = 5. math.ceil(10/5) = 2 → 2*5 = 10 (bereits Vielfaches).

    Raises:
        ValueError: Wenn zahl negativ ist.
    """
    if zahl < 0:
        raise ValueError(f"Nur nicht-negative Zahlen erlaubt, war: {zahl}")
    return math.ceil(zahl / 5) * 5


class TestRundenAufNaechsteFuenf:
    """TDD-Testklasse – Tests wurden VOR der Implementierung geschrieben."""

    def test_runden_3_ergibt_5(self):
        """Zyklus 1: Erster Test – hat die Implementierung gestartet."""
        assert runden_auf_naechste_fuenf(3) == 5

    def test_runden_7_ergibt_10(self):
        """Zyklus 2: Hat die allgemeine Formel erzwungen."""
        assert runden_auf_naechste_fuenf(7) == 10

    def test_runden_10_ergibt_10(self):
        """Zyklus 3: Bereits ein Vielfaches von 5 bleibt unverändert."""
        assert runden_auf_naechste_fuenf(10) == 10

    def test_runden_0_ergibt_0(self):
        """Zyklus 4: Sonderfall 0."""
        assert runden_auf_naechste_fuenf(0) == 0

    def test_runden_negativ_wirft_fehler(self):
        """Zyklus 5: Negative Zahlen → ValueError (Verhaltens-Definition im Test!)."""
        with pytest.raises(ValueError):
            runden_auf_naechste_fuenf(-3)

    def test_runden_1_ergibt_5(self):
        """Grenzwert: 1 (knapp über 0) → 5."""
        assert runden_auf_naechste_fuenf(1) == 5

    def test_runden_5_ergibt_5(self):
        """Grenzwert: 5 (untere Grenze nächstes Vielfaches) → 5."""
        assert runden_auf_naechste_fuenf(5) == 5


# ============================================================
# Aufgabe 2 – PasswortGenerator (TDD Praxisprojekt)
#
# TDD-Reihenfolge:
#   Schritt 1: ALLE Tests schreiben (sie sind alle ROT)
#   Schritt 2: Minimale Implementierung bis alle GRÜN
#   Schritt 3: Refactoring (Namen, Duplikate beseitigen)
# ============================================================

class PasswortGenerator:
    """
    Generiert Passwörter mit konfigurierbaren Zeichentypen.

    Die Klasse wurde Schritt für Schritt implementiert, nachdem jeder
    Test rot war. Erst die User Stories 1–6 als Tests, dann Implementierung.
    """

    SONDERZEICHEN = "!@#$%^&*"

    def generate(
        self,
        laenge: int = 12,
        grossbuchstaben: bool = True,
        ziffern: bool = True,
        sonderzeichen: bool = False,
    ) -> str:
        """
        Generates a password with the specified configuration.

        Raises:
            ValueError: Wenn laenge < 8 oder keine Zeichentypen aktiviert.
        """
        # User Story 5: Mindestlänge erzwingen
        if laenge < 8:
            raise ValueError(f"Passwort muss mindestens 8 Zeichen lang sein, war: {laenge}")

        # Zeichenpool zusammenstellen
        pool = list(string.ascii_lowercase)

        if grossbuchstaben:
            pool += list(string.ascii_uppercase)
        if ziffern:
            pool += list(string.digits)
        if sonderzeichen:
            pool += list(self.SONDERZEICHEN)

        # User Story 6: Fehler wenn kein Zeichentyp aktiviert
        if not pool:
            raise ValueError("Mindestens ein Zeichentyp muss aktiviert sein.")

        return "".join(random.choices(pool, k=laenge))


class TestPasswortGenerator:
    """
    TDD-Tests für PasswortGenerator.
    Alle Tests wurden VOR der Implementierung geschrieben!
    """

    @pytest.fixture
    def generator(self):
        return PasswortGenerator()

    # User Story 1: Konfigurierbare Länge
    def test_passwort_hat_korrekte_laenge(self, generator):
        """Das erzeugte Passwort hat exakt die gewünschte Länge."""
        passwort = generator.generate(laenge=16)
        assert len(passwort) == 16

    def test_passwort_standardlaenge_ist_12(self, generator):
        """Ohne Angabe → Standardlänge 12."""
        passwort = generator.generate()
        assert len(passwort) == 12

    # User Story 2: Großbuchstaben
    def test_passwort_mit_grossbuchstaben(self, generator):
        """Mit Großbuchstaben: mindestens ein Großbuchstabe im Passwort."""
        passwort = generator.generate(laenge=20, grossbuchstaben=True)
        assert any(c.isupper() for c in passwort)

    def test_passwort_ohne_grossbuchstaben(self, generator):
        """Ohne Großbuchstaben: kein einziger Großbuchstabe."""
        passwort = generator.generate(
            laenge=100, grossbuchstaben=False, ziffern=False
        )
        assert not any(c.isupper() for c in passwort)

    # User Story 3: Ziffern
    def test_passwort_mit_ziffern(self, generator):
        """Mit Ziffern: mindestens eine Ziffer vorhanden."""
        passwort = generator.generate(laenge=20, ziffern=True)
        assert any(c.isdigit() for c in passwort)

    def test_passwort_ohne_ziffern(self, generator):
        """Ohne Ziffern: keine einzige Ziffer vorhanden."""
        passwort = generator.generate(laenge=100, ziffern=False)
        assert not any(c.isdigit() for c in passwort)

    # User Story 4: Sonderzeichen
    def test_passwort_mit_sonderzeichen(self, generator):
        """Mit Sonderzeichen: mindestens ein Sonderzeichen vorhanden."""
        passwort = generator.generate(laenge=50, sonderzeichen=True)
        assert any(c in PasswortGenerator.SONDERZEICHEN for c in passwort)

    # User Story 5: Mindestlänge
    def test_mindestlaenge_wird_erzwungen(self, generator):
        """Länge 7 → ValueError (unter Mindestlänge 8)."""
        with pytest.raises(ValueError, match="mindestens 8"):
            generator.generate(laenge=7)

    def test_laenge_8_ist_erlaubt(self, generator):
        """Grenzwert: Länge 8 ist die Mindestlänge → kein Fehler."""
        passwort = generator.generate(laenge=8)
        assert len(passwort) == 8

    # User Story 6: Fehlermeldungen
    def test_laenge_null_wirft_fehler(self, generator):
        """Länge 0 → ValueError."""
        with pytest.raises(ValueError):
            generator.generate(laenge=0)


# ============================================================
# Aufgabe 3 – Refactoring unter Tests
#
# Die Funktion verarbeite_bestellung() ist bereits implementiert.
# Nach dem Refactoring müssen ALLE Tests noch grün sein.
#
# Refactoring: Hilfsfunktionen extrahiert, Duplikate beseitigt.
# ============================================================

def _validiere_artikel(artikel: dict) -> None:
    """Hilfsfunktion: Prüft einen einzelnen Artikel auf Vollständigkeit."""
    if "preis" not in artikel:
        raise ValueError(f"Artikel '{artikel.get('name', '?')}' hat keinen Preis")
    if "menge" not in artikel:
        raise ValueError(f"Artikel '{artikel.get('name', '?')}' hat keine Menge")
    if artikel["preis"] < 0:
        raise ValueError("Preis darf nicht negativ sein")
    if artikel["menge"] <= 0:
        raise ValueError("Menge muss positiv sein")


def _berechne_gesamtpreis(artikel_liste: list) -> float:
    """Hilfsfunktion: Berechnet Brutto-Gesamtpreis aller Artikel."""
    return sum(a["preis"] * a["menge"] for a in artikel_liste)


def verarbeite_bestellung(bestellung: dict) -> dict:
    """
    Verarbeitet eine Bestellung und gibt ein Ergebnis-Dict zurück.

    Refactored: Validierungslogik in Hilfsfunktionen ausgelagert.
    Dadurch: Kürzere Funktion, klare Verantwortlichkeiten.
    """
    if not bestellung:
        raise ValueError("Bestellung darf nicht leer sein")
    if "artikel" not in bestellung:
        raise ValueError("Bestellung muss 'artikel' enthalten")
    if not bestellung["artikel"]:
        raise ValueError("Artikelliste darf nicht leer sein")

    for artikel in bestellung["artikel"]:
        _validiere_artikel(artikel)

    gesamtpreis = _berechne_gesamtpreis(bestellung["artikel"])

    rabatt = bestellung.get("rabatt_prozent", 0)
    if not 0 <= rabatt <= 100:
        raise ValueError(f"Rabatt muss zwischen 0 und 100 liegen, war: {rabatt}")

    endpreis = gesamtpreis * (1 - rabatt / 100)

    return {
        "gesamtpreis_brutto": round(gesamtpreis, 2),
        "rabatt_prozent": rabatt,
        "endpreis": round(endpreis, 2),
        "anzahl_artikel": len(bestellung["artikel"]),
    }


class TestVerarbeiteBestellung:
    """Diese Tests sollen nach dem Refactoring noch alle grün sein."""

    def test_normale_bestellung(self):
        bestellung = {
            "artikel": [
                {"name": "USB-Stick", "preis": 9.99, "menge": 2},
                {"name": "Maus",      "preis": 19.99, "menge": 1},
            ]
        }
        ergebnis = verarbeite_bestellung(bestellung)
        assert ergebnis["gesamtpreis_brutto"] == 39.97
        assert ergebnis["endpreis"] == 39.97
        assert ergebnis["anzahl_artikel"] == 2

    def test_bestellung_mit_rabatt(self):
        bestellung = {
            "artikel": [{"name": "Monitor", "preis": 300.00, "menge": 1}],
            "rabatt_prozent": 10,
        }
        ergebnis = verarbeite_bestellung(bestellung)
        assert ergebnis["endpreis"] == 270.00

    def test_leere_bestellung_wirft_fehler(self):
        with pytest.raises(ValueError):
            verarbeite_bestellung({})

    def test_negativer_preis_wirft_fehler(self):
        with pytest.raises(ValueError, match="negativ"):
            verarbeite_bestellung({
                "artikel": [{"name": "Fehler", "preis": -5.00, "menge": 1}]
            })

    def test_ungültiger_rabatt_wirft_fehler(self):
        with pytest.raises(ValueError, match="Rabatt"):
            verarbeite_bestellung({
                "artikel": [{"name": "Artikel", "preis": 10.00, "menge": 1}],
                "rabatt_prozent": 150,
            })


# ============================================================
# Aufgabe 4 – IHK: berechne_zinsen (TDD)
#
# TDD-Reihenfolge:
#   1. Tests schreiben (alle ROT)
#   2. Funktion implementieren (alle GRÜN)
#   3. Refactoring (Namen verbessern, Duplikate entfernen)
# ============================================================

def berechne_zinsen(kapital: float, zinssatz: float, jahre: int) -> float:
    """
    Berechnet den Endwert bei Zinseszins: Kapital * (1 + Zinssatz/100) ^ Jahre.

    Raises:
        ValueError: Wenn kapital <= 0, zinssatz < 0 oder jahre < 0.
    """
    if kapital <= 0:
        raise ValueError(f"Kapital muss positiv sein, war: {kapital}")
    if zinssatz < 0:
        raise ValueError(f"Zinssatz darf nicht negativ sein, war: {zinssatz}")
    if jahre < 0:
        raise ValueError(f"Jahre darf nicht negativ sein, war: {jahre}")

    return round(kapital * (1 + zinssatz / 100) ** jahre, 2)


class TestBerechneZinsen:
    """
    TDD: Tests wurden VOR der Implementierung von berechne_zinsen geschrieben.
    """

    def test_normalfall_10_prozent_1_jahr(self):
        """1000 € bei 10% für 1 Jahr → 1100 €."""
        assert berechne_zinsen(1000, 10, 1) == 1100.00

    def test_zinseszins_ueber_mehrere_jahre(self):
        """1000 € bei 10% für 2 Jahre → 1210 € (Zinseszins-Effekt)."""
        assert berechne_zinsen(1000, 10, 2) == 1210.00

    def test_nullzins(self):
        """0% Zinssatz → Kapital bleibt unverändert."""
        assert berechne_zinsen(500, 0, 5) == 500.00

    def test_null_jahre(self):
        """0 Jahre → Startkapital wird zurückgegeben."""
        assert berechne_zinsen(1000, 5, 0) == 1000.00

    def test_negatives_kapital_wirft_fehler(self):
        """Negativem Kapital → ValueError."""
        with pytest.raises(ValueError, match="positiv"):
            berechne_zinsen(-100, 5, 1)

    def test_negativer_zinssatz_wirft_fehler(self):
        """Negativer Zinssatz → ValueError."""
        with pytest.raises(ValueError, match="negativ"):
            berechne_zinsen(1000, -5, 1)

    def test_negative_jahre_wirft_fehler(self):
        """Negative Jahre → ValueError."""
        with pytest.raises(ValueError, match="negativ"):
            berechne_zinsen(1000, 5, -1)
