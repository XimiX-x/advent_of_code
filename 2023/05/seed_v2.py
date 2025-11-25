"""trouve la location la plus proche, partie 2"""

import math

def crache_donnee() :
    """sort les info du text"""
    file = open("exemple.txt", encoding = "utf-8", mode = "r")
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
        if ligne_cour :
            yield "loc", ligne_cour
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
    seed_dep = 0
    seed = False
    for donne_type, donnee in iterable :
        if donne_type == "seed" :
            if not seed :
                seed_dep = donnee
                seed = True
            else :
                dico["seed"][seed_dep] = donnee
                seed = False
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

def seed_iterator(dico) :
    """renvoie un iterable sur toute les seeds"""
    for k in dico :
        for i in range(dico[k]) :
            yield k+i

def main() :
    """resoud le probleme"""
    list_seed = {}
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
    for seed_base, length in list_seed.items() :
        print(seed_base, length)
        pos = 0
        while pos < length :
            soil = seed_base + pos
            fert = soil
            water = fert
            light = water
            temp = humid = loc = fert
            for key, couple in dico_seed.items() :
                if key <= seed_base+pos <= couple[1]+key :
                    soil = couple[0] + seed_base+pos - key
                    pos = min(seed_base + length, key+couple[1]) - seed_base
                else :
                    pos += 1
            
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
