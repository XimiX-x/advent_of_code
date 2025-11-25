"""resoud l'enigme du jour 3 partie 1"""

def partitione(text) :
    """recupere les nombres"""
    nombre = 0
    debut_nombre = None
    for x in range(len(text)) :
        for y in range(len(text[x])) :
            if "0"<=text[x][y]<="9" :
                if debut_nombre is None :
                    debut_nombre = (x, y)
                nombre = 10*nombre+int(text[x][y])
            else :
                if nombre :
                    yield nombre, debut_nombre, (x,y)
                    nombre = 0
                    debut_nombre = None
    if nombre :
        yield nombre, debut_nombre, (len(text)-1, len(text[-1]-1))

def trie_nombre(iterable, text) :
    """trie les nombres"""
    nbr, dbt, fin = next(iterable, (None, None, None))
    somme = 0
    while nbr is not None :
        valide = False
        for x in range(dbt[0]-1, fin[0]+2) :
            for y in range(dbt[1]-1, fin[1]+1) :
                if 0<=x<len(text) and 0<=y<len(text[x]) :
                    if text[x][y] not in (".", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "\n") :
                        valide = True
        print(nbr, valide, dbt, fin)
        if valide :
            somme += nbr
        nbr, dbt, fin = next(iterable, (None, None, None))
    return somme

def main() :
    """fonction principale"""
    file = open("input", encoding = "utf-8", mode = "r")
    text = []
    k = 0
    for line in file :
        text.append([])
        for x in line :
            text[k].append(x)
        k = k+1
    file.close()
    print(trie_nombre(partitione(text), text))

main()
