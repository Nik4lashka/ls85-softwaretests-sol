# Aufgabe 4 - Regressionstests  
**(a)** Was ist ein Regressionstest? Erkläre mit eigenen Worten.

Erneutes Ausführen bestehender Tests nach Änderungen an den, von dem Test betroffenen Stellen, Teilen des Codes.

**(b)** Welche bestehenden Tests müssten nach der Änderung als Regressionstests erneut ausgeführt werden? Liste mindestens 3 auf.

- Test ohne Rabatt
- Einkauf mit bestehendem Rabatt
- Einkauf mit Mengenrabatt
- Leerer Warenkorb
- Grenzfälle (9 Stück und 10 Stück)

**(c)** Warum ist das automatisierte Ausführen von Regressionstests besonders wertvoll?
Man vergisst es nicht und man hat nach jeder Änderung entweder die Bestätigung dass (für die Testfälle) keine Fehler auftreten oder man findet Fehler.^


# Aufgabe 5 - IHK-Stil
**(a)** Ordnen Sie diese drei Maßnahmen den Teststufen im V-Modell zu.

1. Unit-Test
2. Integrationstest
3. Abnahmetest

**(b)** Nennen Sie eine weitere Teststufe, die im Plan fehlt, und beschreiben Sie, was dort getestet werden sollte.

Systemtest. Dabei wird das Gesamtsytem auf Funktionalität und Qualität geprüft.

**(c)** Das HR-Team meldet beim Abnahmetest, dass Urlaubstage falsch berechnet werden. Auf welcher Teststufe hätte dieser Fehler idealerweise gefunden werden sollen? Begründen Sie.

Idealerweise hätte das Problem bei den Unit-Tests gefunden werden müssen. Da der Fehler wahrscheinlich in einer einzelnen Funktion auftritt hätte man einen Test dafür schreiben müssen.


## Aufgabe 6 – Transfer: Teststrategie analysieren
**(a)** Analysiere kritisch: Welche Teststufen fehlen in diesem Konzept? Benenne sie mit Fachbegriff.

Es fehlen Integrationstests und Systemtest. Ich bin mir nicht sicher ob das als Unit-Test zählt.

**(b)** Beschreibe die konkreten Risiken für jeden fehlenden Test.
Was könnte im Produktivbetrieb passieren?

Durch den Fehlenden Integrationstest könnten Fehler bei der Kommunikation zwischen zwei oder mehreren Objekten unentdeckt bleiben was dazu führen kann dass die Daten nicht richtig weitergegeben werden. Dadurch kann es zu einem Fehler in dem System kommen, der dafür sorgt, dass am Ende falsche Daten in der Zeiterfassung auftreten.

Durch den Fehlenden Systemtest kann es passieren dass die Funktionalität von der Software nicht erfüllt wird. Es kann also sein dass manche Anforderungen gar nicht funktionieren. Es könnte aber auch sein dass die Software sehr langsam ist und das erst beim Abnahmetest auffällt.

**(c)** Entwirf ein verbessertes Testkonzept nach dem V-Modell für diese Software
mit den Modulen: `zeiterfassung.py`, `benutzerverwaltung.py`, `auswertung.py`.
Ordne konkrete Testbeispiele jeder Teststufe zu.

- Entwickler machen Unit-Tests für die einzelnen Funktionen
- Die Module Zeiterfassung, Benutzerverwaltung und Auswertung werden gemeinsam getestet (Integrationstests)
- Systemtest zur überprüfung von Funktionalität und Qualität
- Abnahmetest durch HR-Team

**(d)** Begründe: Wäre ein ausschließlicher Regressionstest nach einer Änderung ausreichend?
Warum oder warum nicht?

Das hängt von dem Ausmaß der Änderung ab. Wenn viele neue Sachen dazu kommen dann braucht es neue Unit-Tests. Wenn aber nur z.B. nur eine Berechnung angepasst wird dann wird der Regressionstest ausreichen.