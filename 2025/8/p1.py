#!/usr/bin/env python3.10
from math import inf

cluster = []

with open("input") as file :
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

index = 0
_, elem1, elem2 = distances[0]
i, j = pos_reverse[elem1], pos_reverse[elem2]
for _ in range(1000) :
    if i != j :
        for elem in cluster[j] :
            pos_reverse[elem] = i
        cluster[i] = cluster[i]+cluster[j] # type: ignore
        if j != len(cluster)-1 :
            cluster[j] = cluster[-1]
            for elem in cluster[j] :
                pos_reverse[elem] = j
        cluster.pop()
    index += 1
    _, elem1, elem2 = distances[index]
    i, j = pos_reverse[elem1], pos_reverse[elem2]

cluster = list(map(lambda x: len(x), cluster))
cluster.sort(reverse= True)
res = cluster[0]*cluster[1]*cluster[2]

print(res)

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

        if cluster :
            lengths = list(map(lambda x: len(x), cluster))
            lengths.sort(reverse= True)
            res = lengths[0]*lengths[1]*lengths[2]
        else :
            res = 1

        text = font.render(f"Result : {res}", False, (255, 255, 255))
        screen.blit(text, (1050, 20))
    
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

    index = 0
    _, elem1, elem2 = distances[0]
    i, j = pos_reverse[elem1], pos_reverse[elem2]
    if input == "input" :
        borne = 1000
    else :
        borne = 10
    for _ in range(borne) :
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
        index += 1
        _, elem1, elem2 = distances[index]
        i, j = pos_reverse[elem1], pos_reverse[elem2]

        display_map()
        pygame.display.update()
        clock = pygame.time.Clock()
        if input == "input" :
            speed = 40
        else :
            speed = 2
        clock.tick(speed)
    return True

run = True

while run :
    run = animate()
    if run :
        sleep(1)

pygame.quit()
