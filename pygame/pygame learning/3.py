# How to handle keybord events:
#one pressed key;
import pygame

pygame.init()

W=600
H=400

sc=pygame.display.set_mode((W, H), pygame.RESIZABLE)
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
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                x-=speed
            elif event.key==pygame.K_RIGHT:
                x+=speed

    sc.fill(white)    
    pygame.draw.rect(sc, Blue, (x, y, 10, 20))
    pygame.display.update()

    clock.tick(FPS)