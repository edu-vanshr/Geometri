"""
Projekt 3b: Geometriska mönster med ASCII
Ett menybaserat program som ritar textbaserade geometriska figurer.
"""


# === ANSI-FÄRGER ===


class Farger:
    # ANSI-koder används för att färgsätta text i terminalen
    ROD = "\033[91m"
    GRON = "\033[92m"
    GUL = "\033[93m"
    BLA = "\033[94m"
    RESET = "\033[0m"  # Återställer färgen efter utskrift


def valj_farg():
    """
    Låter användaren välja färg från en meny.
    Returnerar en ANSI-kod som används i utskriften.
    """

    print("Välj färg:")
    print("1. Röd")
    print("2. Grön")
    print("3. Gul")
    print("4. Blå")
    print("5. Ingen färg")

    val = input("Val: ").strip()

    # Returnerar rätt färg beroende på val
    if val == "1":
        return Farger.ROD
    elif val == "2":
        return Farger.GRON
    elif val == "3":
        return Farger.GUL
    elif val == "4":
        return Farger.BLA
    else:
        return ""  # Ingen färg


# === FIGURER ===


# ---------------- KVADRAT ----------------
def rita_kvadrat(sida, tecken, farg=""):
    """
    Ritar en fylld kvadrat.

    sida = storlek på kvadraten
    tecken = symbol som används
    farg = valfri färg
    """

    resultat = ""  # sparar hela figuren som text

    for _ in range(sida):
        # Skapar en rad med lika många tecken som sidan
        rad = farg + (tecken + " ") * sida + Farger.RESET
        print(rad)
        resultat += rad + "\n"

    return resultat

# ---------------- TRIANGEL ----------------
def rita_triangel(hojd, tecken, farg=""):
    """
    Ritar en rätvinklig triangel som växer rad för rad.
    """

    resultat = ""

    for i in range(1, hojd + 1):
        # varje rad får fler tecken än den förra
        rad = farg + (tecken + " ") * i + Farger.RESET
        print(rad)
        resultat += rad + "\n"

    return resultat

# ---------------- OMVÄND TRIANGEL ----------------
def rita_omvand_triangel(hojd, tecken, farg=""):
    """
    Ritar en triangel som minskar rad för rad.
    """

    resultat = ""

    for i in range(hojd, 0, -1):
        # börjar stort och blir mindre
        rad = farg + (tecken + " ") * i + Farger.RESET
        print(rad)
        resultat += rad + "\n"

    return resultat

# ---------------- IHÅLIG KVADRAT ----------------
def rita_ihalig_kvadrat(sida, tecken, farg=""):
    """
    Ritar en kvadrat där bara kanterna syns.
    """

    resultat = ""

    for i in range(sida):

        # första och sista raden är fyllda
        if i == 0 or i == sida - 1:
            rad = farg + tecken * sida + Farger.RESET
        else:
            # mittenrader: kant + tomrum + kant
            rad = farg + tecken + " " * (sida - 2) + tecken + Farger.RESET

        print(rad)
        resultat += rad + "\n"

    return resultat

# ---------------- DIAMANT ----------------
def rita_diamant(hojd, tecken, farg=""):
    """
    Ritar en diamant genom två trianglar:
    - en uppåt
    - en nedåt
    """

    resultat = ""

    # --------------------
    # Övre delen
    # --------------------
    for i in range(1, hojd + 1):

        # centrerar genom mellanslag
        rad = " " * (hojd - i) + (tecken + " ") * i
        rad = farg + rad + Farger.RESET

        print(rad)
        resultat += rad + "\n"

    # --------------------
    # Nedre delen
    # --------------------
    for i in range(hojd - 1, 0, -1):

        rad = " " * (hojd - i) + (tecken + " ") * i
        rad = farg + rad + Farger.RESET

        print(rad)
        resultat += rad + "\n"

    return resultat

# ---------------- CIRKEL ----------------
def rita_cirkel(radie, tecken, farg=""):
    """
    Ritar en cirkel med hjälp av matematik:
    x² + y² ≤ r²
    """

    resultat = ""

    # går igenom y-led (top till botten)
    for y in range(-radie, radie + 1):

        rad = ""

        # går igenom x-led (vänster till höger)
        for x in range(-radie, radie + 1):

            # kollar om punkten är inom cirkeln
            if x*x + y*y <= radie*radie:
                rad += farg + tecken + " " + Farger.RESET
            else:
                rad += "  "  # tom plats utanför cirkeln

        print(rad)
        resultat += rad + "\n"

    return resultat

# ---------------- BLOMMA ----------------
def rita_blomma(kronblad, storlek, tecken, farg=""):
    """
    Ritar en enkel blomma genom att upprepa kvadrater.
    """

    resultat = ""

    for _ in range(kronblad):

        # varje kronblad är en liten kvadrat
        for _ in range(storlek):
            rad = farg + (tecken + " ") * storlek + Farger.RESET
            print(rad)
            resultat += rad + "\n"

        print()  # mellanrum mellan kronblad
        resultat += "\n"

    return resultat


# === HUVUDPROGRAM ===

def huvudprogram():
    """
    Styr hela programmet och visar menyn.
    """

    alla_figurer = []  # sparar alla ritade figurer

    while True:

        # meny
        print("\n--- ASCII MÖNSTER ---")
        print("1. Kvadrat")
        print("2. Triangel")
        print("3. Cirkel")
        print("4. Blomma")
        print("5. Omvänd triangel")
        print("6. Diamant")
        print("7. Ihålig kvadrat")
        print("8. Avsluta")
        print("9. Spara alla figurer")

        val = input("Välj: ")

        # ---------------- KVADRAT ----------------
        if val == "1":
            sida = int(input("Sida: "))
            tecken = input("Tecken: ")
            farg = valj_farg()

            figur = rita_kvadrat(sida, tecken, farg)
            alla_figurer.append(("Kvadrat", figur))

        # ---------------- TRIANGEL ----------------
        elif val == "2":
            hojd = int(input("Höjd: "))
            tecken = input("Tecken: ")
            farg = valj_farg()

            figur = rita_triangel(hojd, tecken, farg)
            alla_figurer.append(("Triangel", figur))

        # ---------------- CIRKEL ----------------
        elif val == "3":
            radie = int(input("Radie: "))
            tecken = input("Tecken: ")
            farg = valj_farg()

            figur = rita_cirkel(radie, tecken, farg)
            alla_figurer.append(("Cirkel", figur))

        # ---------------- BLOMMA ----------------
        elif val == "4":
            kronblad = int(input("Kronblad: "))
            storlek = int(input("Storlek: "))
            tecken = input("Tecken: ")
            farg = valj_farg()

            figur = rita_blomma(kronblad, storlek, tecken, farg)
            alla_figurer.append(("Blomma", figur))

        # ---------------- OMVÄND TRIANGEL ----------------
        elif val == "5":
            hojd = int(input("Höjd: "))
            tecken = input("Tecken: ")
            farg = valj_farg()

            figur = rita_omvand_triangel(hojd, tecken, farg)
            alla_figurer.append(("Omvänd triangel", figur))

        # ---------------- DIAMANT ----------------
        elif val == "6":
            hojd = int(input("Höjd: "))
            tecken = input("Tecken: ")
            farg = valj_farg()

            figur = rita_diamant(hojd, tecken, farg)
            alla_figurer.append(("Diamant", figur))

        # ---------------- IHÅLIG KVADRAT ----------------
        elif val == "7":
            sida = int(input("Sida: "))
            tecken = input("Tecken: ")
            farg = valj_farg()

            figur = rita_ihalig_kvadrat(sida, tecken, farg)
            alla_figurer.append(("Ihålig kvadrat", figur))

        # ---------------- AVSLUT ----------------
        elif val == "8":
            print("Hej då!")
            break

        # ---------------- SPARA ----------------
        elif val == "9":

            if not alla_figurer:
                print("Inga figurer att spara!")
            else:
                filnamn = input("Filnamn: ").strip()
                spara_till_fil(alla_figurer, filnamn)

        else:
            print("Ogiltigt val.")



# === SPARA FIL ===

def spara_till_fil(figurer, filnamn="figur.txt"):
    """
    Sparar alla ritade figurer till en textfil.
    """

    try:
        with open(filnamn, "w", encoding="utf-8") as fil:

            for namn, innehall in figurer:
                fil.write(namn + "\n")
                fil.write(innehall + "\n\n")

        print(f"Figurer sparades i {filnamn}")

    except Exception as e:
        print("Fel vid sparning:", e)


# === START ===
if __name__ == "__main__":
    huvudprogram()