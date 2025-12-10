#!/usr/bin/env python3.10
import re
from scipy.optimize import milp, LinearConstraint, Bounds
import numpy as np

res = 0
with open("input") as file :
    for lines in file :
        goal = re.findall(r"\{.*\}", lines)[0][1:-1]
        goal = re.split(",", goal)
        goal = [int(elem) for elem in goal]
        buttons = re.findall(r"\(.*\)", lines)[0].split()
        buttons = [re.findall(r"\d+", elem) for elem in buttons]
        buttons = [[int(elem) for elem in butt] for butt in buttons]

        A = np.zeros((len(goal), len(buttons)))
        for i in range(len(goal)) :
            for j, butt in enumerate(buttons) :
                if i in butt :
                    A[i, j] = 1

        sol = milp(np.ones(len(buttons)),integrality= 1, bounds= Bounds(lb = 0, ub = max(goal)), constraints= LinearConstraint(A, lb = goal, ub = goal)) # type: ignore
        res += int(sum(sol.x))

print(res)

## Animation

import pygame
from time import sleep

pygame.init()
screen = pygame.display.set_mode((1000, 400))

pygame.font.init()
font = pygame.font.SysFont("arial", 20)

def animate() :
    glob_res = 0

    def animate_buttons(x, buttons, size) :
        sleep_time = 0.05
        res = glob_res
        state = [0 for _ in range(size)]
        screen.fill((0,0,0))
        for i, v in enumerate(state) :
            text = font.render(f"{v}", False, (255, 255, 255))
            screen.blit(text, (500 + (size/2-i)*40, 50))
        text = font.render(f"Result : {res}", False, (255, 255, 255))
        screen.blit(text, (435, 300))
        for j in range(len(buttons)) :
            pygame.draw.circle(screen, (0, 0, 255), (500 -(len(buttons)/2-j-1)*100-50, 175), 50)
        pygame.display.update()
        for nb, butt in zip(x, buttons) :
            for _ in range(int(nb)) :
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        return False
                    if event.type == pygame.KEYDOWN :
                        if event.key == pygame.K_ESCAPE :
                            return False
                for index in butt :
                    state[index] += 1
                res += 1
                screen.fill((0,0,0))
                for i, v in enumerate(state) :
                    text = font.render(f"{v}", False, (255, 255, 255))
                    screen.blit(text, (500 + (size/2-i-1)*40, 50))
                text = font.render(f"Result : {res}", False, (255, 255, 255))
                screen.blit(text, (435, 300))
                for j in range(len(buttons)) :
                    if buttons[j] == butt :
                        col = (0, 255, 0)
                    else :
                        col = (0, 0, 255)
                    pygame.draw.circle(screen, col, (500 -(len(buttons)/2-j-1)*100-50, 175), 50)
                pygame.display.update()
                sleep(sleep_time)
                screen.fill((0,0,0))
                for i, v in enumerate(state) :
                    text = font.render(f"{v}", False, (255, 255, 255))
                    screen.blit(text, (500 + (size/2-i-1)*40, 50))
                text = font.render(f"Result : {res}", False, (255, 255, 255))
                screen.blit(text, (435, 300))
                for j in range(len(buttons)) :
                    pygame.draw.circle(screen, (0, 0, 255), (500 -(len(buttons)/2-j-1)*100-50, 175), 50)
                pygame.display.update()
                sleep(sleep_time)
        return True

    with open("input") as file :
        for lines in file :
            goal = re.findall(r"\{.*\}", lines)[0][1:-1]
            goal = re.split(",", goal)
            goal = [int(elem) for elem in goal]
            buttons = re.findall(r"\(.*\)", lines)[0].split()
            buttons = [re.findall(r"\d+", elem) for elem in buttons]
            buttons = [[int(elem) for elem in butt] for butt in buttons]

            A = np.zeros((len(goal), len(buttons)))
            for i in range(len(goal)) :
                for j, butt in enumerate(buttons) :
                    if i in butt :
                        A[i, j] = 1

            sol = milp(np.ones(len(buttons)),integrality= 1, bounds= Bounds(lb = 0, ub = max(goal)), constraints= LinearConstraint(A, lb = goal, ub = goal)) # type: ignore
            if not animate_buttons(sol.x, buttons, len(goal)) :
                return False
            glob_res += int(sum(sol.x))
    return True

run = True

while run :
    run = animate()
    if run :
        sleep(1)

pygame.quit()
