#!/usr/bin/env python3.10
import re
import heapq

def compute_state(curr_state, button) :
    new_state = curr_state.copy()
    for index in button :
        if curr_state[index] == '.' :
            new_state[index] = '#'
        else :
            new_state[index] = '.'
    return new_state

def state_to_str(state) :
    state_str = ""
    for c in state :
        state_str += c
    return state_str

res = 0
with open("input") as file :
    for lines in file :
        goal = re.findall(r"\[.*\]", lines)[0][1:-1]
        goal = [c for c in goal]
        buttons = re.findall(r"\(.*\)", lines)[0].split()
        buttons = [re.findall(r"\d+", elem) for elem in buttons]
        buttons = [[int(elem) for elem in butt] for butt in buttons]

        start = ['.' for _ in goal]
        q = [(0, start)]
        pred = {state_to_str(start) : start}
        while q :
            dist, state = heapq.heappop(q)
            if state == goal :
                res += dist
                break
            for butt in buttons :
                next_state = compute_state(state, butt)
                next_str = state_to_str(next_state)
                if not next_str in pred.keys() :
                    pred[next_str] = state
                    heapq.heappush(q, (dist+1, next_state))

print(res)

### Animation

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
        state = ["." for _ in range(size)]
        screen.fill((0,0,0))
        for i, v in enumerate(state) :
            text = font.render(f"{v}", False, (255, 255, 255))
            screen.blit(text, (500 + (size/2-i)*40, 50))
        text = font.render(f"Result : {res}", False, (255, 255, 255))
        screen.blit(text, (435, 300))
        for j in range(len(buttons)) :
            pygame.draw.circle(screen, (0, 0, 255), (500 -(len(buttons)/2-j-1)*100-50, 175), 50)
        pygame.display.update()
        for nb in x :
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return False
                if event.type == pygame.KEYDOWN :
                    if event.key == pygame.K_ESCAPE :
                        return False
            state = compute_state(state, buttons[nb])
            res += 1
            screen.fill((0,0,0))
            for i, v in enumerate(state) :
                text = font.render(f"{v}", False, (255, 255, 255))
                screen.blit(text, (500 + (size/2-i-1)*40, 50))
            text = font.render(f"Result : {res}", False, (255, 255, 255))
            screen.blit(text, (435, 300))
            for j in range(len(buttons)) :
                if j == nb :
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
            goal = re.findall(r"\[.*\]", lines)[0][1:-1]
            goal = [c for c in goal]
            buttons = re.findall(r"\(.*\)", lines)[0].split()
            buttons = [re.findall(r"\d+", elem) for elem in buttons]
            buttons = [[int(elem) for elem in butt] for butt in buttons]

            start = ['.' for _ in goal]
            q = [(0, start)]
            pred = {state_to_str(start) : (start, 0)}
            while q :
                dist, state = heapq.heappop(q)
                if state == goal :
                    break
                for i, butt in enumerate(buttons) :
                    next_state = compute_state(state, butt)
                    next_str = state_to_str(next_state)
                    if not next_str in pred.keys() :
                        pred[next_str] = (state, i)
                        heapq.heappush(q, (dist+1, next_state))

            path = []
            state = goal
            while state != start :
                state, butt = pred[state_to_str(state)]
                path.append(butt)
            
            if not animate_buttons(path, buttons, len(goal)) :
                return False
            glob_res += dist # type: ignore
    return True

run = True

while run :
    run = animate()
    if run :
        sleep(1)

pygame.quit()

