"""gagne des courses"""

def genere_data() :
    """genere un dico avec les donnees"""
    file = open("input", encoding = "utf-8", mode = "r")
    dico = {}
    line1 = next(file)
    line2 = next(file)
    time = dist = None
    for i, x in enumerate(line1) :
        y = line2[i]
        if "0"<=x<="9" :
            if time is None :
                time = int(x)
            else :
                time = time*10+int(x)
        if "0"<=y<="9" :
            if dist is None :
                dist = int(y)
            else :
                dist = 10*dist+int(y)
        if (x == y == "\n" or x == y == " ")and time is not None and dist is not None :
            dico[time] = dist
            dist = time = None
    return dico

def nombre_solution(time, dist) :
    """calcule le nombre de lanière de gagner"""
    # on cherche les k tel que k(time-k) - dist > 0
    delta = time**2 - 4*dist
    if delta >= 0 :
        r1 = (time + delta**(1/2))/2
        r2 = (time - delta**(1/2))/2
        if r1 % 1 == 0 and r2 % 1 == 0 :
            return int(r1-r2-1)
        else :
            return int(r1)-int(r2)

def main() :
    """resoud l'enigme"""
    dico = genere_data()
    prod = 1
    for k, val in dico.items() :
        prod = prod * nombre_solution(k, val)
    print(prod)

main()
