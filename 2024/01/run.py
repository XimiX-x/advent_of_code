list1 = []
list2 = []

with open("input.txt", mode = 'r', encoding = 'utf8') as file:
    for lines in file :
        line = lines.split()
        list1.append(int(line[0]))
        list2.append(int(line[1]))

list1.sort()
list2.sort()

summ = 0
for i, elem in enumerate(list1) :
    summ += abs(elem-list2[i])

print(summ)
