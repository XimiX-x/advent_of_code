bornes = []
res = 0
ids = False

with open("input") as file :
    for lines in file :
        line = lines.split()
        if line :
            line = line[0]
        else : 
            ids = True
        if not ids :
            bornes.append([int(i) for i in line.split("-")]) # type: ignore
        else :
            if line :
                for (inf, sup) in bornes :
                    if inf <= int(line) <= sup : # type: ignore
                        res += 1
                        break

print(res)

### Animation time !!

import pygame

pygame.init()
screen = pygame.display.set_mode((1500, 200))

pygame.font.init()
my_font = pygame.font.SysFont('arial', 20)
borne_size = 350

def animate() :
    bornes = []
    res = 0
    ids = False
    speed = 60

    def display_bornes(ind = 0) :
        for i in range(ind, min(ind+6, len(bornes))) :
            inf, sup = bornes[i]
            text = my_font.render(f"{inf}-{sup}", False, (255, 255, 255))
            screen.blit(text, (10+(i-ind)*borne_size, 50))

    def display_res() :
        text = my_font.render(f"Result : {res}", False, (255, 255, 255))
        screen.blit(text, (10, 150))

    with open("input") as file :
        for lines in file :
            line = lines.split()
            if line :
                line = line[0]
            else : 
                ids = True
            if not ids :
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        return False
                    if event.type == pygame.KEYDOWN :
                        if event.key == pygame.K_ESCAPE :
                            return False
                bornes.append([int(i) for i in line.split("-")]) # type: ignore
                screen.fill((0,0,0))
                display_bornes()
                pygame.display.update()
            else :
                if line :
                    ind = 0
                    for (inf, sup) in bornes :
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                return False
                            if event.type == pygame.KEYDOWN :
                                if event.key == pygame.K_ESCAPE :
                                    return False
                        if inf <= int(line) <= sup : # type: ignore
                            res += 1
                        screen.fill((0,0,0))
                        display_bornes(ind)
                        display_res()
                        text = my_font.render(line, False, (255, 255, 255)) # type: ignore
                        screen.blit(text, (10, 100))
                        pygame.display.update()
                        clock = pygame.time.Clock()
                        clock.tick(speed)
                        if inf <= int(line) <= sup : # type: ignore
                            for i in range(256) :
                                for event in pygame.event.get():
                                    if event.type == pygame.QUIT:
                                        return False
                                    if event.type == pygame.KEYDOWN :
                                        if event.key == pygame.K_ESCAPE :
                                            return False
                                screen.fill((0,0,0))
                                display_bornes(ind)
                                display_res()
                                text = my_font.render(line, False, (255-i, 255, 255-i)) # type: ignore
                                screen.blit(text, (10, 100))
                                pygame.display.update()
                                clock = pygame.time.Clock()
                                clock.tick(255)
                            break
                        ind += 1
                    else :
                        for i in range(256) :
                            for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                    return False
                                if event.type == pygame.KEYDOWN :
                                    if event.key == pygame.K_ESCAPE :
                                        return False
                            screen.fill((0,0,0))
                            display_bornes(ind)
                            display_res()
                            text = my_font.render(line, False, (255, 255-i, 255-i)) # type: ignore
                            screen.blit(text, (10, 100))
                            pygame.display.update()
                            clock = pygame.time.Clock()
                            clock.tick(255)
    return True

while animate() :
    pass

pygame.quit()
