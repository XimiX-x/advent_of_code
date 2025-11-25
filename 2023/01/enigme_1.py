"""resoud la première enigme du jour 1"""

number = ("one", "two", "three", "four", "five", "six", "seven", "eight", "nine")
dico = {"1" : 1, "2" : 2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "one":1, "two":2, "three":3, "four":4, "five":5, "six":6, "seven":7, "eight":8, "nine":9}

file = open('enigme_1', encoding = "utf-8", mode = 'r')
indice_debut_mots = 0
k = 0
summ = 0
for lines in file :
    k += 1
    line = [x for x in lines]
    first_digit = last_digit = 0
    indice_ligne = 0
    indice = 0
    word = None
    digit = False
    while indice_ligne < len(line) :
        x = line[indice_ligne]
        if k == 1 :
            print(x, indice, word)
        if "0" <= x <= "9" :
            if not digit :
                first_digit = dico[x]
                digit = True
            last_digit = dico[x]
            word = None
            indice = 0
        elif word is None :
            for i in range(len(number)) :
                if x == number[i][0] :
                    indice = 1
                    word = i
                    indice_debut_mots = indice_ligne
        else :
            if indice == 1 and (word == 1 or word == 2) :
                if x == "w" :
                    word = 1
                    indice = 2
                elif x == "h" :
                    word = 2
                    indice = 2
                else :
                    word = None
                    indice = 0
                    indice_ligne = indice_debut_mots
            elif indice == 1 and (word == 3 or word == 4) :
                if x == "o" :
                    word = 3
                    indice = 2
                elif x == "i" :
                    word = 4
                    indice = 2
                else :
                    word = None
                    indice = 0
                    indice_ligne = indice_debut_mots
            elif indice == 1 and (word == 5 or word == 6) :
                if x == "i" :
                    word = 5
                    indice = 2
                elif x == "e" :
                    word = 6
                    indice = 2
                else :
                    word = None
                    indice = 0
                    indice_ligne = indice_debut_mots
            else :
                if x == number[word][indice] :
                    indice += 1
                    if indice == len(number[word]) :
                        if not digit :
                            first_digit = dico[number[word]]
                            digit = True
                        last_digit = dico[number[word]]
                        indice = 0
                        word = None
                        indice_ligne = indice_debut_mots
                else :
                    word = None
                    indice = 0
                    indice_ligne = indice_debut_mots
        indice_ligne += 1
    if k == 1 :
        print(first_digit*10 + last_digit)
    summ += first_digit*10+last_digit

print(summ)
file.close()
