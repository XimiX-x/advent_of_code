"""trouve la location la plus proche"""

import math

def crache_donnee() :
    """sort les info du text"""
    file = open("input", encoding = "utf-8", mode = "r")
    donees = ("seed", "soil", "fert", "water", "light", "temp", "humid", "loc")
    k = 0
    ligne_cour = None
    for line in file :
        if len(line)>1 :
            for x in line :
                if "0" <= x <= "9" :
                    if ligne_cour is None :
                        ligne_cour = int(x)
                    else :
                        ligne_cour = 10*ligne_cour + int(x)
                if x in (" ", "\n") and ligne_cour is not None:
                    yield donees[k], ligne_cour
                    ligne_cour = None
                if x == "\n" :
                    yield "end", 0
        else :
            k += 1
    file.close()

def remplis_dico(dico, iterable) :
    """remplis les dico avec les donnees du texte"""
    type_prec = "seed"
    dest_start = 0
    dest = False
    source_start = 0
    source = False
    length = 0
    larg = False
    for donne_type, donnee in iterable :
        if donne_type == "seed" :
            dico["seed"].append(donnee)
        elif donne_type != "end" :
            if not dest :
                dest_start = donnee
                dest = True
            elif not source :
                source_start = donnee
                source =True
            elif not larg :
                larg = True
                length = donnee
        elif type_prec != "end" and type_prec != "seed":
            dest = source = larg = False
            dico[type_prec][source_start] = (dest_start, length)
        type_prec = donne_type

def recherche_dest(dico, elem) :
    """recherche la destination associé a l'element"""
    for k in dico :
        if k <= elem <= dico[k][1] + k :
            return dico[k][0] + elem - k
    return elem

def main() :
    """resoud le probleme"""
    list_seed = []
    dico_seed = {}
    dico_soil = {}
    dico_fertilizer = {}
    dico_water = {}
    dico_light = {}
    dico_temp = {}
    dico_humididty = {}
    dico_type = {"seed": list_seed, "soil" : dico_seed,
                  "fert":dico_soil, "water":dico_fertilizer, "light":dico_water,
                    "temp":dico_light, "humid":dico_temp, "loc":dico_humididty}
    remplis_dico(dico_type, crache_donnee())
    min_loc = math.inf
    for seed in list_seed :
        soil = recherche_dest(dico_seed, seed)
        fert = recherche_dest(dico_soil, soil)
        water = recherche_dest(dico_fertilizer, fert)
        light = recherche_dest(dico_water, water)
        temp = recherche_dest(dico_light, light)
        humid = recherche_dest(dico_temp, temp)
        loc = recherche_dest(dico_humididty, humid)
        if loc < min_loc :
            min_loc = loc
    print(min_loc)

main()
