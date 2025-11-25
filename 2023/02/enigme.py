"""resoud l'enigme du jour 2"""

color_number = {"red" : 12, "green" : 13, "blue": 14}

def decoupe_ligne(line) :
    """decoupe la ligne"""
    ligne_cour = ""
    for x in line :
        if x in (":", ";", "\n") :
            yield ligne_cour
            ligne_cour = ""
        else :
            ligne_cour += x

def traite_ligne(line) :
    """traite la kigne"""
    text = next(line)
    i = len(text)-1
    id_game = ""
    while i>0 and "0"<=text[i]<="9" :
        id_game = text[i] + id_game
        i = i-1
    text = next(line, None)
    while text is not None :
        nbr = 0
        color = ""
        for x in text :
            if "0"<=x<="9" :
                nbr = nbr*10+int(x)
            elif x not in (" ", ",", ";") :
                color += x
            elif x in (",", ";"):
                if color_number[color] < nbr :
                    return None
                nbr = 0
                color = ""
        if color_number[color]<nbr :
            return None
        text = next(line, None)
    return int(id_game)

def main() :
    """traite le probleme"""
    file = open("input", encoding = "utf-8", mode = "r")
    somme = 0
    for line in file :
        id_game = traite_ligne(decoupe_ligne(line))
        if id_game is not None :
            somme += id_game
    file.close()
    print(somme)

main()
