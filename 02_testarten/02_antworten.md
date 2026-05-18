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