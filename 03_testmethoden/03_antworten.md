## Aufgabe 0 – Grundbegriffe: Black-Box vs. White-Box

**(a)** Erkläre in eigenen Worten (ohne Nachschauen):
- Was ist der grundlegende Unterschied zwischen Black-Box- und White-Box-Test?
- Welche Frage stellt der Tester beim Black-Box-Test?
- Welche Frage stellt der Tester beim White-Box-Test?

- Bei BlackBox ist der Quellcode nicht bekannt, bei WhiteBox schon.

- Was ist das Ergebnis bei der Eingabe?

- Liefert mein Code bei den folgenden Eingaben das richtige Ergebnis?


**(b)** Ordne die folgenden Situationen zu (Black-Box oder White-Box):

| Situation | Methode |
|-----------|---------|
| Ein Kunde testet, ob er sich einloggen kann | Black-Box |
| Ein Entwickler prüft, ob alle if-Zweige durchlaufen werden | White-Box |
| Ein Tester gibt verschiedene Passwörter ein und schaut, was passiert | Black-Box |
| Ein Entwickler misst die Testabdeckung (Coverage) | White-Box |
| Ein externes Testteam prüft das System gegen die Spezifikation | Black-Box |


**(c)** Erkläre in einem Satz, warum es sinnvoll ist, beide Methoden zu kombinieren.

Es ist sinnvoll beide Methoden zu kombinieren, da man dadurch sowohl die Funktionalität und die Qualität der Softwaren testet.


## Aufgabe 2 – White-Box-Test: Coverage

**(a)** Zeichne den **Kontrollflussgraphen** dieser Funktion auf Papier (oder als ASCII-Art in `03_antworten.md`).
Nummeriere alle Knoten (Anweisungen) und alle Kanten (Bedingungszweige).

1.            if betrag <= 0 -- 2. -- return "UNGUELTIG"
                 |
                 |
3.         if ist_neukunde -- 4. -- prioritaet = "HOCH"
                 |
                 |
5.        prioritaet = "NORMAL"
                 |
                 |
6.        if gutscheincode = "VIP2024" -- 7. -- prioritaet = "HOCH"
                 |
                 |
8.        if betrag >= 500 -- 9. -- if prioritat = "HOCH" -- 10. -- return "EXPRESS"
                                   |
                                   |
11.                            return "PRIORITAET"
                 |
                 |
11.         return prioritaet           


**(b)** **Anweisungsüberdeckung (Statement Coverage):**
Wie viele Testfälle brauchst du mindestens, um jede Anweisung einmal auszuführen?
Erstelle diese Testfälle.

Man braucht 4 Testfälle.

| TC-Nr | Eingabe                        |
| TC01  | betrag = 0, False, ""          |
| TC02  | betrag = 600, True, ""         |
| TC03  | betrag = 600, False, ""        |
| TC04  | betrag = 100, False, "VIP2024" |
