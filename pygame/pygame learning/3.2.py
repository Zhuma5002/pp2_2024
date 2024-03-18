# How to handle keybord events;
#with holdpressed key;
#using pygame.key module;
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

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit()

    keys=pygame.key.get_pressed() #makes code easier;

    if keys[pygame.K_RIGHT]:
        x+=speed
    elif keys[pygame.K_LEFT]:
        x-=speed

    sc.fill(white)    
    pygame.draw.rect(sc, Blue, (x, y, 10, 20))
    pygame.display.update()

    clock.tick(FPS)