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

### Animation

import pygame
from time import sleep

pygame.init()
screen = pygame.display.set_mode((1900, 1000))

pygame.font.init()
font = pygame.font.SysFont("arial", 20)

def animate() :
    g = {}
    nb_path = {"out" : 1}
    start = "svr"
    prof = {start : 0}
    elem_prof = [1]
    prof_aff_node = {}

    def display_graph(start) :
        M = max(nb_path.values())
        aff_prof = [0 for _ in range(max(prof.values()) + 1)]
        displayed = set()

        q = [start]
        while q :
            node = q.pop()
            prof_aff_node[node] = elem_prof[prof[node]]/2-aff_prof[prof[node]]
            aff_prof[prof[node]] += 1
            if node != "out" :
                i = 0
                for suiv in g[node] :
                    if suiv in nb_path.keys() :
                        temp = nb_path[suiv]/M*255*6 # type: ignore
                    else :
                        temp = 0
                    if temp < 255 :
                        col = (255, 255-temp, 255)
                    elif temp < 255*2 :
                        col = (255-temp/2, 0, 255)
                    elif temp < 255*3 :
                        col = (0, temp/3, 255)
                    elif temp < 255*4 :
                        col = (0, 255, 255-temp/4)
                    elif temp < 255*5 :
                        col = (temp/5, 255, 0)
                    else :
                        col = (255, 255-temp/6, 0)
                    if not suiv in displayed :
                        pygame.draw.line(screen, col, (15 + 55*prof[node], 500 + 30*(prof_aff_node[node])), (15 + 55*prof[suiv], 500 + 30*(elem_prof[prof[suiv]]/2-(aff_prof[prof[suiv]]+i)))) # type: ignore
                        displayed.add(suiv)
                        q.append(suiv)
                        i += 1
                    else :
                        pygame.draw.line(screen, col, (15 + 55*prof[node], 500 + 30*(prof_aff_node[node])), (15 + 55*prof[suiv], 500 + 30*(prof_aff_node[suiv]))) # type: ignore
        for node in prof_aff_node.keys() :
            col = (255, 255, 255)
            if node == start :
                col = (0, 255, 0)
            elif node == "out" :
                col = (255, 0, 0)
            elif node in ("dac", "fft") :
                col = (0, 0,255)
            pygame.draw.circle(screen, col, (15 + 55*prof[node], 500 + 30*(prof_aff_node[node])), 10)

    nb = {}
    def compute(cour, dac, fft) :
        nb[(cour, dac, fft)] = 0
        nb_path[cour] = 0
        if cour == "out" :
            nb[(cour, dac, fft)] += int(dac and fft)
            nb_path[cour] = 1
            screen.fill((0,0,0))
            display_graph(start)
            pygame.display.update()
        if cour != "out" :
            for suiv in g[cour] :
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        return False
                    if event.type == pygame.KEYDOWN :
                        if event.key == pygame.K_ESCAPE :
                            return False
                match cour :
                    case "dac" :
                        if not (suiv, True, fft) in nb.keys() :
                            if not compute(suiv, True, fft) :
                                return False
                        nb[(cour, dac, fft)] += nb[(suiv, True, fft)]
                        nb_path[cour] += nb[(suiv, True, fft)]
                    case "fft" :
                        if not (suiv, dac, True) in nb.keys() :
                            if not compute(suiv, dac, True) :
                                return False
                        nb[(cour, dac, fft)] += nb[(suiv, dac, True)]
                        nb_path[cour] += nb[(suiv, dac, True)]
                    case default :
                        if not (suiv, dac, fft) in nb.keys() :
                            if not compute(suiv, dac, fft) :
                                return False
                        nb[(cour, dac, fft)] += nb[(suiv, dac, fft)]
                        nb_path[cour] += nb[(suiv, dac, fft)]
                screen.fill((0,0,0))
                display_graph(start)
                pygame.display.update()
        return True

    def compute_prof(start, seen = set()) :
        if start != "out" :
            for suiv in g[start] :
                if not suiv in seen :
                    seen.add(suiv)
                    if len(elem_prof) <= prof[start] +1 :
                        elem_prof.append(1)
                    else :
                        elem_prof[prof[start]+1] += 1
                    prof[suiv] = prof[start] + 1
                    compute_prof(suiv, seen)

    with open("input") as file :
        for lines in file :
            line = lines.split()
            g[line[0][:-1]] = line[1:]

    compute_prof(start)
    if not compute(start, False, False) :
        return False
    res = nb_path[start]
    text = font.render(f"Result : {res}", False, (255, 255, 255))
    screen.blit(text, (1700, 50))
    pygame.display.update()
    return True

run = True

while run :
    run = animate()
    if run :
        sleep(1)

pygame.quit()