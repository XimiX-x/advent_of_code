"""resoud l'enigme 1 du jour 4"""

def partitionne(line) :
    """creer un iterable qui crache tous les int"""
    ligne_cour = 0
    numeros = False
    for x in line :
        if numeros :
            if "0"<=x<="9" :
                ligne_cour = ligne_cour*10 + int(x)
            if x == " " and ligne_cour :
                yield ligne_cour
                ligne_cour = 0
            if x == "|" :
                yield x
        if x == ":" :
            numeros = True
    if ligne_cour :
        yield ligne_cour

def calcule_valeur(iterable) :
    """calcule la valeur d'une carte"""
    nbr = next(iterable, None)
    num_gagnant = []
    while nbr != "|" :
        num_gagnant.append(nbr)
        nbr = next(iterable, None)
    nbr = next(iterable, None)
    nbr_gagnant = 0
    while nbr is not None :
        if nbr in num_gagnant :
            nbr_gagnant += 1
        nbr = next(iterable, None)
    if nbr_gagnant :
        return 2**(nbr_gagnant-1)
    return 0

def main() :
    """Calcule les points totaux"""
    file = open("input", encoding = "utf-8", mode = 'r')
    somme = 0
    for lines in file :
        somme += calcule_valeur(partitionne(lines))
    print(somme)
    file.close()

main()
