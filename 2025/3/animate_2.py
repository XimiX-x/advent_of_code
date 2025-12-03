res = 0

with open("input") as file :
    for lines in file :
        line = [int(c) for c in lines.split()[0]]
        temp = 0
        for i in range(11, -1, -1) :
            dix = max(line) if i == 0 else max(line[:-i])
            temp = 10*temp + dix
            line = line[line.index(dix)+1:]
        res += temp

print(res)

import pygame
from time import sleep

pygame.init()
screen = pygame.display.set_mode((1500, 700))

pygame.font.init()
my_font = pygame.font.SysFont('arial', 20)

def animate() :
    res = [0]
    text = []
    index = [[-1]]
    with open("input") as file :
        for lines in file :
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return False
                if event.type == pygame.KEYDOWN :
                    if event.key == pygame.K_ESCAPE :
                        return False
            screen.fill((0, 0, 0))
            line = [int(c) for c in lines.split()[0]]
            text.append(line)
            temp = 0
            for i in range(11, -1, -1) :
                dix = max(line) if i == 0 else max(line[:-i])
                temp = 10*temp + dix
                index[-1].append(index[-1][-1]+1 + line.index(dix))
                line = line[line.index(dix)+1:]
            res.append(res[-1] + temp)
            text_surface = my_font.render("Results :", False, (255, 255, 255))
            screen.blit(text_surface, (50 + 30 + 12*len(text[0]), 50))
            for i in range(len(text)) :
                for j in range(len(text[i])) :
                    if j in index[i][1:] :
                        text_surface = my_font.render(f"{text[i][j]}", False, (0, 255, 0))
                    else :
                        text_surface = my_font.render(f"{text[i][j]}", False, (255, 0, 0))
                    screen.blit(text_surface, (50 + 12*j, 80 + 30*(len(text)-1-i)))
                text_surface = my_font.render(f"{res[i+1]}", False, (255, 255, 255))
                screen.blit(text_surface, (50 + 30 + 12*len(text[0]), 80 + 30*(len(text)-1-i)))
            pygame.display.update()
            clock = pygame.time.Clock()
            clock.tick(20)
            index.append([-1])
    return True


run = True

while run :
    run = animate()
    if run :
        sleep(2)

pygame.quit()
