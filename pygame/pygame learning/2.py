#drawing graphic per:
import pygame

pygame.init()

W, H=600, 400
sc=pygame.display.set_mode((600, 400))
pygame.display.set_caption("графические примитивы")

pygame.draw.rect(sc, (255,255,255), (10,10,50,100))
pygame.display.flip() #use "flip" function to demonstrate object on screen;

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit()