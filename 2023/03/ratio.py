"""resoud l'enigme du jour 3 partie 2"""

def retrouve_nbr(text, x, y) :
    """retrouve le nombre associé a une position (x, y)"""
    i = 0
    while i<=y and "0"<=text[x][y+i]<="9":
        i = i-1
    i += 1
    nbr = 0
    while y+i<len(text[x]) and "0"<=text[x][y+i]<="9" :
        nbr = nbr*10+int(text[x][y+i])
        i += 1
    return nbr


def calcule(text) :
    """tcalcule"""
    somme = 0
    for x in range(len(text)) :
        for y in range(len(text[x])) :
            if text[x][y] == "*" :
                pos_adj = []
                for i in (x-1, x, x+1) :
                    for j in (y-1, y, y+1) :
                        if "0"<=text[i][j]<="9" :
                            if (i, j-1) not in pos_adj and (i, j+1) not in pos_adj :
                                pos_adj.append((i, j))
                            if (x-1, y-1) in pos_adj and (x-1, y+1) in pos_adj and "0"<=text[x-1][y]<="9" :
                                pos_adj.remove((x-1, y+1))
                            if (x+1, y-1) in pos_adj and (x+1, y+1) in pos_adj and "0"<=text[x+1][y]<="9" :
                                pos_adj.remove((x+1, y+1))
                if len(pos_adj) == 2 :
                    prod = 1
                    for (i,j) in pos_adj :
                        prod = prod*retrouve_nbr(text, i, j)
                    somme += prod
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
    print(calcule(text))

main()
