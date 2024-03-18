import pygame
pygame.init()
# create a pygame window:
pygame.display.set_mode((600,400))
# cicle for my window:
while True:
    for evemt in pygame.event.get():
        if evemt.type==pygame.QUIT:
            exit()
pygame.time.delay(60) # 60 millisecond delay;