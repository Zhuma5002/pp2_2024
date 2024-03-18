#drawing other figures:
import pygame

pygame.init()


sc=pygame.display.set_mode((600, 400))
pygame.display.set_caption("графические примитивы")
White=(255, 255, 255)
Blue=(0,0,255)
Green=(0,255,0)
RED=(255, 0, 0)
pygame.draw.rect(sc, Blue, (10,10,100,50),2) # добавляем толщину пикселям;
pygame.draw.line(sc, Green, (300,20),(550,50))# draw a pixel line;
pygame.draw.aaline(sc, Green, (300,40),(550,70))#draw a regular line;
pygame. draw.lines (sc, RED, True, [ (200, 80 ), (250, 80), (300, 200)], 2)
pygame.draw.aalines (sc, RED, True, [(300, 80), (350, 80), (400, 200)])

pygame.display.flip() #use "flip" function to demonstrate object on screen;

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit()