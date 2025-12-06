pb = [[]]
res = 0

with open("input") as file :
    for lines in file :
        line = lines.split()
        if line[0].isdigit() :
            for num in line :
                pb[-1].append(int(num))
        else :
            for i, op in enumerate(line) :
                match op :
                    case '+' :
                        temp = 0
                        for j in range(len(pb)-1) :
                            temp += pb[j][i]
                        res += temp
                    case '*' :
                        temp = 1
                        for j in range(len(pb)-1) :
                            temp = temp * pb[j][i]
                        res += temp
        pb.append([])

print(res)

import pygame
from time import sleep

pygame.init()
screen = pygame.display.set_mode((1000, 200))

pygame.font.init()
my_font = pygame.font.SysFont('arial', 20)
my_big_font = pygame.font.SysFont('arial', 30)

def animate() :
    pb = [[]]
    res = 0

    def display(i) :
        j = 0
        for line in pb :
            for k in range(max(0, i-3), min(i+17, len(line))) :
                if k == i :
                    text = my_big_font.render(f"{line[k]}", False, (0, 255, 0))
                else :
                    text = my_font.render(f"{line[k]}", False, (255, 255, 255))
                if k == i :
                    screen.blit(text, ((k-i)*50 + 150, j*30+5))
                elif k < i :
                    screen.blit(text, ((k-i)*50 + 150, j*30+10))
                else :
                    screen.blit(text, ((k-i)*50 + 150 + 20, j*30+10))
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
            line = lines.split()
            if line[0].isdigit() :
                for num in line :
                    pb[-1].append(int(num))
            else :
                for i, op in enumerate(line) :
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            return False
                        if event.type == pygame.KEYDOWN :
                            if event.key == pygame.K_ESCAPE :
                                return False
                    match op :
                        case '+' :
                            temp = 0
                            for j in range(len(pb)-1) :
                                temp += pb[j][i]
                            res += temp
                        case '*' :
                            temp = 1
                            for j in range(len(pb)-1) :
                                temp = temp * pb[j][i]
                            res += temp
                    screen.fill((0,0,0))
                    display(i)
                    display_op(op)
                    pygame.display.update()
                    clock = pygame.time.Clock()
                    clock.tick(min(1 if i == 0 else i, len(line)-i))
            pb.append([])
    return True

run = True

while run :
    run = animate()
    if run :
        sleep(1)

pygame.quit()
