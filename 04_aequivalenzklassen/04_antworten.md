## Aufgabe 0 – Grundbegriffe: Äquivalenzklassen erkennen

**(a)** Eine Ampel-Steuerung akzeptiert nur Ganzzahlen von 1 bis 5 als Prioritätsstufe.
Benenne ohne viel Nachdenken: Was sind gültige, was ungültige Eingaben?

Gültig  : 1, 2, 3, 4, 5
Ungültig: 0, n >= 6

**(b)** Erkläre in einem Satz, was eine Äquivalenzklasse ist –
so als würdest du es einem Mitschüler ohne IT-Kenntnis erklären.

Eine Äquivalenzklasse ist eine Gruppe von Testwerten, die alle das gleiche Ergebnis erwaten.

**(c)** Nenne je ein Beispiel aus dem Berufsalltag für:
- Eine gültige Äquivalenzklasse
- Eine ungültige Äquivalenzklasse
- Einen Grenzwert, der besonders kritisch sein könnte

- Ein Lagerbestand von 3
- Ein Lagerbestand von -5
- Ein Lagerbestand von 0

## Aufgabe 1 – Äquivalenzklassen für ein Bestellformular

**(a)** Ermittle alle Äquivalenzklassen und trage sie in die Tabelle ein:

| AK-Nr | Klasse | Repräsentativer Wert | Gültig / Ungültig |
|-------|--------|---------------------|-------------------|
| AK1 | 1 | 1500 | Ungültig |
| AK2 | 2 | 500  | Gültig   |
| AK3 | 3 | 0    | Ungültig |
| AK4 | 4 | -500 | Gültig   |

**(b)** Ergänze die Tabelle um Grenzwerttestfälle:

| GW-Nr | Grenzwert | Erwartetes Ergebnis |
|-------|-----------|---------------------|
| GW1 | 0 | Ungültig    |
| GW2 | 1 | Gültig      |
| GW3 | 999  | Gültig   |
| GW4 | 1000 | Ungültig |
| GW5 | -1 | Ungültig   |