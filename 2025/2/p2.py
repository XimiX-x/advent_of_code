print(sum([sum([sum([sum([id if sum([id if (len(str(id))%n == 0 and sum(map(lambda x : int(x == str(id)[:len(str(id))//n]), [str(id)[i*len(str(id))//n: (i+1)*len(str(id))//n] for i in range(1, n)])) == n-1) else 0 for n in range(2, len(str(id))+1)]) >0 else 0 for id in range(int(bornes[0]), int(bornes[1])+1)]) if len(bornes) == 2 else 0 for bornes in [rangee.split("-")]]) for rangee in line.split(',')]) for line in open("input")]))

### And we animate

import pygame
import re
from time import sleep

pygame.init()
screen = pygame.display.set_mode((550, 350))

pygame.font.init()
my_font = pygame.font.SysFont('arial', 20)

def animate() :
    res = 0
    bad_ids = []
    with open("test") as file :
        for lines in file :
            for bornes in [rangee.split("-") for rangee in lines.split(",")] :
                if len(bornes) == 2 :
                    for id in range(int(bornes[0]), int(bornes[1])+1) :
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                return False
                            if event.type == pygame.KEYDOWN :
                                if event.key == pygame.K_ESCAPE :
                                    return False
                        screen.fill((0, 0, 0))
                        text_surface = my_font.render(f"Range : {bornes[0]} - {bornes[1]}", False, (255, 255, 255))
                        screen.blit(text_surface, (50, 100))
                        if re.search(r"\A(\d+)\1+\Z", str(id)) is not None :
                            text_surface = my_font.render(f"ID : {id}", False, (0, 255, 0))
                            bad_ids.append(id)
                            res += id
                        else :
                            text_surface = my_font.render(f"ID : {id}", False, (255, 0, 0))
                        screen.blit(text_surface, (50, 150))
                        text_surface = my_font.render(f"Result : {res}", False, (255, 255, 255))
                        screen.blit(text_surface, (50, 200))
                        text_surface = my_font.render("Bad IDs :", False, (255, 255, 255))
                        screen.blit(text_surface, (400, 50))
                        for i, id in enumerate(bad_ids) :
                            text_surface = my_font.render(f"{id}", False, (255, 255, 255))
                            screen.blit(text_surface, (400, 50 + 30*(len(bad_ids)-i)))
                        pygame.display.update()
                        clock = pygame.time.Clock()
                        clock.tick(20)
    return True

run = True

while run :
    run = animate()
    if run :
        sleep(2)

pygame.quit()
