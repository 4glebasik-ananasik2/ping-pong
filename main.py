from pygame import *
import random

class GameSprite(sprite.Sprite):
    def __init__(self, picture, x, y, w, h, speed):
        super().__init__()
        self.image = transform.scale(image.load(picture), (w, h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y)) 

class Player(GameSprite):
    def update_r(self):
        global height
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < height - self.rect.height:
            self.rect.y += self.speed
    def update_l(self):
        global height
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < height - self.rect.height:
            self.rect.y += self.speed

class Ball(GameSprite):
    def __init__(self, picture, x, y, w, h, speed):
        super().__init__(picture, x, y, w, h, speed)
        self.speedx = speed
        self.speedy = speed
    def update(self):
        if self.rect.x >= width - self.rect.width or self.rect.x <= 0:
            self.speedx = self.speedx * -1
        if self.rect.y >= height - self.rect.height or self.rect.y <= 0:
            self.speedy = self.speedy * -1
        self.rect.x += self.speedx
        self.rect.y += self.speedy

width = 900
height = 700
rocket_1 = Player(picture = 'ложка-no-bg-preview (carve.photos).png', x = 10, y = 50, w = 60, h = 150, speed = 6)
rocket_2 = Player(picture = 'ложка-no-bg-preview (carve.photos).png', x = width - 70, y = 50, w = 60, h = 150, speed = 6)
#rocket_1 = Player('ложка-no-bg-preview (carve.photos).png', 10, 50, 120, 200, 10)

ball = Ball('сырники-no-bg-preview (carve.photos).png', 150, 200, 100, 100, 4)

font.init()
font1 = font.Font(None, 50)
loser1 = font1.render('игрок1 попал сырниками в родителей...', True, (255, 200, 240))
loser2 = font1.render('игрок2 промахнулся по сырнику...', True, (67, 67, 67))

window = display.set_mode((width, height))
display.set_caption('ping pong')
background = transform.scale(image.load('столик.png'), (width, height))

FPS = 120
game = True
final = False
clock = time.Clock()

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if final != True:
        window.blit(background, (0, 0))
        rocket_1.reset()
        rocket_1.update_l()
        rocket_2.reset()
        rocket_2.update_r()
        ball.reset()
        ball.update()
        if sprite.collide_rect(ball, rocket_1) or sprite.collide_rect(ball, rocket_2):
            ball.speedx *= -1
        if ball.rect.x < 10:
            final = True
            window.blit(loser1, (150, 200))
        if ball.rect.x > width - 10 - ball.rect.width:
            final = True
            window.blit(loser2, (150, 200))

    clock.tick(FPS)
    display.update()
