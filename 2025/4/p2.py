res = 0
removed = set()
res_temp = None

mapp = [list(lines.split()[0]+".") for lines in open("input")]

while res_temp != 0 :
    tab = [None, None, None]
    res_temp = 0
    for lines in mapp :
        tab[0] = lines # type: ignore
        if tab[1] is not None :
            if tab[2] is not None :
                for i,c in enumerate(tab[1]) :
                    if c == '@' :
                        count = 0
                        for x, y in ((1, i+1), (2, i+1), (2, i), (2, i-1), (1, i-1), (0, i-1), (0, i), (0, i+1)) :
                            if tab[x][y] == '@' : # type: ignore
                                count += 1
                        if count < 4 :
                            res_temp += 1
                            tab[1][i] = 'x'
            else :
                for i,c in enumerate(tab[1]) :
                    if c == '@' :
                        count = 0
                        for x, y in ((1, i+1), (1, i-1), (0, i-1), (0, i), (0, i+1)) :
                            if tab[x][y] == '@' : # type: ignore
                                count += 1
                        if count < 4 :
                            res_temp += 1
                            tab[1][i] = 'x'
        tab[2] = tab[1] # type: ignore
        tab[1] = tab[0] # type: ignore

    for i,c in enumerate(tab[1]) : # type: ignore
        if c == '@' :
            count = 0
            for x, y in ((1, i+1), (2, i+1), (2, i), (2, i-1), (1, i-1)) :
                if tab[x][y] == '@' : # type: ignore
                    count += 1
            if count < 4 :
                res_temp += 1
                tab[1][i] = 'x' # type: ignore
    res += res_temp

print(res)

### And an animation

import pygame
from time import sleep

pygame.init()
screen = pygame.display.set_mode((300, 400))

pygame.font.init()
my_font = pygame.font.SysFont('arial', 20)
car_width = 20

def animate() :
    input = "test"
    mapp = [list(lines.split()[0]+".") for lines in open(input)]
    res = 0
    res_temp = None
    speed = 60
    tab = [None, None, None]

    def display_line() :
        for k in range(len(mapp)) :
            for i, c in enumerate(mapp[k][:-1]) :
                if c == 'x' :
                    text = my_font.render(f"{c}", False, (0, 255, 0))
                else :
                    text = my_font.render(f"{c}", False, (255, 255, 255))
                if c == "." :
                    screen.blit(text, (50 + car_width/3 + i*car_width, 80 + k*30))
                else :
                    screen.blit(text, (50 + i*car_width, 80 + k*30))

    def display_res() :
        text = my_font.render(f"Results : {res}", False, (255, 255, 255))
        screen.blit(text, (100, 40)) # type: ignore

    while res_temp != 0 :
        j = -1
        tab = [None, None, None]
        res_temp = 0
        for lines in mapp :
            tab[0] = lines # type: ignore
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
                            count = 0
                            for x, y in ((1, i+1), (2, i+1), (2, i), (2, i-1), (1, i-1), (0, i-1), (0, i), (0, i+1)) :
                                if tab[x][y] == '@' : # type: ignore
                                    count += 1
                            if count < 4 :
                                res += 1
                                res_temp += 1
                                tab[1][i] = 'x'
                        screen.fill((0,0,0))
                        display_line()
                        text = my_font.render(f"{c}", False, (0, 0, 255))
                        screen.blit(text, (50 + i*car_width, 80 + j*30))
                        display_res()
                        pygame.display.update()
                        clock = pygame.time.Clock()
                        clock.tick(speed)
                else :
                    for i,c in enumerate(tab[1][:-1]) :
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                return False
                            if event.type == pygame.KEYDOWN :
                                if event.key == pygame.K_ESCAPE :
                                    return False
                        if c == '@' :
                            count = 0
                            for x, y in ((1, i+1), (1, i-1), (0, i-1), (0, i), (0, i+1)) :
                                if tab[x][y] == '@' : # type: ignore
                                    count += 1
                            if count < 4 :
                                res += 1
                                res_temp += 1
                                tab[1][i] = 'x'
                        screen.fill((0,0,0))
                        display_line()
                        text = my_font.render(f"{c}", False, (0, 0, 255))
                        screen.blit(text, (50 + i*car_width, 80 + j*30))
                        display_res()
                        pygame.display.update()
                        clock = pygame.time.Clock()
                        clock.tick(speed)
            tab[2] = tab[1] # type: ignore
            tab[1] = tab[0] # type: ignore
            j += 1

        for i,c in enumerate(tab[1][:-1]) : # type: ignore
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return False
                if event.type == pygame.KEYDOWN :
                    if event.key == pygame.K_ESCAPE :
                        return False
            if c == '@' :
                count = 0
                for x, y in ((1, i+1), (2, i+1), (2, i), (2, i-1), (1, i-1)) :
                    if tab[x][y] == '@' : # type: ignore
                        count += 1
                if count < 4 :
                    res += 1
                    res_temp += 1
                    tab[1][i] = 'x' # type: ignore
            screen.fill((0,0,0))
            display_line()
            text = my_font.render(f"{c}", False, (0, 0, 255))
            screen.blit(text, (50 + i*car_width, 80 + j*30))
            display_res()
            pygame.display.update()
            clock = pygame.time.Clock()
            clock.tick(speed)

    for j in range(256) :
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN :
                if event.key == pygame.K_ESCAPE :
                    return False
        screen.fill((0,0,0))
        display_res()
        for k in range(len(mapp)) :
            for i, c in enumerate(mapp[k][:-1]) :
                if c == 'x' :
                    text = my_font.render(f"{c}", False, (0, 255, 0))
                elif c == '.' :
                    text = my_font.render(f"{c}", False, (255, 255, 255))
                else :
                    text = my_font.render(f"{c}", False, (255, 255-j, 255-j))
                if c == "." :
                    screen.blit(text, (50 + car_width/3 + i*car_width, 80 + k*30))
                else :
                    screen.blit(text, (50 + i*car_width, 80 + k*30))
        pygame.display.update()
        clock = pygame.time.Clock()
        clock.tick(130)

    return True

while animate() :
    pass


pygame.quit()
