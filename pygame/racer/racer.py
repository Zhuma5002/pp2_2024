import pygame
import time
import random

pygame.init()

clock=pygame.time.Clock()

Black=(0, 0, 0)
Red=(255, 0, 0)
Green=(0, 255, 0)
Blue=(0, 0, 255)

sc_width=500
sc_height=400
sc=pygame.display.set_mode((sc_width, sc_height))
pygame.display.set_caption("Race car with road block")

#image
bg=pygame.image.load("track.png")
carimg=pygame.image.load("porsche.png")

westb=157 #уствновил границы за которые тачка не сможет выходить.
eastb=359

class Block: # create block
    def __init__(self, x, y, width, height):
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.speedy=5 # starting speed on y coordinate
        self.dodged=0 # dodged block score
    
    def update(self):
        self.y= self.y+self.speedy # update block coordinates on screen

        # check block boundary:
        if self.y>sc_height:
            self.y=0-self.height
            self.x=random.randrange(westb, eastb-self.width)
            self.dodged=self.dodged+1 # добавляет +1 к счетчику если тачка проехал блок

    def draw(self, sc): # draw block:
        pygame.draw.rect(sc, Black, [self.x, self.y,  self.width, self.height])

class Player:
    def __init__(self):
        self.image=carimg # эта строка устанавливает картину машины
        self.height=self.image.get_height() #Эта строка определяет высоту объекта

        self.rect=self.image.get_rect() # Эта строка создает прямоугольник (Rect), который описывает область, занимаемую изображением image
        self.rect.x = int(sc_width / 2 - self.rect.width / 2)
        self.rect.y = int(sc_height / 2 - self.rect.height / 2) # Эти строки устанавливают начальное положение объекта игрока по горизонтали и вертикали.

        self.speedx=0 # устанавливает начальную скорость перемещения объекта игрока по горизонтали

    def update(self):
        key=pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            self.speedx=-10  # установил скорости перемещеня по горизонтали при нажатии лефт и райт клавиш
        if key[pygame.K_RIGHT]:
            self.speedx=10
        
        self.rect.x=self.rect.x+self.speedx # эта строка обновляет позицию по горизонтали добовляя текущую скорость

        #check boundaries:
        if self.rect.left<westb:
            self.rect.left=westb
        if self.rect.right>eastb:
            self.rect.right=eastb # эти строки проверяют чтобы тачка не выходила за пределы трассы

def score_board(dodged):
    font=pygame.font.Font(None, 25)
    text=font.render("score:"+str(dodged), True, Red)
    sc.blit(text, (0, 0))

# check if the block crashes my porsche:
def crash(): # определает юыла ли авария
    font=pygame.font.Font(None, 80) # создает шрифт размером 80 
    text=font.render("LOH!", True, Red)# задаем что отображать
    text_width=text.get_width()
    text_height=text.get_height() # ширина и высота текста
    x=int(sc_width/2-text_width/2)
    y=int(sc_height/2-text_height/2) # координаты текста лох
    sc.blit(text, (x, y)) # рисует текст
    pygame.display.update()
    time.sleep(2) # задержка текста на 2 секунды.
    game_loop() # вызывает функцию гейм луп чтобы начать новуб игру.


#def game function
def game_loop():
    block_width= 80 # размеры блока
    block_height=20
    block_x=random.randrange(westb, eastb-block_width)
    block_y=-100 # начальная координата по оси у для блока

    player=Player()
    block=Block(block_x, block_y, block_width, block_height) # созлает обьект блока
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
        player.update()
        block.update()
        sc.blit(bg, (0, 0))  
        sc.blit(player.image, (player.rect.x, player.rect.y))   
        block.draw(sc)  
        if player.rect.right>block.x and player.rect. x<block.x+block.width: # проверяет, находится ли правая сторона тачки справа от левой стороны блока и одновременно левая сторона тачки слева от правой стороны блока 
            if block.y+block.height>player.rect.y and block.y<player.rect.bottom: # находится ли нижняя сторона блока ниже верхней стороны тачки и одновременно верхняя сторона блока выше нижней стороны тачки
                crash() # если да, то краш. а если нет то летс го дальше

        score_board(block.dodged)
        pygame.display.update()
        clock.tick(60) # FPS
        

#Main loop
game_loop()
        
        

pygame.quit()
quit()