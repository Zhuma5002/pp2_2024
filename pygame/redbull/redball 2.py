#этот 2й код работает так чтобы мяч двигался при holding keys:
import pygame

pygame.init()

w = 800
h = 600

sc = pygame.display.set_mode((w, h))
pygame.display.set_caption("Redball")

white = (255, 255, 255)
Red = (255, 0, 0)

FPS = 60

clock = pygame.time.Clock()

radius = 25

posx = w // 2
posy = h // 2

flleft = flright = flup = fldown = False
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                flleft = True
            elif event.key == pygame.K_RIGHT:
                flright = True
            if event.key == pygame.K_UP:
                flup = True
            elif event.key == pygame.K_DOWN:
                fldown = True
        elif event.type == pygame.KEYUP:
            if event.key in [pygame.K_LEFT, pygame.K_RIGHT, pygame.K_DOWN, pygame.K_UP]:
                flleft = flright = flup = fldown = False

    if flleft:
        posx -= 20
    elif flright:
        posx += 20
    elif fldown:
        posy += 20
    elif flup:
        posy -= 20

    if posx - radius < 0:  
        posx = radius
    elif posx + radius > 800:  
        posx = 800 - radius
    if posy - radius < 0:  
        posy = radius
    elif posy + radius > 600:  
        posy = 600 - radius

    sc.fill(white)

    pygame.draw.circle(sc, Red, (posx, posy), radius)

    pygame.display.update()

    clock.tick(FPS)
