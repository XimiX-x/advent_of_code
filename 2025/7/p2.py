#!/usr/bin/env python3.10

res = 0
beam = {}
arriving = set()

with open("inpput") as file :
    for lines in file :
        line = lines.split()[0]
        if not beam :
            for i, c in enumerate(line) :
                if c == 'S' :
                    beam[i] = 1
                    arriving.add(i)
        else :
            new_beam = {}
            new_arriving = set()
            for arr in arriving :
                if line[arr] == '^' :
                    if arr > 0 :
                        new_arriving.add(arr-1)
                        if arr-1 in new_beam.keys() :
                            new_beam[arr-1] += beam[arr]
                        else :
                            new_beam[arr-1] = beam[arr]
                    if arr < len(line) :
                        new_arriving.add(arr+1)
                        if arr+1 in new_beam.keys() :
                            new_beam[arr+1] += beam[arr]
                        else :
                            new_beam[arr+1] = beam[arr]
                else :
                    new_arriving.add(arr)
                    if arr in new_beam.keys() :
                        new_beam[arr] += beam[arr]
                    else :
                        new_beam[arr] = beam[arr]
            beam = new_beam
            arriving = new_arriving

for keys in arriving :
    res += beam[keys]
print(res)

### Again !

import pygame
from time import sleep

pygame.init()
screen = pygame.display.set_mode((1750, 1000))

pygame.font.init()
my_font = pygame.font.SysFont('arial', 15)

def animate() :
    input = "inpput"
    res = 0
    beam = {}
    sep = set()
    arriving = set()
    nb_path = {}
    mapp = [list(line.split()[0]) for line in open(input)]
    col_bar = [(255, 0, 255), (0, 0, 255), (0, 255, 255), (0, 255, 0), (255, 255, 0), (255, 0, 0)]

    def display(k) :
        for j, line in enumerate(mapp) :
            delta_y = max(0, k-75)
            for i, c in enumerate(line) :
                if c == 'S' :
                    col = (0, 255, 0)
                elif c == '|' :
                    col = col_bar[(nb_path[(j, i)]-1)%len(col_bar)]
                elif c == '^' :
                    if (j, i) in sep:
                        col = (255, 0, 0)
                    else :
                        col = (255, 255, 255)
                else :
                    col = (0, 0, 0)
                text = my_font.render(c, False, col)
                if c == '^' :
                    screen.blit(text, (20+i*12-2, 10+(j-delta_y)*12+7))
                elif c == 'S' :
                    screen.blit(text, (20+i*12-3, 10+(j-delta_y)*12))
                else :
                    screen.blit(text, (20+i*12, 10+(j-delta_y)*12))

    def display_res() :
        text = my_font.render(f"Result : {res}", False, (255, 255, 255))
        screen.blit(text, (800, 950))
    
    with open(input) as file :
        j = 0
        for lines in file :
            for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            return False
                        if event.type == pygame.KEYDOWN :
                            if event.key == pygame.K_ESCAPE :
                                return False
            line = lines.split()[0]
            if not beam :
                for i, c in enumerate(line) :
                    if c == 'S' :
                        beam[i] = 1
                        arriving.add(i)
            else :
                new_beam = {}
                new_arriving = set()
                for arr in arriving :
                    if line[arr] == '^' :
                        sep.add((j, arr))
                        if arr > 0 :
                            new_arriving.add(arr-1)
                            if arr-1 in new_beam.keys() :
                                new_beam[arr-1] += beam[arr]
                            else :
                                new_beam[arr-1] = beam[arr]
                            nb_path[(j, arr-1)] = new_beam[arr-1]
                        if arr < len(line) :
                            new_arriving.add(arr+1)
                            if arr+1 in new_beam.keys() :
                                new_beam[arr+1] += beam[arr]
                            else :
                                new_beam[arr+1] = beam[arr]
                            nb_path[(j, arr+1)] = new_beam[arr+1]
                    else :
                        new_arriving.add(arr)
                        if arr in new_beam.keys() :
                            new_beam[arr] += beam[arr]
                        else :
                            new_beam[arr] = beam[arr]
                        nb_path[(j, arr)] = beam[arr]
                beam = new_beam
                arriving = new_arriving
                for pos in arriving :
                    mapp[j][pos] = '|'
            screen.fill((0,0,0))
            display(j)
            pygame.display.update()
            j += 1
        for keys in arriving :
            res += beam[keys]
        screen.fill((0,0,0))
        display(j)
        display_res()
        pygame.display.update()
    return True

run = True

while run :
    run = animate()
    if run :
        sleep(1)

pygame.quit()
