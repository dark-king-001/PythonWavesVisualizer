import pygame
import sys
import math as m
import os
from pygame.locals import *


# Type = input("Enter the wave:")
amp = int(input("Enter Amplitude:"))
freq = int(input("Enter Frequency:"))

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((1000, 400))

pygame.mouse.set_visible(0)

FULLRED = (255, 0, 0)
FULLGREEN = (0, 255, 0)
FULLBLUE = (0, 0, 255)

x_axis = pygame.Rect(0, 199, 1000, 2)
y_axis = pygame.Rect(100, 0, 2, 400)
pos = 0
while True:
    clock.tick(60)
    pygame.draw.rect(screen, (255,255,255), x_axis)
    pygame.draw.rect(screen, (255,255,255), y_axis)
    pygame.draw.circle(screen, (255,255,255), (pos, amp*m.sin(m.radians(pos)*freq) + 200), 1)
    pos+=1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    pygame.display.update()