# Defining a circular array attempt

import pygame
import numpy as np

pygame.init()

#colors
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
gameDisplay = pygame.display.set_mode((800,600))
gameDisplay.fill(black)

# block settings
l = 15
b = 15

#circle
w = np.linspace(0.0, 360.0, num=100)
r = 200
offset = 300
x = [ r*np.cos(i) for i in w]
y = [ r*np.sin(i) for i in w]

for i in range(len(x)):
    pygame.draw.rect(gameDisplay, red, (x[i]+offset+l ,y[i]+offset+b,l,b))

pygame.draw.rect(gameDisplay, red, (0,0,l,b))
pygame.draw.rect(gameDisplay, green, (800-l,600-b,l,b))

#pygame.draw.circle(gameDisplay, white, (150,150), 75)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    pygame.display.update()
