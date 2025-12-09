#!/usr/bin/env python3.10
points = []

with open("input") as file :
    for lines in file :
        line = lines.split()[0].split(",")
        points.append((int(line[0]), int(line[1])))

max_area = 0
for i, p1 in enumerate(points) :
    for j in range(i) :
        p2 = points[j]
        max_area = max((abs(p1[0]-p2[0])+1)*(abs(p1[1]-p2[1])+1), max_area)

print(max_area)

### Time to animate

import pygame
from time import sleep

pygame.init()
screen = pygame.display.set_mode((1300, 1000))

pygame.font.init()
font = pygame.font.SysFont("arial", 20)

def animate() :
    points = []
    max_area = 0

    def display_points() :
        for x, y in points :
            pygame.draw.rect(screen, (255, 0, 0), (x/100, y/100, 1, 1))

    def display_data(area) :
        text = font.render(f"Max area : {max_area}", False, (255, 255, 255))
        screen.blit(text, (1020, 50))
        text = font.render(f"Area : {area}", False, (255, 255, 255))
        screen.blit(text, (1020, 80))

    with open("input") as file: 
        for lines in file :
            line = lines.split()[0].split(",")
            points.append((int(line[0]), int(line[1])))

    screen.fill((0,0,0))
    display_points()
    pygame.display.update()

    for i, p1 in enumerate(points) :
        for j in range(i) :
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return False
                if event.type == pygame.KEYDOWN :
                    if event.key == pygame.K_ESCAPE :
                        return False
            p2 = points[j]
            area = (abs(p1[0]-p2[0])+1)*(abs(p1[1]-p2[1])+1)
            if area > max_area :
                max_area = area
                col = (0, 255, 0)
            else :
                col = (0, 0, 255)
            screen.fill((0,0,0))
            display_points()
            display_data(area)
            pygame.draw.rect(screen, col, (min(p1[0], p2[0])/100, min(p1[1], p2[1])/100, abs(p1[0]-p2[0])/100+1, abs(p1[1]-p2[1])/100+1))
            pygame.display.update()
    return True

run = True

while run :
    run = animate()
    if run :
        sleep(1)

pygame.quit()
