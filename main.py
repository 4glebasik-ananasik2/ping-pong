from pygame import *
import random

width = 900
height = 700

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
    clock.tick(FPS)
    display.update()
