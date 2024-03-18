import pygame
pygame.init()
# create a pygame window:
pygame.display.set_mode((600,400))
pygame.display.set_caption("My first programm on pygame")# name my pygame window;
# cicle for my window:
while True:
    for evemt in pygame.event.get():
        if evemt.type==pygame.QUIT:
            exit()