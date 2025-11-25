"""resoud l'enigme du jour 2 partie 2"""

def decoupe_ligne(line) :
    """decoupe la ligne"""
    ligne_cour = ""
    for x in line :
        if x in (":", ";", "\n") :
            yield ligne_cour
            ligne_cour = ""
        else :
            ligne_cour += x
    yield ligne_cour

def traite_ligne(line) :
    """traite la kigne"""
    min_number = {"green":0, "red":0, "blue":0}
    text = next(line)
    text = next(line, None)
    while text is not None and text != "":
        nbr = 0
        color = ""
        for x in text :
            if "0"<=x<="9" :
                nbr = nbr*10+int(x)
            elif x not in (" ", ",", ";") :
                color += x
            elif x in (",", ";"):
                if min_number[color] < nbr :
                    min_number[color] = nbr
                nbr = 0
                color = ""
        if min_number[color]<nbr :
            min_number[color] = nbr
        text = next(line, None)
    return min_number["green"]*min_number["blue"]*min_number["red"]

def main() :
    """traite le probleme"""
    file = open("input", encoding = "utf-8", mode = "r")
    somme = 0
    for line in file :
        somme += traite_ligne(decoupe_ligne(line))
    file.close()
    print(somme)

main()
