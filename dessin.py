import pygame
from map import Map
from globals import globals as G


class Dessin:
    
    # Define some colors
    BLACK = (0,0,0)
    WHITE = (255,255,255)
    NOT_WHITE = (200,200,200)
    RED = (255,0,0)
    LIGHT_RED = (255,100,100)
    GREEN = (0,255,0)
    LIGHT_GREEN = (190,255,120)
    BLUE = (0,0,255)

    @staticmethod
    def drawScene(maze, salle, hero, startMapX, startMapY, sizeMapX, sizeMapY, decalX, decalY, nextSalle):
        G['screen'].fill(Dessin.BLACK)
        Dessin.drawRoom(salle, startMapX, startMapY, sizeMapX, sizeMapY, decalX, decalY)
        if(decalY!=0):
            Dessin.drawRoom(nextSalle, startMapX, startMapY, sizeMapX, sizeMapY, 0, -sizeMapY+decalY)
        if(decalX !=0):
            Dessin.drawRoom(nextSalle, startMapX, startMapY, sizeMapX, sizeMapY, -sizeMapX+decalX, 0)
        pygame.draw.rect(G['screen'],Dessin.BLACK,pygame.Rect(0,0,startMapX,G["SIZEY"]))
        Dessin.drawBorder()
        Dessin.drawMap(maze, salle)
        Dessin.drawHeroRoom(hero)
        pygame.display.flip()

    @staticmethod
    def drawBorder():
        pygame.draw.line(G['screen'], Dessin.NOT_WHITE, [0, 4], [G['SIZEX'], 4], 10)
        pygame.draw.line(G['screen'], Dessin.NOT_WHITE, [0, G['SIZEY']-4], [G['SIZEX'], G['SIZEY']-4], 10)
        pygame.draw.line(G['screen'], Dessin.NOT_WHITE, [4, 5], [4, G['SIZEY']-5], 10)
        pygame.draw.line(G['screen'], Dessin.NOT_WHITE, [G['SIZEX']-5, 5], [G['SIZEX']-5, G['SIZEY']-5], 10)
        pygame.draw.line(G['screen'], Dessin.NOT_WHITE, [208, 4], [208, G['SIZEY']-5], 10)
        pygame.draw.line(G['screen'], Dessin.NOT_WHITE, [0, 208], [213, 208], 10)
        
    @staticmethod
    def drawMap(maze, salle):
        for place in maze:
            if(place.North!=None):
                pygame.draw.line(G['screen'], Dessin.WHITE, [100+place.X*25+4, 100+place.Y*-25+4], [100+place.X*25+4, 100+place.Y*-25-9], 2)
            if(place.East!=None):
                pygame.draw.line(G['screen'], Dessin.WHITE, [100+place.X*25+4, 100+place.Y*-25+4], [100+place.X*25+17, 100+place.Y*-25+4], 2)
            if(place.South!=None):
                pygame.draw.line(G['screen'], Dessin.WHITE, [100+place.X*25+4, 100+place.Y*-25+4], [100+place.X*25+4, 100+place.Y*-25+17], 2)
            if(place.West!=None):
                pygame.draw.line(G['screen'], Dessin.WHITE, [100+place.X*25+4, 100+place.Y*-25+4], [100+place.X*25-9, 100+place.Y*-25+4], 2)
            if place.nb==salle.nb :
                pygame.draw.rect(G['screen'],Dessin.RED,pygame.Rect(100+place.X*25,100+place.Y*-25,10,10))
            else:
                pygame.draw.rect(G['screen'],Dessin.WHITE,pygame.Rect(100+place.X*25,100+place.Y*-25,10,10))

    @staticmethod
    def drawRoom(place, startX, startY, sizeMapX, sizeMapY, decalX, decalY):
        #NORTH
        if(place.North == None):
            pygame.draw.line(G['screen'], Dessin.WHITE, [startX+decalX, startY+10+decalY], [startX+sizeMapX+decalX, startY+10+decalY], 20)
        else:
            pygame.draw.line(G['screen'], Dessin.WHITE, [startX+decalX, startY+10+decalY], [int(startX+sizeMapX/2-154)+decalX, startY+10+decalY], 20)
            pygame.draw.line(G['screen'], Dessin.WHITE, [int(startX+sizeMapX/2+147)+decalX, startY+10+decalY], [startX+sizeMapX+decalX, startY+10+decalY], 20)
        #SOUTH
        if(place.South == None):
            pygame.draw.line(G['screen'], Dessin.WHITE, [startX+decalX, startY+sizeMapY-10+decalY], [startX+sizeMapX+decalX, startY+sizeMapY-10+decalY], 20)
        else:
            pygame.draw.line(G['screen'], Dessin.WHITE, [startX+decalX, startY+sizeMapY-10+decalY], [int(startX+sizeMapX/2-154)+decalX, startY+sizeMapY-10+decalY], 20)
            pygame.draw.line(G['screen'], Dessin.WHITE, [int(startX+sizeMapX/2+147)+decalX, startY+sizeMapY-10+decalY], [startX+sizeMapX+decalX, startY+sizeMapY-10+decalY], 20)
        #EAST
        if(place.East == None):
            pygame.draw.line(G['screen'], Dessin.WHITE, [startX+sizeMapX-10+decalX, startY+10+decalY], [startX+sizeMapX-10+decalX, startY+sizeMapY+decalY], 20)
        else:
            pygame.draw.line(G['screen'], Dessin.WHITE, [startX+sizeMapX-10+decalX, startY+10+decalY], [startX+sizeMapX-10+decalX, int(startY+sizeMapY/2-150)+decalY], 20)
            pygame.draw.line(G['screen'], Dessin.WHITE, [startX+sizeMapX-10+decalX, int(startY+sizeMapY/2+150)+decalY], [startX+sizeMapX-10+decalX, startY+sizeMapY+decalY], 20)
        #WEST
        if(place.West == None):
            pygame.draw.line(G['screen'], Dessin.WHITE, [startX+10+decalX, startY+10+decalY], [startX+10+decalX, startY+sizeMapY+decalY], 20)
        else:
            pygame.draw.line(G['screen'], Dessin.WHITE, [startX+10+decalX, startY+10+decalY], [startX+10+decalX, int(startY+sizeMapY/2-150)+decalY], 20)
            pygame.draw.line(G['screen'], Dessin.WHITE, [startX+10+decalX, int(startY+sizeMapY/2+150)+decalY], [startX+10+decalX, startY+sizeMapY+decalY], 20)

    @staticmethod
    def drawHeroRoom(hero):
        pygame.draw.circle(G['screen'],Dessin.BLUE,(hero.X+15, hero.Y+15),15)

    @staticmethod
    def transition1():
        nb = int(G['SIZEY']/5)
        for i in range(5):
            x = 0
            while x<G['SIZEX']:
                pygame.draw.rect(G['screen'],Dessin.RED,pygame.Rect(x,nb*i,20,nb))
                pygame.display.flip()
                x+=15

    @staticmethod
    def transition2():
        nb = int(G['SIZEX']/8)
        for i in range(8):
            y = 0
            while y<G['SIZEY']:
                pygame.draw.rect(G['screen'],Dessin.BLUE,pygame.Rect(nb*i,y,nb,11))
                pygame.display.flip()
                y+=11
            
        
