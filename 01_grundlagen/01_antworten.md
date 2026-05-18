# Aufgabe 4 - IHK-Stil
**(a)** Nennen Sie zwei konkrete Risiken, die durch das Weglassen von Tests entstehen.
1. Fehler in der Software können unerkannt bleiben.
2. Fehler erst später zu finden kann teurer sein als vorher zu testen.

**(b)** Unterscheiden Sie die Begriffe „Defekt" und „Versagen" anhand eines Beispiels aus dem Lagerverwaltungssystem.
Defekt:   Falscher Operator bei Abfrage zum Bestand (z.B. if (Bestand >= 0) statt if (Bestand > 0)).
Versagen: Es wird vorhandener Bestand gemeldet auch wenn der Bestand = 0 ist.

**(c)** Erläutern Sie, warum frühzeitiges Testen (Grundprinzip 3) wirtschaftlich sinnvoll ist. Nutzen Sie das Schlagwort „Rule of Ten".
Ein Fehler kostet nach jeder Phase in der er nicht aufgefallen ist ca. 10x so viel wie in der Phase zuvor. Deshalb ist es wirtschaftlich sinnvoll, frühzeitig zu testen.    