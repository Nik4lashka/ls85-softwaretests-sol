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
| AK4 | 4 | abc  | Ungültig   |

**(b)** Ergänze die Tabelle um Grenzwerttestfälle:

| GW-Nr | Grenzwert | Erwartetes Ergebnis |
|-------|-----------|---------------------|
| GW1 | 0 | Ungültig    |
| GW2 | 1 | Gültig      |
| GW3 | 999  | Gültig   |
| GW4 | 1000 | Ungültig |
| GW5 | -1 | Ungültig   |


## Aufgabe 2 – Äquivalenzklassen für Passwortstärke

**(a)** Erstelle die Äquivalenzklassentabelle für alle vier Regeln kombiniert.
Hinweis: Jede Regel erzeugt eigene gültige/ungültige Klassen!

| AK-Nr | Klasse | Repräsentativer Wert | Gültig / Ungültig |
|-------|--------|---------------------|-------------------|
| AK1 | Länge zu kurz/lang | 123 | Ungültig |
| AK2 | Länge passt | Test1234 | Gültig |
| AK3 | Enthält keinen Großbuchstaben  | test1234 | Ungültig |
| AK4 | Enthält Großbuchstaben | Test1234 | Gültoig |
| AK5 | Enthält keine Ziffer | TestTest | Ungültig |
| AK6 | Enthält eine Ziffer | Test1234 | Gültig |
| AK7 | Enthält ein Leerzeichen | Test 1234 | Ungültig |
| AK8 | Enthält kein Leerzeichen | Test1234 | Gültig |


## Aufgabe 3 – Grenzwertanalyse: Altersverifikation

**(a)** Bestimme alle Grenzwerte und erstelle eine Grenzwerttabelle mit:
- Unterer Grenzwert der Klasse
- Wert genau an der Grenze
- Oberer Grenzwert der Klasse

| GW-Nr | Grenzwert | oberer wert | unterer wert |
|-------|-----------|---------------------|
| GW1 | 11/0 | 12 | -1 |
| GW2 | 12/17 | 18 | 11 |
| GW3 | 18 | / | 17 |


**(b)** Welche Fälle würden erfahrene Tester zusätzlich einbeziehen?
(Denke an ungültige Werte wie negative Zahlen, 0, 150, Kommazahlen)

- Negative Zahlen, unrealistische Alter


## Aufgabe 4 – IHK-Stil

**(a)** Ermitteln Sie alle Äquivalenzklassen (gültige und ungültige).

ÄK1: 0-29   | 6
ÄK2: 30-49  | 5
ÄK3: 50-66  | 4
ÄK4: 67-80  | 3
ÄK5: 81-91  | 2
ÄK6: 92-100 | 1
ÄK71: x < 0         | ungültig
ÄK8: x > 100        | ungültig
ÄK9: keine ganzzahl | ungültig


**(b)** Erstellen Sie eine vollständige Grenzwerttabelle für alle Notengrenzen.

0

29 30

49 50

66 67

80 81

91 92

100

**(c)** Welche Eingabewerte würden Sie als Tester wählen, um mit möglichst wenigen Testfällen alle Klassen und Grenzwerte abzudecken? Begründen Sie Ihre Wahl.
-1
0
29
30
49
50
66
67
80
81
91
92
100
101
22,5

Damit sind alle ÄK abgedeckt