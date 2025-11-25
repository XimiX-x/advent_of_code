def new(liste) :
    ne = [liste[i]-liste[i-1] for i in range(1, len(liste))]
    for elem in ne :
        if elem != 0 :
            ne.append(new(ne))
            break
    return liste[0]-ne[-1]

def main() :
    seq = []
    with open("input", encoding = "utf-8") as file :
        for line in file :
            seq.append([int(x) for x in line.split()])
    for se in seq :
        for index, elem in enumerate(se) :
            se[index] = int(elem)
        se.append(new(se))
    s = 0
    for se in seq :
        s += se[-1]
    print(s)

main()