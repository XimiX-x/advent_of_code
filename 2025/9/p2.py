#!/usr/bin/env python3.10
from math import inf

# points = []
# edges = []

# with open("input") as file :
#     for lines in file :
#         line = lines.split()[0].split(",")
#         points.append((int(line[0]), int(line[1])))
#         if len(points) > 1 :
#             edges.append((points[-2], points[-1]))
# edges.append((points[-1], points[0]))

# def is_point_inside(x, y) :
#     cpt = 0
#     for p1, p2 in edges :
#         if p1 == (x, y) :
#             return True
#         if p1[1] == p2[1] == y :
#             if p2[0] < x <= p1[0] or p1[0] <= x < p2[0] :
#                 return True
#             if x < min(p1[0], p2[0]) :
#                 cpt += 1
#         elif p1[1] != p2[1] and p1[0] >= x :
#             if p1[1] <= y < p2[1] or p1[1] >= y > p2[1] :
#                 if p1[0] == x :
#                     return True
#                 cpt += 1
#     return cpt%2 == 1

# for i in range(len(edges)-1, 0, -1) :
#     edge1, edge2 = edges[i-1], edges[i]
#     if edge1[0][0] == edge2[1][0] or edge1[0][1] == edge2[1][1] :
#         edge = (edge1[0], edge2[1])
#         edges[i-1] = edge
#         del edges[i]

# max_area = 0
# for i, p1 in enumerate(points) :
#     for j in range(i) :
#         p2 = points[j]
#         min_x = min(p1[0], p2[0])
#         max_x = max(p1[0], p2[0])
#         min_y = min(p1[1], p2[1])
#         max_y = max(p1[1], p2[1])
#         for e1, e2 in edges :
#             if min_x < e1[0] == e2[0] < max_x :
#                 min_e, max_e = min(e1[1], e2[1]), max(e1[1], e2[1])
#                 if min_e <= min_y < max_e or min_e < max_y <= max_e :
#                     break
#             elif min_y < e1[1] == e2[1] < max_y :
#                 min_e, max_e = min(e1[0], e2[0]), max(e1[0], e2[0])
#                 if min_e <= min_x < max_e or min_e < max_x <= max_e :
#                     break
#         else :
#             if is_point_inside(p1[0], p2[1]) and is_point_inside(p2[0], p1[1]) :
#                 max_area = max((abs(p1[0]-p2[0])+1)*(abs(p1[1]-p2[1])+1), max_area)

# print(max_area)

### And a cool animation

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
        for p1, p2 in edges :
            pygame.draw.rect(screen, (255, 0, 0), (min(p1[0], p2[0])/100, min(p1[1], p2[1])/100, abs(p1[0]-p2[0])/100+1, abs(p1[1]-p2[1])/100+1))

    def display_data(area) :
        text = font.render(f"Max area : {max_area}", False, (255, 255, 255))
        screen.blit(text, (1020, 50))
        if area == 0 :
            text = font.render(f"Area : Invalid rectangle", False, (255, 255, 255))
        else :
            text = font.render(f"Area : {area}", False, (255, 255, 255))
        screen.blit(text, (1020, 80))

    edges = []
    with open("input") as file :
        for lines in file :
            line = lines.split()[0].split(",")
            points.append((int(line[0]), int(line[1])))
            if len(points) > 1 :
                edges.append((points[-2], points[-1]))
    edges.append((points[-1], points[0]))

    def is_point_inside(x, y) :
        cpt = 0
        for p1, p2 in edges :
            if p1 == (x, y) :
                return True
            if p1[1] == p2[1] == y :
                if p2[0] < x <= p1[0] or p1[0] <= x < p2[0] :
                    return True
                if x < min(p1[0], p2[0]) :
                    cpt += 1
            elif p1[1] != p2[1] and p1[0] >= x :
                if p1[1] <= y < p2[1] or p1[1] >= y > p2[1] :
                    if p1[0] == x :
                        return True
                    cpt += 1
        return cpt%2 == 1

    for i in range(len(edges)-1, 0, -1) :
        edge1, edge2 = edges[i-1], edges[i]
        if edge1[0][0] == edge2[1][0] or edge1[0][1] == edge2[1][1] :
            edge = (edge1[0], edge2[1])
            edges[i-1] = edge
            del edges[i]

    max_area = 0
    for i, p1 in enumerate(points) :
        for j in range(i) :
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return False
                if event.type == pygame.KEYDOWN :
                    if event.key == pygame.K_ESCAPE :
                        return False
            p2 = points[j]
            area = 0
            col = (0, 0, 255)
            min_x = min(p1[0], p2[0])
            max_x = max(p1[0], p2[0])
            min_y = min(p1[1], p2[1])
            max_y = max(p1[1], p2[1])
            for e1, e2 in edges :
                if min_x < e1[0] == e2[0] < max_x :
                    min_e, max_e = min(e1[1], e2[1]), max(e1[1], e2[1])
                    if min_e <= min_y < max_e or min_e < max_y <= max_e :
                        break
                elif min_y < e1[1] == e2[1] < max_y :
                    min_e, max_e = min(e1[0], e2[0]), max(e1[0], e2[0])
                    if min_e <= min_x < max_e or min_e < max_x <= max_e :
                        break
            else :
                if is_point_inside(p1[0], p2[1]) and is_point_inside(p2[0], p1[1]) :
                    area = (abs(p1[0]-p2[0])+1)*(abs(p1[1]-p2[1])+1)
                    col = (0, 255, 0)
                    max_area = max((abs(p1[0]-p2[0])+1)*(abs(p1[1]-p2[1])+1), max_area)
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
