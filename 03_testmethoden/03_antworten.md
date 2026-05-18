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


## Aufgabe 3 – Methoden vergleichen 🟡

Fülle die Tabelle aus:

| Merkmal | Black-Box | White-Box |
|---------|-----------|-----------|
| Codekenntnis notwendig? | Nein        | Ja                        |
| Aus wessen Perspektive? | Endanwender | Entwickler                |
| Was wird geprüft? | Funktionalität    | Struktur                  |
| Typische Werkzeuge | Fertige Anwendung testen | Test-Cases und Kontrollflussgraphen |
| Vorteil | Unabhängig vom Code         | Findet innere Logikfehler |
| Nachteil | Interne Fehler werden nicht aufgedeckt | Fehlende Anforderungen werden nicht Aufgedeckt|


## Aufgabe 4 – IHK-Stil

**(a)** Erstellen Sie einen Kontrollflussgraphen für diese Funktion. Benennen Sie alle Knoten und Kanten.

1.      if gewicht_kg <= 0 -- 2. -- ValueError()
              |
              |
3.       if express -- 4. -- if gewicht_kg <= 5 -- 5. -- return 8.90
                                    |
                                    |
6.                              return 14.90 
              |
              |            
7.      if gewicht_gk <= 5 -- 8. -- return 3.90
              |
              |
         return 6.90

**(b)** Wie viele Testfälle sind für eine vollständige **Zweigüberdeckung** erforderlich? Listen Sie diese auf.

Es sind 5 Testfälle notwendig.
1. (0 , true)
2. (2, true)
3. (2, false)
4. (7, true)
5. (7, false)

**(c)** Welche Testfälle würden Sie zusätzlich aus **Black-Box-Sicht** (Grenzwertanalyse) ergänzen?

Kommt erst in Baustein 04 ich lasse das jetzt aus Bequemlichkeit weg :)