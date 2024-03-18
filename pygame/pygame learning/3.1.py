# How to handle keybord events;
#with holdpressed key;
import pygame

pygame.init()

W=600
H=400

sc=pygame.display.set_mode((W, H))
pygame.display.set_caption("keybord events")
white=(255, 255, 255)
Blue=(0, 0, 255)
Green=(0, 255, 0)
Red=(255, 0, 0)

FPS=60 # frames per second;
clock=pygame.time.Clock()

x=W // 2
y=H // 2
speed=5 

flleft=flright=False
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit()
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                flleft=True
            elif event.key==pygame.K_RIGHT:
                flright=True
        elif event.type==pygame.KEYUP:
            if event.key in [pygame.K_LEFT, pygame.K_RIGHT]:
                flleft=flright=False
    if flleft:
        x-=speed
    elif flright:
        x+=speed

    sc.fill(white)    
    pygame.draw.rect(sc, Blue, (x, y, 10, 20))
    pygame.display.update()

    clock.tick(FPS)