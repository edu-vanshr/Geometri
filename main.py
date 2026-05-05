"""
Projekt 3b: Geometriska mönster med ASCII
Ett menybaserat program som ritar textbaserade geometriska figurer.

Funktioner som ska implementeras:
- rita_kvadrat(sida, tecken)
- rita_triangel(hojd, tecken)
- rita_cirkel(radie, tecken)
- rita_blomma(kronblad, storlek, tecken)
- huvudprogram() med meny
"""


# === ANSI-FÄRGER ===

class Farger:
    ROD = "\033[91m"
    GRON = "\033[92m"
    GUL = "\033[93m"
    BLA = "\033[94m"
    RESET = "\033[0m"


def valj_farg():
    print("Välj färg:")
    print("1. Röd")
    print("2. Grön")
    print("3. Gul")
    print("4. Blå")
    print("5. Ingen färg")

    val = input("Val: ")

    if val == "1":
        return Farger.ROD
    elif val == "2":
        return Farger.GRON
    elif val == "3":
        return Farger.GUL
    elif val == "4":
        return Farger.BLA
    else:
        return ""


# === FIGURER ===

def rita_kvadrat(sida, tecken, farg=""):
    """
    Ritar en fylld kvadrat.

    Parametrar:
        sida (int): Längden på sidan (antal tecken)
        tecken (str): Tecknet som används för att rita
    """
    for i in range(sida):
        print(farg + (tecken + " ") * sida + Farger.RESET)


def rita_triangel(hojd, tecken, farg=""):
    """
    Ritar en rätvinklig triangel.

    Parametrar:
        hojd (int): Triangelns höjd (antal rader)
        tecken (str): Tecknet som används för att rita
    """
    for i in range(1, hojd + 1):
        print(farg + (tecken + " ") * i + Farger.RESET)


def rita_cirkel(radie, tecken, farg=""):
    """
    Ritar en cirkel med ASCII-tecken.
    Använder Pythagoras sats (x² + y² ≤ r²) för att avgöra om en punkt är innanför.

    Parametrar:
        radie (int): Cirkelns radie
        tecken (str): Tecknet som används för att rita
    """
    for y in range(-radie, radie + 1):
        rad = ""
        for x in range(-radie, radie + 1):
            if x*x + y*y <= radie*radie:
                rad += farg + tecken + " " + Farger.RESET
            else:
                rad += "  "
        print(rad)


def rita_blomma(kronblad, storlek, tecken, farg=""):
    """
    Ritar en enkel blomma genom att kombinera flera kvadrater.

    Parametrar:
        kronblad (int): Antal kronblad
        storlek (int): Storleken på varje kronblad
        tecken (str): Tecknet som används för att rita
    """
    for i in range(kronblad):
        rita_kvadrat(storlek, tecken, farg)
        print(" ")
    print(" " * storlek + "|")


# === HUVUDPROGRAM ===

def huvudprogram():
    """
    Huvudprogrammet som styr menyn och programflödet.
    """
    while True:
        print("\n--- ASCII MÖNSTER ---")
        print("1. Rita kvadrat")
        print("2. Rita triangel")
        print("3. Rita cirkel")
        print("4. Rita blomma")
        print("5. Avsluta")

        val = input("Valj: ")

        if val == "1":
            sida = int(input("Sida: "))
            tecken = input("Tecken (t.ex. *): ")
            farg = valj_farg()
            rita_kvadrat(sida, tecken, farg)

        elif val == "2":
            hojd = int(input("Höjd: "))
            tecken = input("Tecken (t.ex. *): ")
            farg = valj_farg()
            rita_triangel(hojd, tecken, farg)

        elif val == "3":
            radie = int(input("Radie: "))
            tecken = input("Tecken (t.ex. *): ")
            farg = valj_farg()
            rita_cirkel(radie, tecken, farg)

        elif val == "4":
            kronblad = int(input("Antal kronblad: "))
            storlek = int(input("Storlek: "))
            tecken = input("Tecken (t.ex. *): ")
            farg = valj_farg()
            rita_blomma(kronblad, storlek, tecken, farg)

        elif val == "5":
            print("Hej då!")
            break

        else:
            print("Ogiltigt val, försök igen.")


# === EXTRA FUNKTIONER FÖR UTMANINGAR ===

def rita_ihalig_kvadrat(sida, tecken):
    """
    Ritar en ihålig kvadrat (endast kantlinjen).
    """
    for i in range(sida):
        if i == 0 or i == sida - 1:
            print(tecken * sida)
        else:
            print(tecken + " " * (sida - 2) + tecken)


def rita_omvand_triangel(hojd, tecken):
    """
    Ritar en omvänd triangel (basen upp, spetsen ner).
    """
    # TODO: Implementera funktionen
    # Tips: for i in range(hojd, 0, -1): print(tecken * i)
    pass


def rita_diamant(hojd, tecken):
    """
    Ritar en diamant (två trianglar som möts).
    """
    # TODO: Implementera funktionen
    # Tips: Först en triangel uppåt, sedan en nedåt (utan mittenraden två gånger)
    pass


def spara_till_fil(figur_namn, innehall, filnamn="figur.txt"):
    """
    Sparar en ASCII-figur till en textfil.

    Parametrar:
        figur_namn (str): Namn på figuren
        innehall (str): Figurens textinnehåll
        filnamn (str): Namn på filen att spara till
    """
    # TODO: Implementera funktionen
    # Tips: Använd filhantering från projekt 1
    pass


# Starta programmet om filen körs direkt
if __name__ == "__main__":
    huvudprogram()