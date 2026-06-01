## Aufgabe 0 – Grundbegriffe: Unit-Test lesen und verstehen

**(a)** Was testet jeder dieser Tests? Beschreibe in je einem Satz.

- Prüft ob der Rabatt richtig von dem Preis abgezogen wird
- Prüft ob eine leere BEstellung einen Preis von 0 hat
- Prüft ob ein negativer Rabatt richtig als Fehler gewertet wird

**(b)** Welche Klasse und welche Methoden werden in den Tests verwendet?
Die Klasse Bestellsystem und die dazu gehörigen methoden:
artikel_hinzufuegen()
und
rabatt_setzen()

außerdem wird die Klasse TestBestellsystem (die UnitTest Klasse) verwendet mit den assert Methoden.

**(c)** Was bedeutet `assertAlmostEqual` und warum wird es hier statt `assertEqual` verwendet?

Prüft ob zwei Fließkommazahlen "fast gleich" sind. Wird benutzt um bei rundungsfehlern trotzdem den test zu bestehen

**(d)** Was passiert, wenn `test_negativer_rabatt_wirft_fehler` fehlschlägt?
Was wäre dann das Problem in der Implementierung?

