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

    val = input("Val: ").strip()

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


def rita_ihalig_kvadrat(sida, tecken, farg=""):
    """
    Ritar en ihålig kvadrat (endast kantlinjen).
    """
    for i in range(sida):
        if i == 0 or i == sida - 1:
            print(tecken * sida)
        else:
            print(farg + tecken + " " + "  " * (sida - 2) + tecken + " " + Farger.RESET)


def rita_triangel(hojd, tecken, farg=""):
    """
    Ritar en rätvinklig triangel.

    Parametrar:
        hojd (int): Triangelns höjd (antal rader)
        tecken (str): Tecknet som används för att rita
    """
    for i in range(1, hojd + 1):
        print(farg + (tecken + " ") * i + Farger.RESET)


def rita_omvand_triangel(hojd, tecken, farg=""):
    """
    Ritar en omvänd triangel (basen upp, spetsen ner).
    """
    for i in range(hojd, 0, -1):
        print(farg + (tecken + " ")* i + Farger.RESET)


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


def rita_diamant(hojd, tecken, farg=""):
    """
    Ritar en diamant (två trianglar som möts).
    """
    for i in range(1, hojd + 1):
        mellanslag = " " * (hojd - i)
        rad = (tecken + " ") * i
        print(farg + mellanslag + rad + Farger.RESET)

    for i in range(hojd - 1, 0, -1):
        mellanslag = " " * (hojd - i)
        rad = (tecken + " ")* i
        print(farg + mellanslag + rad + Farger.RESET)

# === SPARA ALLA FIGURER ===

def spara_till_fil(figur_namn, innehall, filnamn="figur.txt"):
    """
    Sparar en ASCII-figur till en textfil.

    Parametrar:
        figur_namn (str): Namn på figuren
        innehall (str): Figurens textinnehåll
        filnamn (str): Namn på filen att spara till
    """
    try:
        with open(filnamn, "w", encoding="utf-8") as fil:
            fil.write(f"{figur_namn}\n")
            fil.write(innehall)
        print(f"Figuren sparades i {filnamn}")
    except Exception as e:
        print("Fel vid sparning:", e)


# === HUVUDPROGRAM ===

def huvudprogram():

    alla_figurer = []

    while True:
        print("\n--- ASCII MÖNSTER ---")
        print("1. Kvadrat")
        print("2. Triangel")
        print("3. Cirkel")
        print("4. Blomma")
        print("5. Diamant")
        print("6. Avsluta")
        print("7. Spara alla figurer")

        val = input("Val: ").strip()

        # === KVADRAT ===
        if val == "1":
            sida = int(input("Sida: "))
            tecken = input("Tecken: ")
            farg = valj_farg()

            print("1. Fylld kvadrat")
            print("2. Ihålig kvadrat")
            val2 = input("Val: ").strip()

            if val2 == "1":
                figur = rita_kvadrat(sida, tecken, farg)
                visa_eller_spara("Fylld kvadrat", figur)

            elif val2 == "2":
                figur = rita_ihalig_kvadrat(sida, tecken, farg)
                visa_eller_spara("Ihålig kvadrat", figur)

        # === TRIANGEL ===
        elif val == "2":
            hojd = int(input("Höjd: "))
            tecken = input("Tecken: ")
            farg = valj_farg()

            print("1. Vanlig triangel")
            print("2. Omvänd triangel")
            val2 = input("Val: ")

            if val2 == "1":
                figur = rita_triangel(hojd, tecken, farg)
                visa_eller_spara("Triangel", figur)

            elif val2 == "2":
                figur = rita_omvand_triangel(hojd, tecken, farg)
                visa_eller_spara("Omvänd triangel", figur)

        # === CIRKEL ===
        elif val == "3":
            radie = int(input("Radie: "))
            tecken = input("Tecken: ")
            farg = valj_farg()

            figur = rita_cirkel(radie, tecken, farg)
            visa_eller_spara("Cirkel", figur)

        # === BLOMMA ===
        elif val == "4":
            kronblad = int(input("Kronblad: "))
            storlek = int(input("Storlek: "))
            tecken = input("Tecken: ")
            farg = valj_farg()

            figur = rita_blomma(kronblad, storlek, tecken, farg)
            visa_eller_spara("Blomma", figur)

        # === DIAMANT ===
        elif val == "5":
            hojd = int(input("Höjd: "))
            tecken = input("Tecken: ")
            farg = valj_farg()

            figur = rita_diamant(hojd, tecken, farg)
            visa_eller_spara("Diamant", figur)

        elif val == "6":
            print("Hej då!")
            break

        else:
            print("Ogiltigt val.")


# Starta programmet om filen körs direkt
if __name__ == "__main__":
    huvudprogram()