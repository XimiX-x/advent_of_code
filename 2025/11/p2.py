#!/usr/bin/env python3.10

g = {}
nb = {}
with open("input") as file :
    for lines in file :
        line = lines.split()
        g[line[0][:-1]] = line[1:]

def compute(cour, dac, fft) :
    nb[(cour, dac, fft)] = 0
    if cour == "out" :
        nb[(cour, dac, fft)] += int(dac and fft)
    if cour != "out" :
        for suiv in g[cour] :
            match cour :
                case "dac" :
                    if not (suiv, True, fft) in nb.keys() :
                        compute(suiv, True, fft)
                    nb[(cour, dac, fft)] += nb[(suiv, True, fft)]
                case "fft" :
                    if not (suiv, dac, True) in nb.keys() :
                        compute(suiv, dac, True)
                    nb[(cour, dac, fft)] += nb[(suiv, dac, True)]
                case default :
                    if not (suiv, dac, fft) in nb.keys() :
                        compute(suiv, dac, fft)
                    nb[(cour, dac, fft)] += nb[(suiv, dac, fft)]

compute("svr", False, False)
print(nb[('svr', False, False)])
