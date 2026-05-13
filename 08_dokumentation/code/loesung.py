# -*- coding: utf-8-sig -*-
"""
Baustein 08 – Testdokumentation
MUSTERLÖSUNG

Zeigt vollständige Testfalldokumentation, Coverage-Analyse und
die Generierung eines Testprotokolls als CSV-Datei.

Ausführen:
    pytest 08_dokumentation/code/loesung.py -v
    pytest 08_dokumentation/code/loesung.py --cov=08_dokumentation/code/loesung --cov-report=term-missing -v

CSV-Protokoll erzeugen:
    python 08_dokumentation/code/loesung.py
"""

import pytest
import csv
import os
from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional


# ============================================================
# Zu testendes Modul: Lagerbestandsverwaltung
# ============================================================

@dataclass
class Artikel:
    """Repräsentiert einen Lagerartikel mit ID, Name, Preis und Bestand."""

    artikel_id: str
    name: str
    preis: float
    bestand: int = 0

    def __post_init__(self):
        if not self.artikel_id:
            raise ValueError("Artikel-ID darf nicht leer sein.")
        if self.preis < 0:
            raise ValueError("Preis darf nicht negativ sein.")
        if self.bestand < 0:
            raise ValueError("Bestand darf nicht negativ sein.")


class Lager:
    """
    Vereinfachte Lagerverwaltung.

    Verantwortlich für:
    - Anlegen und Löschen von Artikeln
    - Bestandsführung (erhöhen/reduzieren)
    - Kapazitätsüberwachung
    """

    def __init__(self, kapazitaet: int = 1000):
        if kapazitaet <= 0:
            raise ValueError("Kapazität muss positiv sein.")
        self._kapazitaet = kapazitaet
        self._artikel: dict[str, Artikel] = {}

    def artikel_anlegen(self, artikel: Artikel) -> None:
        """Legt einen neuen Artikel an. Raises: ValueError bei Duplikat."""
        if artikel.artikel_id in self._artikel:
            raise ValueError(f"Artikel '{artikel.artikel_id}' existiert bereits.")
        self._artikel[artikel.artikel_id] = artikel

    def bestand_erhoehen(self, artikel_id: str, menge: int) -> None:
        """Erhöht den Bestand. Raises: ValueError/KeyError bei Fehler."""
        if menge <= 0:
            raise ValueError("Menge muss positiv sein.")
        artikel = self._artikel.get(artikel_id)
        if artikel is None:
            raise KeyError(f"Artikel '{artikel_id}' nicht gefunden.")
        gesamtbestand = sum(a.bestand for a in self._artikel.values())
        if gesamtbestand + menge > self._kapazitaet:
            raise ValueError("Lagerkapazität würde überschritten.")
        artikel.bestand += menge

    def bestand_reduzieren(self, artikel_id: str, menge: int) -> None:
        """Reduziert den Bestand. Raises: ValueError wenn Bestand nicht ausreicht."""
        if menge <= 0:
            raise ValueError("Menge muss positiv sein.")
        artikel = self._artikel.get(artikel_id)
        if artikel is None:
            raise KeyError(f"Artikel '{artikel_id}' nicht gefunden.")
        if artikel.bestand < menge:
            raise ValueError(
                f"Unzureichender Bestand: {artikel.bestand} < {menge}"
            )
        artikel.bestand -= menge

    def artikel_suchen(self, artikel_id: str) -> Optional[Artikel]:
        """Gibt den Artikel zurück oder None, wenn nicht vorhanden."""
        return self._artikel.get(artikel_id)

    def gesamtwert(self) -> float:
        """Berechnet den Gesamtwert aller Artikel im Lager."""
        return round(
            sum(a.preis * a.bestand for a in self._artikel.values()), 2
        )

    def artikel_unter_mindestbestand(self, mindestbestand: int) -> list:
        """Gibt alle Artikel zurück, deren Bestand unter dem Minimum liegt."""
        return [a for a in self._artikel.values() if a.bestand < mindestbestand]

    def artikel_loeschen(self, artikel_id: str) -> None:
        """Löscht einen Artikel aus dem Lager."""
        if artikel_id not in self._artikel:
            raise KeyError(f"Artikel '{artikel_id}' nicht gefunden.")
        del self._artikel[artikel_id]

    @property
    def artikel_anzahl(self) -> int:
        """Anzahl verschiedener Artikel im Lager."""
        return len(self._artikel)


# ============================================================
# Aufgabe 1 – Vollständig dokumentierte Testfälle
#
# Jeder Testfall hat:
# - TC-ID (eindeutige Kennung)
# - Titel (kurze Beschreibung)
# - Vorbedingung (was vor dem Test gelten muss)
# - Testeingabe (Daten)
# - Erwartetes Ergebnis
# - Status (wird nach Ausführung eingetragen)
# ============================================================

class TestLagerDokumentiert:
    """
    Aufgabe 1 – Vollständig dokumentierte Testfälle für die Lagerklasse.

    Warum Testfall-Dokumentation wichtig ist:
    - Nachvollziehbarkeit: Wer hat was wann getestet?
    - Grundlage für Abnahmeentscheidungen durch den Auftraggeber
    - Rückverfolgbarkeit: Welche Anforderung wird abgedeckt?
    """

    @pytest.fixture
    def leeres_lager(self):
        """Vorbedingung: Leeres Lager mit 500 Einheiten Kapazität."""
        return Lager(kapazitaet=500)

    @pytest.fixture
    def lager_mit_artikel(self):
        """Vorbedingung: Lager mit zwei vorhandenen Artikeln (A001, A002)."""
        lager = Lager(kapazitaet=500)
        lager.artikel_anlegen(Artikel("A001", "USB-Stick", 9.99, 50))
        lager.artikel_anlegen(Artikel("A002", "Maus", 24.99, 20))
        return lager

    # TC-LAGER-001
    def test_artikel_anlegen_normalfall(self, leeres_lager):
        """
        TC-ID: TC-LAGER-001
        Titel: Artikel anlegen – Normalfall
        Vorbedingung: Leeres Lager
        Testeingabe: Artikel(id='A001', name='USB-Stick', preis=9.99)
        Erwartetes Ergebnis: artikel_anzahl == 1, Artikel abrufbar
        Status: BESTANDEN
        """
        leeres_lager.artikel_anlegen(Artikel("A001", "USB-Stick", 9.99))
        assert leeres_lager.artikel_anzahl == 1
        assert leeres_lager.artikel_suchen("A001") is not None

    # TC-LAGER-002
    def test_artikel_anlegen_duplikat_wirft_fehler(self, lager_mit_artikel):
        """
        TC-ID: TC-LAGER-002
        Titel: Artikel anlegen – Duplikat
        Vorbedingung: Lager mit Artikel A001
        Testeingabe: Nochmals Artikel mit ID 'A001'
        Erwartetes Ergebnis: ValueError
        Status: BESTANDEN
        """
        with pytest.raises(ValueError, match="existiert bereits"):
            lager_mit_artikel.artikel_anlegen(Artikel("A001", "Duplikat", 5.00))

    # TC-LAGER-003
    def test_bestand_erhoehen_normalfall(self, lager_mit_artikel):
        """
        TC-ID: TC-LAGER-003
        Titel: Bestand erhöhen – Normalfall
        Vorbedingung: Lager mit A001 (Bestand 50)
        Testeingabe: bestand_erhoehen('A001', 10)
        Erwartetes Ergebnis: Bestand von A001 == 60
        Status: BESTANDEN
        """
        lager_mit_artikel.bestand_erhoehen("A001", 10)
        artikel = lager_mit_artikel.artikel_suchen("A001")
        assert artikel.bestand == 60

    # TC-LAGER-004
    def test_bestand_reduzieren_normalfall(self, lager_mit_artikel):
        """
        TC-ID: TC-LAGER-004
        Titel: Bestand reduzieren – Normalfall
        Vorbedingung: Lager mit A001 (Bestand 50)
        Testeingabe: bestand_reduzieren('A001', 20)
        Erwartetes Ergebnis: Bestand von A001 == 30
        Status: BESTANDEN
        """
        lager_mit_artikel.bestand_reduzieren("A001", 20)
        artikel = lager_mit_artikel.artikel_suchen("A001")
        assert artikel.bestand == 30

    # TC-LAGER-005
    def test_bestand_reduzieren_unter_null(self, lager_mit_artikel):
        """
        TC-ID: TC-LAGER-005
        Titel: Bestand reduzieren – Unter Null (Grenzwert)
        Vorbedingung: Lager mit A001 (Bestand 50)
        Testeingabe: bestand_reduzieren('A001', 60)  → mehr als vorhanden
        Erwartetes Ergebnis: ValueError
        Status: BESTANDEN
        """
        with pytest.raises(ValueError, match="Unzureichender Bestand"):
            lager_mit_artikel.bestand_reduzieren("A001", 60)

    # TC-LAGER-006
    def test_artikel_suchen_vorhanden(self, lager_mit_artikel):
        """
        TC-ID: TC-LAGER-006
        Titel: Artikel suchen – vorhanden
        Vorbedingung: Lager mit A002 (Maus)
        Testeingabe: artikel_suchen('A002')
        Erwartetes Ergebnis: Artikel-Objekt mit name='Maus'
        Status: BESTANDEN
        """
        artikel = lager_mit_artikel.artikel_suchen("A002")
        assert artikel is not None
        assert artikel.name == "Maus"

    # TC-LAGER-007
    def test_artikel_suchen_nicht_vorhanden(self, lager_mit_artikel):
        """
        TC-ID: TC-LAGER-007
        Titel: Artikel suchen – nicht vorhanden
        Testeingabe: artikel_suchen('X999')
        Erwartetes Ergebnis: None (kein Fehler, nur None!)
        Status: BESTANDEN
        """
        ergebnis = lager_mit_artikel.artikel_suchen("X999")
        assert ergebnis is None

    # TC-LAGER-008
    def test_gesamtwert(self, lager_mit_artikel):
        """
        TC-ID: TC-LAGER-008
        Titel: Gesamtwert berechnen
        Testeingabe: A001 (9.99 * 50 = 499.50) + A002 (24.99 * 20 = 499.80)
        Erwartetes Ergebnis: 999.30
        Status: BESTANDEN
        """
        assert lager_mit_artikel.gesamtwert() == pytest.approx(999.30, abs=0.01)

    # TC-LAGER-009
    def test_kapazitaet_ueberschreitung(self):
        """
        TC-ID: TC-LAGER-009
        Titel: Kapazitätsüberschreitung
        Vorbedingung: Kleines Lager (Kapazität 10)
        Testeingabe: bestand_erhoehen um 15 Einheiten
        Erwartetes Ergebnis: ValueError
        Status: BESTANDEN
        """
        kleines_lager = Lager(kapazitaet=10)
        kleines_lager.artikel_anlegen(Artikel("A001", "Artikel", 1.00, 5))
        with pytest.raises(ValueError, match="Kapazität"):
            kleines_lager.bestand_erhoehen("A001", 10)  # 5 + 10 = 15 > 10

    # TC-LAGER-010
    def test_artikel_unter_mindestbestand(self, lager_mit_artikel):
        """
        TC-ID: TC-LAGER-010
        Titel: Artikel unter Mindestbestand ermitteln
        Testeingabe: mindestbestand=30 (A001 hat 50, A002 hat 20)
        Erwartetes Ergebnis: Nur A002 in der Liste
        Status: BESTANDEN
        """
        ergebnis = lager_mit_artikel.artikel_unter_mindestbestand(30)
        ids = [a.artikel_id for a in ergebnis]
        assert "A002" in ids
        assert "A001" not in ids


# ============================================================
# Aufgabe 3 – Coverage-Tests (fehlende Zweige abdecken)
# ============================================================

class TestLagerCoverage:
    """
    Zusätzliche Tests für Coverage-Lücken.

    Warum Coverage nicht alles ist:
    100% Coverage bedeutet, jede Zeile wurde ausgeführt – nicht, dass
    die Logik korrekt ist. Grenzwerte und kombinierte Bedingungen können
    trotzdem fehlen. Coverage ist ein Werkzeug, kein Qualitätsgarant.
    """

    def test_artikel_loeschen_vorhanden(self):
        """Coverage: artikel_loeschen – Normalfall (Zeile del self._artikel)."""
        lager = Lager()
        lager.artikel_anlegen(Artikel("A001", "Artikel", 5.00))
        lager.artikel_loeschen("A001")
        assert lager.artikel_suchen("A001") is None

    def test_artikel_loeschen_nicht_vorhanden(self):
        """Coverage: artikel_loeschen – KeyError-Zweig."""
        lager = Lager()
        with pytest.raises(KeyError):
            lager.artikel_loeschen("X999")

    def test_bestand_erhoehen_unbekannter_artikel(self):
        """Coverage: bestand_erhoehen – KeyError-Zweig (Artikel nicht vorhanden)."""
        lager = Lager()
        with pytest.raises(KeyError):
            lager.bestand_erhoehen("X999", 5)

    def test_bestand_reduzieren_unbekannter_artikel(self):
        """Coverage: bestand_reduzieren – KeyError-Zweig."""
        lager = Lager()
        with pytest.raises(KeyError):
            lager.bestand_reduzieren("X999", 5)

    def test_artikel_anlegen_negatives_kapazitaet(self):
        """Coverage: Lager.__init__ – ValueError bei Kapazität <= 0."""
        with pytest.raises(ValueError, match="positiv"):
            Lager(kapazitaet=0)

    def test_gesamtwert_leeres_lager(self):
        """Coverage: gesamtwert() mit leerem Lager → 0.0."""
        lager = Lager()
        assert lager.gesamtwert() == 0.0

    def test_artikel_unter_mindestbestand_keine_treffer(self):
        """Coverage: Kein Artikel unter Mindestbestand → leere Liste."""
        lager = Lager()
        lager.artikel_anlegen(Artikel("A001", "Viel", 5.00, 100))
        ergebnis = lager.artikel_unter_mindestbestand(5)
        assert ergebnis == []


# ============================================================
# Aufgabe 5 – IHK Testbericht-Antworten (als Kommentare)
# ============================================================

# (a) Erfolgsquote aus der Beispielausgabe:
#     8 von 11 Tests bestanden → 8/11 * 100 = 72,7%

# (b) Unterschied FAILED vs ERROR:
#     FAILED: Der Test wurde vollständig ausgeführt, aber eine Assertion
#             schlug fehl (z.B. assert ergebnis == 5 → war aber 3).
#             Der getestete Code funktioniert, aber nicht wie erwartet.
#     ERROR:  Der Test konnte nicht vollständig ausgeführt werden, weil
#             eine unerwartete Exception (kein pytest.raises) geworfen
#             wurde. Häufig: Fehler in setUp, importfehler, NameError.

# (c) Testbericht-Tabelle:
# | TC-ID | Titel                              | Status   | Bemerkung                      |
# |-------|------------------------------------|----------|--------------------------------|
# | TC-01 | Artikel anlegen                    | PASSED   | OK                             |
# | TC-02 | Bestand erhöhen                    | PASSED   | OK                             |
# | TC-03 | Bestand reduzieren unter Null      | FAILED   | ValueError wird nicht geworfen |
# | TC-04 | Artikel suchen (vorhanden)         | PASSED   | OK                             |
# | TC-05 | Artikel suchen (nicht vorhanden)   | FAILED   | Gibt Fehler statt None         |
# | TC-06 | Lagerkapazität prüfen              | PASSED   | OK                             |
# | TC-07 | Bericht erstellen                  | ERROR    | ImportError in setup()         |
# | TC-08 | Bestand exportieren                | PASSED   | OK                             |
# | TC-09 | Import aus CSV                     | PASSED   | OK                             |
# | TC-10 | Löschen vorhandener Artikel        | PASSED   | OK                             |
# Abnahmebereit: NEIN – 2 Failures + 1 Error müssen vor Abnahme behoben werden.

# (d) Empfohlene Maßnahmen vor erneuter Abnahme:
# 1. TC-03: Fehlerbehandlung in bestand_reduzieren prüfen/implementieren.
# 2. TC-05: Rückgabewert von artikel_suchen auf None prüfen, kein KeyError.
# 3. TC-07: Import-Fehler in Berichtsmodul beheben, dann Regressionstest.


# ============================================================
# Testprotokoll als CSV generieren
#
# Warum CSV: Einfach in Excel öffenbar, maschinenlesbar, branchenweit üblich
# für Testberichte und Übergabedokumente.
# ============================================================

def testprotokoll_erstellen(ausgabepfad: str = None) -> str:
    """
    Generiert ein Testprotokoll als CSV-Datei.

    Was zur Dokumentation gehört:
    - TC-ID und Titel (Identifikation)
    - Vorbedingung und Eingabe (Reproduzierbarkeit)
    - Erwartetes und tatsächliches Ergebnis (Nachweis)
    - Status und Datum (Rückverfolgbarkeit)
    """
    if ausgabepfad is None:
        ausgabepfad = os.path.join(
            os.path.dirname(__file__), "testprotokoll.csv"
        )

    testfaelle = [
        {
            "tc_id": "TC-LAGER-001",
            "titel": "Artikel anlegen - Normalfall",
            "vorbedingung": "Leeres Lager (Kapazität 500)",
            "eingabe": "Artikel('A001', 'USB-Stick', 9.99)",
            "erwartet": "artikel_anzahl == 1",
            "tatsaechlich": "artikel_anzahl == 1",
            "status": "BESTANDEN",
            "datum": datetime.now().strftime("%Y-%m-%d"),
        },
        {
            "tc_id": "TC-LAGER-002",
            "titel": "Artikel anlegen - Duplikat",
            "vorbedingung": "Lager mit Artikel A001",
            "eingabe": "artikel_anlegen(Artikel('A001', ...))",
            "erwartet": "ValueError",
            "tatsaechlich": "ValueError: 'A001' existiert bereits",
            "status": "BESTANDEN",
            "datum": datetime.now().strftime("%Y-%m-%d"),
        },
        {
            "tc_id": "TC-LAGER-003",
            "titel": "Bestand erhöhen - Normalfall",
            "vorbedingung": "Lager mit A001 (Bestand 50)",
            "eingabe": "bestand_erhoehen('A001', 10)",
            "erwartet": "Bestand == 60",
            "tatsaechlich": "Bestand == 60",
            "status": "BESTANDEN",
            "datum": datetime.now().strftime("%Y-%m-%d"),
        },
        {
            "tc_id": "TC-LAGER-004",
            "titel": "Bestand reduzieren - Normalfall",
            "vorbedingung": "Lager mit A001 (Bestand 50)",
            "eingabe": "bestand_reduzieren('A001', 20)",
            "erwartet": "Bestand == 30",
            "tatsaechlich": "Bestand == 30",
            "status": "BESTANDEN",
            "datum": datetime.now().strftime("%Y-%m-%d"),
        },
        {
            "tc_id": "TC-LAGER-005",
            "titel": "Bestand reduzieren - Unter Null",
            "vorbedingung": "Lager mit A001 (Bestand 50)",
            "eingabe": "bestand_reduzieren('A001', 60)",
            "erwartet": "ValueError",
            "tatsaechlich": "ValueError: Unzureichender Bestand",
            "status": "BESTANDEN",
            "datum": datetime.now().strftime("%Y-%m-%d"),
        },
        {
            "tc_id": "TC-LAGER-006",
            "titel": "Artikel suchen - vorhanden",
            "vorbedingung": "Lager mit A002",
            "eingabe": "artikel_suchen('A002')",
            "erwartet": "Artikel-Objekt, name='Maus'",
            "tatsaechlich": "Artikel-Objekt, name='Maus'",
            "status": "BESTANDEN",
            "datum": datetime.now().strftime("%Y-%m-%d"),
        },
        {
            "tc_id": "TC-LAGER-007",
            "titel": "Artikel suchen - nicht vorhanden",
            "vorbedingung": "Lager mit A001, A002",
            "eingabe": "artikel_suchen('X999')",
            "erwartet": "None",
            "tatsaechlich": "None",
            "status": "BESTANDEN",
            "datum": datetime.now().strftime("%Y-%m-%d"),
        },
        {
            "tc_id": "TC-LAGER-008",
            "titel": "Gesamtwert berechnen",
            "vorbedingung": "Lager mit A001(50 Stk) und A002(20 Stk)",
            "eingabe": "gesamtwert()",
            "erwartet": "999.30",
            "tatsaechlich": "999.30",
            "status": "BESTANDEN",
            "datum": datetime.now().strftime("%Y-%m-%d"),
        },
        {
            "tc_id": "TC-LAGER-009",
            "titel": "Kapazitätsüberschreitung",
            "vorbedingung": "Lager Kapazität 10, A001 mit Bestand 5",
            "eingabe": "bestand_erhoehen('A001', 10)",
            "erwartet": "ValueError",
            "tatsaechlich": "ValueError: Kapazität überschritten",
            "status": "BESTANDEN",
            "datum": datetime.now().strftime("%Y-%m-%d"),
        },
        {
            "tc_id": "TC-LAGER-010",
            "titel": "Artikel unter Mindestbestand",
            "vorbedingung": "A001(50 Stk), A002(20 Stk)",
            "eingabe": "artikel_unter_mindestbestand(30)",
            "erwartet": "[A002]",
            "tatsaechlich": "[A002]",
            "status": "BESTANDEN",
            "datum": datetime.now().strftime("%Y-%m-%d"),
        },
    ]

    felder = ["tc_id", "titel", "vorbedingung", "eingabe",
              "erwartet", "tatsaechlich", "status", "datum"]

    # UTF-8 mit BOM für Excel-Kompatibilität unter Windows
    with open(ausgabepfad, "w", newline="", encoding="utf-8-sig") as csvdatei:
        writer = csv.DictWriter(csvdatei, fieldnames=felder, delimiter=";")
        writer.writeheader()
        writer.writerows(testfaelle)

    return ausgabepfad


if __name__ == "__main__":
    pfad = testprotokoll_erstellen()
    print(f"Testprotokoll erstellt: {pfad}")

    # Ergebnis kurz ausgeben
    with open(pfad, encoding="utf-8-sig") as f:
        print(f.read())
