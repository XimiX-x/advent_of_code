"""resoud l'enigme 2 du jour 4"""

def partitionne(line) :
    """creer un iterable qui crache tous les int"""
    ligne_cour = 0
    for x in line :
        if "0"<=x<="9" :
            ligne_cour = ligne_cour*10 + int(x)
        if x == " " and ligne_cour :
            yield ligne_cour
            ligne_cour = 0
        if x == "|" :
            yield x
    if ligne_cour :
        yield ligne_cour

def calcule_valeur(iterable, dico) :
    """calcule la valeur d'une carte"""
    num_card = next(iterable)
    if num_card in dico :
        dico[num_card] += 1
    else :
        dico[num_card] = 1
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
    for i in range(num_card + 1, num_card + nbr_gagnant +1) :
        if i in dico :
            dico[i] += dico[num_card]
        else :
            dico[i] = dico[num_card]

def main() :
    """Calcule les points totaux"""
    dico = {}
    file = open("input", encoding = "utf-8", mode = 'r')
    somme = 0
    for lines in file :
        calcule_valeur(partitionne(lines), dico)
    for k in dico.items() :
        somme += k[1]
    print(somme)
    file.close()

main()
