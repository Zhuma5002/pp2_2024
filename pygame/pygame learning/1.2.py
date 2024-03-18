import pygame
pygame.init()
# create a pygame window:
pygame.display.set_mode((600,400))
# cicle for my window:
clock=pygame.time.Clock()
while True:
    for evemt in pygame.event.get():
        if evemt.type==pygame.QUIT:
            exit()
clock.tick(60) #frames per second (FPS);
