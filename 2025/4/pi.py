res = 0

tab = [None, None, None]
with open("input") as file :
    for lines in file :
        tab[0] = lines.split()[0] + "." # type: ignore
        if tab[1] is not None :
            if tab[2] is not None :
                for i,c in enumerate(tab[1]) :
                    if c == '@' :
                        count = 0
                        for x, y in ((1, i+1), (2, i+1), (2, i), (2, i-1), (1, i-1), (0, i-1), (0, i), (0, i+1)) :
                            if tab[x][y] == '@' : # type: ignore
                                count += 1
                        if count < 4 :
                            res += 1
            else :
                for i,c in enumerate(tab[1]) :
                    if c == '@' :
                        count = 0
                        for x, y in ((1, i+1), (1, i-1), (0, i-1), (0, i), (0, i+1)) :
                            if tab[x][y] == '@' : # type: ignore
                                count += 1
                        if count < 4 :
                            res += 1
        tab[2] = tab[1] # type: ignore
        tab[1] = tab[0] # type: ignore


for i,c in enumerate(tab[1]) : # type: ignore
    if c == '@' :
        count = 0
        for x, y in ((1, i+1), (2, i+1), (2, i), (2, i-1), (1, i-1)) :
            if tab[x][y] == '@' : # type: ignore
                count += 1
        if count < 4 :
            res += 1

print(res)

### And an animation

import pygame
from time import sleep

pygame.init()
screen = pygame.display.set_mode((1800, 470))

pygame.font.init()
my_font = pygame.font.SysFont('arial', 15)
car_width = 12

def animate() :
    input = "input"
    mapp = [list(lines.split()[0]) for lines in open(input)]
    pos = {}
    res = []
    j = 0
    speed = 0
    tab = [None, None, None]

    def display_line() :
        for k in range(max(0, j-10), min(j+1, len(mapp))) :
            for i, c in enumerate(mapp[k]) :
                if (k, i) in pos.keys() :
                    text = my_font.render(f"{c}", False, pos[(k, i)])
                else :
                    text = my_font.render(f"{c}", False, (255, 255, 255))
                if c == "." :
                    screen.blit(text, (50 + car_width/3 + i*car_width, 450 - (80+(j-k)*30)))
                else :
                    screen.blit(text, (50 + i*car_width, 450 - (80+(j-k)*30)))

    def display_res() :
        text = my_font.render("Results :", False, (255, 255, 255))
        screen.blit(text, (50 + 30 + (len(tab[0])-1)*car_width, 40)) # type: ignore
        for k in range(max(0, j-10), j) :
            text = my_font.render(f"{res[k]}", False, (255, 255, 255))
            screen.blit(text, (50 + 30 + (len(tab[0])-1)*car_width, 450 - (80+(j-k)*30))) # type: ignore

    with open(input) as file :
        for lines in file :
            tab[0] = lines.split()[0] + "." # type: ignore
            if tab[1] is not None :
                if tab[2] is not None :
                    for i,c in enumerate(tab[1][:-1]) :
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                return False
                            if event.type == pygame.KEYDOWN :
                                if event.key == pygame.K_ESCAPE :
                                    return False
                        if c == '@' :
                            pos[j-1, i] = (255, 0, 0)
                            count = 0
                            for x, y in ((1, i+1), (2, i+1), (2, i), (2, i-1), (1, i-1), (0, i-1), (0, i), (0, i+1)) :
                                if tab[x][y] == '@' : # type: ignore
                                    count += 1
                            if count < 4 :
                                pos[j-1, i] = (0, 255, 0)
                                res[-1] += 1
                        screen.fill((0,0,0))
                        display_line()
                        display_res()
                        pygame.display.update()
                        clock = pygame.time.Clock()
                        clock.tick(speed)
                else :
                    for i,c in enumerate(tab[1]) :
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                return False
                            if event.type == pygame.KEYDOWN :
                                if event.key == pygame.K_ESCAPE :
                                    return False
                        if c == '@' :
                            pos[j-1, i] = (255, 0, 0)
                            count = 0
                            for x, y in ((1, i+1), (1, i-1), (0, i-1), (0, i), (0, i+1)) :
                                if tab[x][y] == '@' : # type: ignore
                                    count += 1
                            if count < 4 :
                                pos[j-1, i] = (0, 255, 0)
                                res[-1] += 1
                        screen.fill((0,0,0))
                        display_line()
                        display_res()
                        pygame.display.update()
                        clock = pygame.time.Clock()
                        clock.tick(speed)
            tab[2] = tab[1] # type: ignore
            tab[1] = tab[0] # type: ignore
            j += 1
            if res :
                res.append(res[-1])
            else :
                res.append(0)

    for i,c in enumerate(tab[1]) : # type: ignore
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN :
                if event.key == pygame.K_ESCAPE :
                    return False
        if c == '@' :
            pos[j-1, i] = (255, 0, 0)
            count = 0
            for x, y in ((1, i+1), (2, i+1), (2, i), (2, i-1), (1, i-1)) :
                if tab[x][y] == '@' : # type: ignore
                    count += 1
            if count < 4 :
                pos[j-1, i] = (0, 255, 0)
                res[-1] += 1
        screen.fill((0,0,0))
        display_line()
        display_res()
        pygame.display.update()
        clock = pygame.time.Clock()
        clock.tick(speed)
    return True

run = True

while run :
    run = animate()
    if run :
        sleep(2)

pygame.quit()
