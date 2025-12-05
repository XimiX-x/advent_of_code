bornes = []
res = 0

with open("input") as file :
    for lines in file :
        line = lines.split()
        if line :
            line = line[0]
            inf, sup = [int(i) for i in line.split("-")]
            for i, (bi, bs) in enumerate(bornes) :
                if bi <= inf and sup <= bs :
                    break
                if inf <= bi and bi <= sup <= bs :
                    bornes[i] = [inf, bs]
                    j = i-1
                    while j>=0 and bornes[j][1] >= bornes[i][0] :
                        if bornes[j][0] <= inf :
                            bornes[i] = [bornes[j][0], bs]
                        j = j-1
                    for _ in range(j+1, i) :
                        del bornes[j+1]
                    break
                if bs >= inf >= bi and bs <= bornes[i][1] :
                    bornes[i] = [bi, sup]
                    k = i+1
                    while k < len(bornes) and bornes[k][0] <= bornes[i][1] :
                        if bornes[k][1] >= sup :
                            bornes[i] = [bi, bornes[k][1]]
                        k += 1
                    for _ in range(i+1, k) :
                        del bornes[i+1]
                    break
                if inf <= bi and bs <= sup :
                    bornes[i] = [inf, sup]
                    j = i-1
                    while j>=0 and bornes[j][1] >= bornes[i][0] :
                        if bornes[j][0] <= inf :
                            bornes[i] = [bornes[j][0], sup]
                        j = j-1
                    k = i+1
                    while k < len(bornes) and bornes[k][0] <= bornes[i][1] :
                        if bornes[k][1] >= sup :
                            bornes[i] = [bornes[i][0], bornes[k][1]]
                        k += 1
                    for _ in range(j+1, i) :
                        del bornes[j+1]
                    for _ in range(i+1, k) :
                        del bornes[i+1-(i-j-1)]
                    break
            else :
                bornes.append([int(i) for i in line.split("-")])
                bornes.sort()
        else : 
            for inf, sup in bornes :
                res += sup - inf + 1
            break

print(res)

### Animation time :

import pygame
from time import sleep

pygame.init()
screen = pygame.display.set_mode((1500, 900))

pygame.font.init()
my_font = pygame.font.SysFont('arial', 15)
borne_width = 350
borne_heigth = 20

def animate() :
    bornes = []
    res = 0
    speed = 10
    sleep_time = 0.1

    def display_bornes(insert = None, delete_inf = None, delete_sup = None, ind_min = 0) :
        for k in range(min(ind_min, len(bornes)-1), len(bornes)) :
            inf, sup = bornes[k]
            if insert is not None :
                if k == insert :
                    text = my_font.render(f"{inf}-{sup}", False, (0, 255, 0))
                elif delete_inf is not None :
                    for bi, bs in zip(delete_inf, delete_sup) : # type: ignore
                        if bi <= k <= bs :
                            text = my_font.render(f"{inf}-{sup}", False, (255, 0, 0))
                            break
                    else :
                        text = my_font.render(f"{inf}-{sup}", False, (255, 255, 255))
                else :
                    text = my_font.render(f"{inf}-{sup}", False, (255, 255, 255))
            else :
                text = my_font.render(f"{inf}-{sup}", False, (255, 255, 255))
            screen.blit(text, (10+((k-ind_min)//42)*borne_width, 50 + ((k-ind_min)%42)*borne_heigth))

    def display_res() :
        text = my_font.render(f"Result : {res}", False, (255, 255, 255))
        screen.blit(text, (10, 20))

    def display_input(input) :
        text = my_font.render(f"Line : {input}", False, (255, 255, 255))
        screen.blit(text, (400, 20))

    with open("input") as file :
        for lines in file :
            line = lines.split()
            if line :
                line = line[0]
                inf, sup = [int(i) for i in line.split("-")]
                for i, (bi, bs) in enumerate(bornes) :
                    if bi <= inf and sup <= bs :
                        for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                    return False
                                if event.type == pygame.KEYDOWN :
                                    if event.key == pygame.K_ESCAPE :
                                        return False
                        screen.fill((0,0,0))
                        display_bornes(i)
                        display_res()
                        display_input(line)
                        pygame.display.update()
                        sleep(sleep_time)
                        break
                    if inf <= bi and bi <= sup <= bs :
                        for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                    return False
                                if event.type == pygame.KEYDOWN :
                                    if event.key == pygame.K_ESCAPE :
                                        return False
                        screen.fill((0,0,0))
                        display_bornes(i)
                        display_res()
                        display_input(line)
                        pygame.display.update()
                        # sleep(sleep_time)
                        bornes[i] = [inf, bs]
                        j = i-1
                        while j>=0 and bornes[j][1] >= bornes[i][0] :
                            for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                    return False
                                if event.type == pygame.KEYDOWN :
                                    if event.key == pygame.K_ESCAPE :
                                        return False
                            if bornes[j][0] <= inf :
                                bornes[i] = [bornes[j][0], bs]
                            screen.fill((0,0,0))
                            display_bornes(i, [j+1], [i-1])
                            display_res()
                            display_input(line)
                            pygame.display.update()
                            clock = pygame.time.Clock()
                            clock.tick(speed)
                            j = j-1
                        screen.fill((0,0,0))
                        display_bornes(i, [j+1], [i-1])
                        display_res()
                        display_input(line)
                        pygame.display.update()
                        clock = pygame.time.Clock()
                        clock.tick(speed)
                        sleep(sleep_time)
                        for p in range(i-j-1) :
                            for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                    return False
                                if event.type == pygame.KEYDOWN :
                                    if event.key == pygame.K_ESCAPE :
                                        return False
                            del bornes[j+1]
                            screen.fill((0,0,0))
                            display_bornes(i-p-1, [j+1], [i-2-p])
                            display_res()
                            display_input(line)
                            pygame.display.update()
                            clock = pygame.time.Clock()
                            clock.tick(speed)
                        break
                    if bs >= inf >= bi and bs <= bornes[i][1] :
                        for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                    return False
                                if event.type == pygame.KEYDOWN :
                                    if event.key == pygame.K_ESCAPE :
                                        return False
                        screen.fill((0,0,0))
                        display_bornes(i)
                        display_res()
                        display_input(line)
                        pygame.display.update()
                        # sleep(sleep_time)
                        bornes[i] = [bi, sup]
                        k = i+1
                        while k < len(bornes) and bornes[k][0] <= bornes[i][1] :
                            for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                    return False
                                if event.type == pygame.KEYDOWN :
                                    if event.key == pygame.K_ESCAPE :
                                        return False
                            if bornes[k][1] >= sup :
                                bornes[i] = [bi, bornes[k][1]]
                            screen.fill((0,0,0))
                            display_bornes(i, [i+1], [k-1])
                            display_res()
                            display_input(line)
                            pygame.display.update()
                            clock = pygame.time.Clock()
                            clock.tick(speed)
                            k += 1
                        screen.fill((0,0,0))
                        display_bornes(i, [i+1], [k-1])
                        display_res()
                        display_input(line)
                        pygame.display.update()
                        clock = pygame.time.Clock()
                        clock.tick(speed)
                        sleep(sleep_time)
                        for p in range(k-i-1) :
                            for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                    return False
                                if event.type == pygame.KEYDOWN :
                                    if event.key == pygame.K_ESCAPE :
                                        return False
                            del bornes[i+1]
                            screen.fill((0,0,0))
                            display_bornes(i, [i+1], [k-p-2])
                            display_res()
                            display_input(line)
                            pygame.display.update()
                            clock = pygame.time.Clock()
                            clock.tick(speed)
                        break
                    if inf <= bi and bs <= sup :
                        for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                    return False
                                if event.type == pygame.KEYDOWN :
                                    if event.key == pygame.K_ESCAPE :
                                        return False
                        screen.fill((0,0,0))
                        display_bornes(i)
                        display_res()
                        display_input(line)
                        pygame.display.update()
                        # sleep(sleep_time)
                        bornes[i] = [inf, sup]
                        j = i-1
                        while j>=0 and bornes[j][1] >= bornes[i][0] :
                            for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                    return False
                                if event.type == pygame.KEYDOWN :
                                    if event.key == pygame.K_ESCAPE :
                                        return False
                            if bornes[j][0] <= inf :
                                bornes[i] = [bornes[j][0], sup]
                            screen.fill((0,0,0))
                            display_bornes(i, [j+1], [i-1])
                            display_res()
                            display_input(line)
                            pygame.display.update()
                            clock = pygame.time.Clock()
                            clock.tick(speed)
                            j = j-1
                        k = i+1
                        while k < len(bornes) and bornes[k][0] <= bornes[i][1] :
                            for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                    return False
                                if event.type == pygame.KEYDOWN :
                                    if event.key == pygame.K_ESCAPE :
                                        return False
                            if bornes[k][1] >= sup :
                                bornes[i] = [bornes[i][0], bornes[k][1]]
                            screen.fill((0,0,0))
                            display_bornes(i, [j+1, i+1], [i-1, k-1])
                            display_res()
                            display_input(line)
                            pygame.display.update()
                            clock = pygame.time.Clock()
                            clock.tick(speed)
                            k += 1
                        screen.fill((0,0,0))
                        display_bornes(i, [j+1, i+1], [i-1, k-1])
                        display_res()
                        display_input(line)
                        pygame.display.update()
                        sleep(sleep_time)
                        for p in range(i-j-1) :
                            for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                    return False
                                if event.type == pygame.KEYDOWN :
                                    if event.key == pygame.K_ESCAPE :
                                        return False
                            del bornes[j+1]
                            screen.fill((0,0,0))
                            display_bornes(i-p-1, [j+1, i-p], [i-2-p, k-p])
                            display_res()
                            display_input(line)
                            pygame.display.update()
                            clock = pygame.time.Clock()
                            clock.tick(speed)
                        # sleep(sleep_time)
                        for p in range(k-i-1) :
                            for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                    return False
                                if event.type == pygame.KEYDOWN :
                                    if event.key == pygame.K_ESCAPE :
                                        return False
                            del bornes[i+1-(i-j-1)]
                            screen.fill((0,0,0))
                            display_bornes(i-(i-j-1), [i-(i-j-1), j+1], [k-p-2-(i-j-1), i-p-1-(i-j-1)-1])
                            display_res()
                            display_input(line)
                            pygame.display.update()
                            clock = pygame.time.Clock()
                            clock.tick(speed)
                        break
                else :
                    bornes.append([int(i) for i in line.split("-")])
                    bornes.sort()
                    screen.fill((0,0,0))
                    display_bornes()
                    display_res()
                    display_input(line)
                    pygame.display.update()
                    sleep(sleep_time)
            else :
                for i in range(len(bornes)) :
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            return False
                        if event.type == pygame.KEYDOWN :
                            if event.key == pygame.K_ESCAPE :
                                return False
                    inf, sup = bornes[i]
                    res += sup - inf + 1
                    screen.fill((0,0,0))
                    display_bornes(ind_min = i+1)
                    display_res()
                    pygame.display.update()
                    clock = pygame.time.Clock()
                    clock.tick(10)
                break
    return True


run = True

while run :
    run = animate()
    if run :
        sleep(2)

pygame.quit()
