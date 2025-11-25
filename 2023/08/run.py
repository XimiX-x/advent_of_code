def avance (pos_cour, dire, dico) :
    x = pos_cour
    for d in dire :
        x = dico[x][d]
    return x

def chinois (boucle): 
    a = b = 0
    pos = 0
    while not a or not b :
        if boucle[pos][2] == "Z" :
            a = pos
        if boucle[pos] == boucle[-1] :
            b = len(boucle) - 1 - pos
        pos += 1
    return a, b

def verif(pos) :
    for elem in pos :
        if elem[2] != "Z" :
            return False
    return True

def cherche_pos(liste, elem) :
    for index, x in enumerate(liste) :
        if x == elem :
            return index

def main() :
    dire = []
    dico = {}
    start_pos = []
    with open("input", encoding = "utf-8") as file :
        k = 0
        for line in file  :
            if k == 0 :
                for elem in line :
                    if elem == "L" :
                        dire.append(0)
                    elif elem == "R" :
                        dire.append(1)
            if k > 1 :
                pos = line[0]+line[1]+line[2]
                left = line[7]+line[8]+line[9]
                right = line[12]+line[13]+line[14]
                dico[pos] = (left, right)
                if pos[2] == "A" :
                    start_pos.append(pos)
            k += 1
    boucle = [[] for _ in start_pos]
    for index, pos in enumerate(start_pos) :
        while not pos in boucle[index] :
            boucle[index].append(pos)
            pos = avance(pos, dire, dico)
        boucle[index].append(pos)
    a, b = chinois(boucle[0])
    nb_essai = a
    print(a, b)
    for elem in boucle :
        print(len(elem), elem)
        print()
    pos = [-1 for _ in boucle]
    for index, elem in enumerate(start_pos) :
        boucle[index] = boucle[index][1:]
        pos[index] = (a-1)%(len(boucle[index])-1)
        start_pos[index] = boucle[index][pos[index]]
    while not verif(start_pos) :
        if nb_essai < 160*b :
            print(start_pos)
        nb_essai += b
        for index, elem in enumerate(start_pos) :
            pos[index] = (pos[index]+b)%(len(boucle[index])-1)
            start_pos[index] = boucle[index][pos[index]]
    print(nb_essai*len(dire))

main()
