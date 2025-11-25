list1 = []
list2 = []

with open("input.txt", mode = 'r', encoding = 'utf8') as file:
    for lines in file :
        line = lines.split()
        list1.append(int(line[0]))
        list2.append(int(line[1]))

dico = {}
summ = 0
for elem in list1 :
    if not (elem in dico) :
        occ = 0
        for e in list2 :
            if e == elem :
                occ+=1
        dico[elem] = occ
    summ += elem*dico[elem]

print(summ)