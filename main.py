import pygame
import time
from random import randint
import ctypes
import os
from map import Map
from dessin import Dessin
from heroDessin import HeroDessin
from globals import *

speed = 20

#the windows start at the top-left corner.
x = 0
y = 30
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (x,y)
pygame.init()

#do not show the mouse cursor
pygame.mouse.set_visible(False)

# The clock will be used to control how fast the screen updates
clock = pygame.time.Clock()

#List that will contain all the sprites we intend to use in our game.
all_sprites_list = pygame.sprite.Group()

# Open a new window
user32 = ctypes.windll.user32
SIZEX = user32.GetSystemMetrics(0)
SIZEY = user32.GetSystemMetrics(1)-70
screen = pygame.display.set_mode((SIZEX,SIZEY))
globals['SIZEX'] = SIZEX
globals['SIZEY'] = SIZEY
globals['screen'] = screen
pygame.display.set_caption("Game")


startMapX = 213
startMapY = 9
sizeMapX = SIZEX-223
sizeMapY = SIZEY-18

mapA = Map(screen, SIZEX, SIZEY, 15)
salleActu = mapA.maze[0]
hero = HeroDessin()

carryOn = True
while carryOn:
    # --- Main event loop
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
              carryOn = False # Flag that we are done so we exit this loop
        elif event.type==pygame.KEYDOWN:
                if event.key==pygame.K_ESCAPE: #Pressing the escape Key will quit the game
                    carryOn=False

    #look at the key pressed
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        hero.moveUp(speed, salleActu.North)
    if keys[pygame.K_DOWN]:
        hero.moveDown(speed, salleActu.South)
    if keys[pygame.K_LEFT]:
        hero.moveLeft(speed, salleActu.West)
    if keys[pygame.K_RIGHT]:
        hero.moveRight(speed, salleActu.East)

    #check if the hero go to a "door"
    #NORTH
    if hero.Y<10:
        for i in range(90):
            decalY = int(sizeMapY/90*(i+1))
            hero.Y = startMapY+int(sizeMapY/90*(i+1))
            Dessin.drawScene(mapA.maze, salleActu, hero, startMapX, startMapY, sizeMapX, sizeMapY, 0, decalY, salleActu.North)
        salleActu = salleActu.North
        hero.Y = 785
    #SOUTH
    if hero.Y>785:
        salleActu = salleActu.South
        for i in range(90):
            decalY = sizeMapY-int(sizeMapY/90*(i+1))
            hero.Y = startMapY+sizeMapY-int(sizeMapY/90*(i+1))
            Dessin.drawScene(mapA.maze, salleActu, hero, startMapX, startMapY, sizeMapX, sizeMapY, 0, decalY, salleActu.North)
        hero.Y = 10
    #WEST
    if hero.X<214:
        for i in range(120):
            decalX = int(sizeMapX/120*(i+1))
            hero.X = startMapX+int(sizeMapX/120*(i+1))
            Dessin.drawScene(mapA.maze, salleActu, hero, startMapX, startMapY, sizeMapX, sizeMapY, decalX, 0, salleActu.West)
        salleActu = salleActu.West
        hero.X = 1561
    #EAST
    if hero.X>1561:
        salleActu = salleActu.East
        for i in range(120):
            decalX = sizeMapX-int(sizeMapX/120*(i+1))
            hero.X = startMapX+sizeMapX-int(sizeMapX/120*(i+1))
            Dessin.drawScene(mapA.maze, salleActu, hero, startMapX, startMapY, sizeMapX, sizeMapY, decalX, 0, salleActu.West)
        hero.X = 214
        

    Dessin.drawScene(mapA.maze, salleActu, hero, startMapX, startMapY, sizeMapX, sizeMapY, 0, 0, None)
    
    # --- Limit to 60 frames per second
    clock.tick(60)
 
#stop the game engine when main program exited
pygame.quit()
