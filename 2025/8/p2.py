#!/usr/bin/env python3.10
from math import inf

cluster = []

with open("test") as file :
    for lines in file :
        line = lines.split()[0]
        line = line.split(',')
        cluster.append([(int(line[0]), int(line[1]), int(line[2]))])

pos_reverse = {elem[0] : index for index, elem in enumerate(cluster)}

def dist(i, j) :
    if i == j :
        return inf
    return (i[0]-j[0])**2 + (i[1]-j[1])**2 + (i[2]-j[2])**2

distances = []
for i, elem1 in enumerate(cluster) :
    for j in range(i) :
        distances.append((dist(cluster[j][0], elem1[0]), elem1[0], cluster[j][0]))

distances.sort()

for _, elem1, elem2 in distances :
    i, j = pos_reverse[elem1], pos_reverse[elem2]
    if i != j :
        for elem in cluster[j] :
            pos_reverse[elem] = i
        cluster[i] = cluster[i]+cluster[j] # type: ignore
        if j != len(cluster)-1 :
            cluster[j] = cluster[-1]
            for elem in cluster[j] :
                pos_reverse[elem] = j
        cluster.pop()
    if len(cluster) == 1 :
        print(elem1[0]*elem2[0])
        break

### Animation time !

import pygame
from time import sleep

pygame.init()
screen = pygame.display.set_mode((1200, 1000))

pygame.font.init()
font = pygame.font.SysFont("arial", 15)

points = []
input = "input"

with open(input) as file :
    for lines in file :
        line = lines.split()[0]
        line = line.split(',')
        points.append((int(line[0]), int(line[1]), int(line[2])))

def animate(): 
    connexions = []
    cluster = []

    def display_map() :
        for elem1, elem2 in connexions :
            if input == "input" :
                pygame.draw.line(screen, (0, 255, 0), (20 + elem1[0]/100, elem1[1]/100), (20 + elem2[0]/100, elem2[1]/100))
            else :
                pygame.draw.line(screen, (0, 255, 0), (20 + elem1[0], elem1[1]), (20 + elem2[0], elem2[1]))

        for x, y, z in points :
            if input == "input" :
                pygame.draw.circle(screen, (255, 255,255), (20 + x/100, y/100), 3-z/100000*2)
            else :
                pygame.draw.circle(screen, (255, 255,255), (20 + x, y), 10-z/1000*9)

        if len(cluster) == 1 :
            elem1, elem2 = connexions[-1]
            res = elem1[0]*elem2[0]

            text = font.render(f"Result : {res}", False, (255, 255, 255))
            screen.blit(text, (1050, 20))
            return True
        return False
    
    screen.fill((0,0,0))
    display_map()
    pygame.display.update()
    sleep(0.5)

    with open(input) as file :
        for lines in file :
            line = lines.split()[0]
            line = line.split(',')
            cluster.append([(int(line[0]), int(line[1]), int(line[2]))])

    pos_reverse = {elem[0] : index for index, elem in enumerate(cluster)}

    distances = []
    for i, elem1 in enumerate(cluster) :
        for j in range(i) :
            distances.append((dist(cluster[j][0], elem1[0]), elem1[0], cluster[j][0]))

    distances.sort()

    for _, elem1, elem2 in distances :
        i, j = pos_reverse[elem1], pos_reverse[elem2]
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN :
                if event.key == pygame.K_ESCAPE :
                    return False
        screen.fill((0,0,0))
        if i != j :
            for elem in cluster[j] :
                pos_reverse[elem] = i
            cluster[i] = cluster[i]+cluster[j] # type: ignore
            if j != len(cluster)-1 :
                cluster[j] = cluster[-1]
                for elem in cluster[j] :
                    pos_reverse[elem] = j
            cluster.pop()
            connexions.append((elem1, elem2))
        else :
            if input == "input" :
                pygame.draw.line(screen, (255, 0, 0), (20 + elem1[0]/100, elem1[1]/100), (20 + elem2[0]/100, elem2[1]/100))
            else :
                pygame.draw.line(screen, (255, 0, 0), (20 + elem1[0], elem1[1]), (20 + elem2[0], elem2[1]))

        if display_map() :
            pygame.display.update()
            clock = pygame.time.Clock()
            return True
        pygame.display.update()
        clock = pygame.time.Clock()
        if input == "input" :
            speed = 40
        else :
            speed = 2
        clock.tick(speed)

run = True

while run :
    run = animate()
    if run :
        sleep(1)

pygame.quit()
