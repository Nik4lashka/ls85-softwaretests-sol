"""
Baustein 04 – Äquivalenzklassen & Grenzwertanalyse
Startvorlage – bearbeite diese Datei für deine Aufgaben.
"""


# ============================================================
# Aufgabe 1 – Mengenvalidierung
# ============================================================

def validiere_menge(menge) -> bool:
    """
    Prüft, ob eine Bestellmenge gültig ist.

    Regeln:
    - Typ: ganzzahlig
    - Minimum: 1
    - Maximum: 999

    Returns:
        True wenn gültig, False wenn ungültig.
    """
    return (menge >= 1 and menge <= 999)


# ============================================================
# Aufgabe 2 – Passwortprüfung
# ============================================================

def pruefe_passwort(passwort: str) -> bool:
    """
    Prüft, ob ein Passwort den Anforderungen entspricht.

    Regeln:
    - Länge: 8–64 Zeichen
    - Mindestens ein Großbuchstabe
    - Mindestens eine Ziffer
    - Keine Leerzeichen

    Returns:
        True wenn gültig, False wenn ungültig.
    """
    # TODO: Implementiere die Prüflogik
    # Hinweis: str.isupper(), str.isdigit(), ' ' in passwort

    hasUpper  = False
    hasNumber = False 
    hasWhite  = False

    if len(passwort) < 8 or len(passwort) > 64:
        return False

    for char in passwort:
        if char.isupper():
            hasUpper = True

        if char.isdigit():
            hasNumber = True
        
        if char == ' ':
            hasWhite = True

    return hasUpper and hasNumber and not hasWhite


# ============================================================
# Aufgabe 4 – Notenberechnung (IHK-Stil)
# ============================================================

def berechne_note(punkte: int) -> int:
    """
    Gibt die Note (1–6) für eine Punktzahl zurück.

    Skala:
        92–100 → 1
        81–91  → 2
        67–80  → 3
        50–66  → 4
        30–49  → 5
        0–29   → 6

    Raises:
        ValueError: Wenn punkte außerhalb [0, 100] liegt.
    """
    if not 0 <= punkte <= 100:
        raise ValueError("Punktzahl muss zwischen 0 und 100 liegen.")

    if punkte >= 92:
        return 1
    elif punkte >= 81:
        return 2
    elif punkte >= 67:
        return 3
    elif punkte >= 50:
        return 4
    elif punkte >= 30:
        return 5
    else:
        return 6


# ============================================================
# Tests (manuelle Überprüfung)
# ============================================================

if __name__ == "__main__":

    # --- Aufgabe 1: validiere_menge ---
    print("=== Aufgabe 1: validiere_menge ===")

    # Äquivalenzklassen testen:
    # TODO: Gültige Klasse (z. B. menge = 50)
    ergebnis = validiere_menge(50)
    print(f" validiere_menge(50) -> {ergebnis}")
    # TODO: Ungültige Klasse Untergrenze (z. B. menge = 0)
    ergebnis = validiere_menge(0)
    print(f" validiere_menge(0) -> {ergebnis}")
    # TODO: Ungültige Klasse Obergrenze (z. B. menge = 1000)
    ergebnis = validiere_menge(1000)
    print(f" validiere_menge(1000) -> {ergebnis}")

    # Grenzwerte testen:
    # TODO: Grenzwert 0, 1, 999, 1000
    for testfall in [0, 1, 500, 999, 1000, -1, "abc"]:
        try:
            ergebnis = validiere_menge(testfall)
            print(f"  validiere_menge({testfall!r}) → {ergebnis}")
        except Exception as e:
            print(f"  validiere_menge({testfall!r}) → Exception: {e}")

    # --- Aufgabe 2: pruefe_passwort ---
    print("\n=== Aufgabe 2: pruefe_passwort ===")
    testpasswoerter = [
        "Abc12345",       # gültig
        "abc12345",       # kein Großbuchstabe
        "ABCDEFGH",       # keine Ziffer
        "Abc 1234",       # Leerzeichen
        "Ab1",            # zu kurz
        "A" * 64 + "1",  # zu lang
    ]
    for pw in testpasswoerter:
        print(f"  pruefe_passwort({pw!r}) → {pruefe_passwort(pw)}")

    # --- Aufgabe 4: berechne_note ---
    print("\n=== Aufgabe 4: berechne_note ===")
    # Alle Notengrenzen testen (Grenzwertanalyse):
    grenzwerte = [0, 29, 30, 49, 50, 66, 67, 80, 81, 91, 92, 100]
    for p in grenzwerte:
        try:
            print(f"  berechne_note({p}) → {berechne_note(p)}")
        except ValueError as e:
            print(f"  berechne_note({p}) → ValueError: {e}")

    # Ungültige Werte:
    for p in [-1, 101]:
        try:
            print(f"  berechne_note({p}) → {berechne_note(p)}")
        except ValueError as e:
            print(f"  berechne_note({p}) → ValueError: {e}")
