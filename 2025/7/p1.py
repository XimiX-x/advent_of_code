#!/usr/bin/env python3.10

res = 0
beam = set()

with open("inpput") as file :
    for lines in file :
        line = lines.split()[0]
        if not beam :
            for i, c in enumerate(line) :
                if c == 'S' :
                    beam.add(i)
        else :
            for i, c in enumerate(line) :
                if c == '^' and i in beam :
                    beam.remove(i)
                    if i >0 :
                        beam.add(i-1)
                    if i < len(line) :
                        beam.add(i+1)
                    res += 1

print(res)

### Let's vizualize !

import pygame
from time import sleep

pygame.init()
screen = pygame.display.set_mode((1900, 1000))

pygame.font.init()
my_font = pygame.font.SysFont('arial', 15)

def animate() :
    input = "inpput"
    res = 0
    beam = set()
    sep = set()
    mapp = [list(line.split()[0]) for line in open(input)]

    def display(k) :
        for j, line in enumerate(mapp) :
            delta_y = max(0, k-75)
            for i, c in enumerate(line) :
                if c in ('S', '|') :
                    col = (0, 255, 0)
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
        text = my_font.render(f"Result : {res}", False, (255, 255, 255))
        screen.blit(text, (50 + len(mapp[0])*12, 50))
    
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
                        beam.add(i)
            else :
                for i, c in enumerate(line) :
                    if c == '^' and i in beam :
                        sep.add((j, i))
                        beam.remove(i)
                        if i >0 :
                            beam.add(i-1)
                        if i < len(line) :
                            beam.add(i+1)
                        res += 1
                for pos in beam :
                    mapp[j][pos] = '|'
            screen.fill((0,0,0))
            display(j)
            pygame.display.update()
            j += 1
    return True

run = True

while run :
    run = animate()
    if run :
        sleep(1)

pygame.quit()
