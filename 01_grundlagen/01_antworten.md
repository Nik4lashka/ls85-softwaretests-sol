# Aufgabe 4 - IHK-Stil
**(a)** Nennen Sie zwei konkrete Risiken, die durch das Weglassen von Tests entstehen.

1. Fehler in der Software können unerkannt bleiben.
2. Fehler erst später zu finden kann teurer sein als vorher zu testen.

**(b)** Unterscheiden Sie die Begriffe „Defekt" und „Versagen" anhand eines Beispiels aus dem Lagerverwaltungssystem.

Defekt:   Falscher Operator bei Abfrage zum Bestand (z.B. if (Bestand >= 0) statt if (Bestand > 0)).
Versagen: Es wird vorhandener Bestand gemeldet auch wenn der Bestand = 0 ist.

**(c)** Erläutern Sie, warum frühzeitiges Testen (Grundprinzip 3) wirtschaftlich sinnvoll ist. Nutzen Sie das Schlagwort „Rule of Ten".

Ein Fehler kostet nach jeder Phase in der er nicht aufgefallen ist ca. 10x so viel wie in der Phase zuvor. Deshalb ist es wirtschaftlich sinnvoll, frühzeitig zu testen.    


## Aufgabe 5 – Transfer: Testen bewerten und empfehlen
**(a)** Formuliere eine überzeugende Argumentation (5–8 Sätze) für systematisches Testen.
Nutze mindestens drei der sieben Grundprinzipien und ein reales Beispiel
(Ariane-5, Therac-25, Y2K oder ein eigenes Beispiel aus dem Berufsalltag).

Durch systematisches testen könnten wir Fehler im Produktionsbetrieb vorbeugen. Nur weil es bisher immer gut gegangen ist heißt das nicht, dass es so bleibt. Frühzeitiges Testen spart Geld. Je später ein Fehler auftritt, desto mehr kostet es diesen wieder los zu werden. Außerdem häufen Fehler sich. Wenn wir durch testen einen Fehler finden, ist es wahrscheinlich dass wir an dieser Stelle im Code noch weitere Fehler finden. Wir müssen also nicht zwinged alles Testen. Das ist nämlich nicht möglich. Es gibt zu viele verschiedene Szenarien. Wenn du immer noch nicht überzeugt bist, dann schaue dir den Y2K-Bug an. Dieses Problem kostete mehrere Unternehmen Milliarden Euro.

**(b)** Dein Betrieb entwickelt eine neue Funktion `berechne_urlaubstage(eintrittsdatum, arbeitstage_pro_woche)`.
- Identifiziere einen möglichen Fehler (Error), Defekt (Defect) und ein Versagen (Failure) für diese Funktion.
- Beschreibe die Konsequenzen eines unentdeckten Defekts in einem Lohnabrechnungssystem.

Error:   Entwickler denkt an falsche Urlaubstage berechnung (falsche Formel)
Defect:  Tatsächlicher Fehler in der Formel
Failure: Die berechneten Urlaubstage sind zu hoch / zu niedrig

Ein unenteckter Defekt in einem Lohnabrechnungssystem kann dazu führen dass ein Mitarbeiter zu wenig / zu viel Gehalt ausgezahlt bekommt


**(c)** Bewerte: Ist Grundprinzip 7 ("Keine Fehler = Gutes System") für diesen Fall relevant? Begründe.

Das Prinzip ist immer relevant. Auch wenn es keine Fehler gibt ist die Anwendung sinnlos, wenn sie die Anforderungen nicht erfüllt.