pb = []
res = 0

with open("input") as file :
    for lines in file :
        if lines.split()[0].isdigit() :
            pb.append(lines[:-1])
        else :
            line = lines.split()
            pred = 0
            suiv = 0
            for i, op in enumerate(line) :
                for i in range(pred+1, len(lines)) :
                    if lines[i] in ('+', '*') :
                        suiv = i
                        break
                else :
                    suiv = len(lines)+1
                match op :
                    case '+' :
                        temp = 0
                        for k in range(pred, suiv-1) :
                            num = ''
                            for j in range(len(pb)) :
                                if pb[j][k] != ' ' :
                                    num += pb[j][k]
                            temp += int(num)
                        res += temp
                    case '*' :
                        temp = 1
                        for k in range(pred, suiv-1) :
                            num = ''
                            for j in range(len(pb)) :
                                if pb[j][k] != ' ' :
                                    num += pb[j][k]
                            temp *= int(num)
                        res += temp
                pred = suiv

print(res)

import pygame
from time import sleep
from itertools import cycle

pygame.init()
screen = pygame.display.set_mode((1000, 200))

pygame.font.init()
my_font = pygame.font.SysFont('arial', 20)
my_big_font = pygame.font.SysFont('arial', 30)

def animate() :
    pb = []
    res = 0

    def display(pred, suiv) :
        j = 0
        for line in pb :
            col_it = cycle(((255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 0, 255)))
            for k in range(max(0, pred-9), min(suiv+53, len(line))) :
                if pred <= k < suiv :
                    text = my_big_font.render(f"{line[k]}", False, next(col_it))
                else :
                    text = my_font.render(f"{line[k]}", False, (255, 255, 255))
                if pred <= k < suiv :
                    screen.blit(text, ((k-pred)*20 + 150, j*30+5))
                elif k < pred :
                    screen.blit(text, ((k-pred)*15 + 150, j*30+10))
                else :
                    screen.blit(text, ((k-i)*15 + 150 + (suiv-pred)*20, j*30+10))
            j += 1
        text = my_font.render(f"Result :", False, (255, 255, 255))
        screen.blit(text, (20, 170))
        text = my_font.render(f"{res}", False, (255, 255, 255))
        screen.blit(text, (150, 170))

    def display_op(op) :
        text = my_font.render(f"Operator :", False, (255, 255, 255))
        screen.blit(text, (20, 140))
        text = my_font.render(f"{op}", False, (255, 255, 255))
        screen.blit(text, (170, 140))

    with open("input") as file :
        for lines in file :
            if lines.split()[0].isdigit() :
                pb.append(lines[:-1])
            else :
                line = lines.split()
                pred = 0
                suiv = 0
                for i, op in enumerate(line) :
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            return False
                        if event.type == pygame.KEYDOWN :
                            if event.key == pygame.K_ESCAPE :
                                return False
                    for i in range(pred+1, len(lines)) :
                        if lines[i] in ('+', '*') :
                            suiv = i
                            break
                    else :
                        suiv = len(lines)+1
                    match op :
                        case '+' :
                            temp = 0
                            for k in range(pred, suiv-1) :
                                num = ''
                                for j in range(len(pb)) :
                                    if pb[j][k] != ' ' :
                                        num += pb[j][k]
                                temp += int(num)
                            res += temp
                        case '*' :
                            temp = 1
                            for k in range(pred, suiv-1) :
                                num = ''
                                for j in range(len(pb)) :
                                    if pb[j][k] != ' ' :
                                        num += pb[j][k]
                                temp *= int(num)
                            res += temp
                    screen.fill((0,0,0))
                    display(pred, suiv)
                    display_op(op)
                    pygame.display.update()
                    clock = pygame.time.Clock()
                    clock.tick(min(1 if pred//2 == 0 else pred//2, (len(lines)-pred)//2))
                    pred = suiv
    return True

run = True

while run :
    run = animate()
    if run :
        sleep(1)

pygame.quit()
