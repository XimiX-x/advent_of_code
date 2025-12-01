from numpy import cumsum

print(sum([not pos for pos in cumsum([50] + [(-1 if line.split()[0][0] == 'L' else 1) * int(line.split()[0][1:]) for line in open("input")])%100]))

### And a cool animation :

import pygame
from numpy import cos, sin, pi
from time import sleep

pygame.init()
screen = pygame.display.set_mode((1900, 1000))

pygame.font.init()
my_font = pygame.font.SysFont('arial', 15)
res_font = pygame.font.SysFont('arial', 25)

def print_dial(rota) :
    pygame.draw.circle(screen, (255, 255, 255), (950, 550), 400)
    pygame.draw.circle(screen, (0, 0, 0), (950, 550), 399)
    top, bot, value = False, False, 0 if abs((((-50)*3.6 + 90 + rota)*pi/180)%(2*pi)-pi/2) < abs(((99-50)*3.6 + 90 + rota)*pi/180%(2*pi)-pi/2)  else 99
    for i in range(100) :
        alpha = ((i-50)*3.6 + 90 + rota)*pi/180
        alpha2 = ((i-1-50)*3.6 + 90 + rota)*pi/180
        if not bot :
            if alpha%(2*pi) >= 3*pi/2 or alpha%(2*pi) < pi/2:
                bot = True
        if not top and bot :
            if 3*pi/2 > alpha%(2*pi) >= pi/2 :
                top = True
                if abs(alpha%(2*pi)-pi/2) < abs(alpha2%(2*pi)-pi/2) :
                    value = i
                else :
                    value = i-1
        x, y = 370*cos(alpha), 370*sin(alpha)
        text_surface = my_font.render(f"{i}", False, (255, 255, 255))
        screen.blit(text_surface, (950+x-5, 550-y-5))
    pygame.draw.line(screen, (255, 255, 255), (950, 140), (950, 100))
    text_surface = my_font.render(f"{value}", False, (255, 255, 255))
    screen.blit(text_surface, (942, 85))
    return value

def simu_pb():
    deg = 0
    res = 0
    tick = 60
    with open("input") as file :
        for lines in file :
            line = lines.split()[0]
            match line[0] :
                case 'L' :
                    for _ in range(1, 3*int(line[1:])+1) :
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                return False
                            if event.type == pygame.KEYDOWN :
                                if event.key == pygame.K_ESCAPE :
                                    return False
                        screen.fill((0, 0, 0))
                        deg += 1.2
                        value = print_dial(deg)
                        text_surface = res_font.render(f"{res=}", False, (255, 255, 255))
                        screen.blit(text_surface, (915, 515))
                        pygame.display.update()
                        clock = pygame.time.Clock()
                        clock.tick(tick)
                case 'R' :
                    for _ in range(1, 3*int(line[1:])+1) :
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                return False
                            if event.type == pygame.KEYDOWN :
                                if event.key == pygame.K_ESCAPE :
                                    return False
                        screen.fill((0, 0, 0))
                        deg -= 1.2
                        value = print_dial(deg)
                        text_surface = res_font.render(f"{res=}", False, (255, 255, 255))
                        screen.blit(text_surface, (915, 515))
                        pygame.display.update()
                        clock = pygame.time.Clock()
                        clock.tick(tick)
            if value == 0 : # type: ignore
                res += 1
            sleep(0.5)
    return True

run = True

while run :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN :
            if event.key == pygame.K_ESCAPE :
                run = False
    run = simu_pb()
    if run :
        sleep(2)

pygame.quit()