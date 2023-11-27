import pygame
import winsound
wn=pygame.display.set_mode((800,600))
pygame.init()

white=(255,255,255)
closewindow=False
while not closewindow:
    for i in pygame.event.get():
        if i.type==pygame.QUIT:
            closewindow=True
        if i.type==pygame.KEYDOWN:
            if i.type==pygame.K_w:
                exit()
    wn.fill(white)
    pygame.display.update()
pygame.quit()