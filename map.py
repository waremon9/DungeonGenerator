import pygame
from place import Place
from random import randint

class Map():

    def __init__(self, screen, SIZEX, SIZEY, size):

        #each maze has 10 places (will be in parameter later)
        nbPlace = size
        
        #create a tab with all the places
        maze = []
        for i in range(nbPlace):
            maze.append(Place(i))

        #list of coord already taken to not have overlaping place.
        listeCoord = []

        #Every places
        for place in maze:
            #except 0 (the first one)
            if place.nb == 0:
                place.setPosition(0,0)
                listeCoord.append((0,0))
            else:
                #start searching empty space from an randomly selected already placed palce
                current_place = maze[randint(0,place.nb-1)]
                posX, posY = current_place.X,current_place.Y
                pasOk = True
                #randomly go N/E/S/W until it find a empty space
                while (pasOk):
                    x = randint(0,3)
                    if (x==0):
                        posY += 1
                        if (current_place.North!=None):
                            current_place = current_place.North
                        else:
                            current_place.North = place
                            place.South = current_place
                            pasOk = False
                    elif (x==1):
                        posX += 1
                        if (current_place.East!=None):
                            current_place = current_place.East
                        else:
                            current_place.East = place
                            place.West = current_place
                            pasOk = False
                    elif (x==2):
                        posY -= 1
                        if (current_place.South!=None):
                            current_place = current_place.South
                        else:
                            current_place.South = place
                            place.North = current_place
                            pasOk = False
                    elif (x==3):
                        posX -= 1
                        if (current_place.West!=None):
                            current_place = current_place.West
                        else:
                            current_place.West = place
                            place.East = current_place
                            pasOk = False
                    if (pasOk == False):
                        azer=False
                        for coord in listeCoord:
                            if (coord == (posX,posY) or not(-4<posX<4) or not(-4<posY<4)):
                                azer=True
                                pasOk = True
                                if(x==0):
                                    current_place.North=None
                                    place.South=None
                                if(x==1):
                                    current_place.East=None
                                    place.West=None
                                if(x==2):
                                    current_place.South=None
                                    place.North=None
                                if(x==3):
                                    current_place.West=None
                                    place.East=None
                        if azer:
                            current_place = maze[randint(0,place.nb-1)]
                            posX, posY = current_place.X,current_place.Y
                listeCoord.append((posX,posY))
                place.setPosition(posX,posY)

        self.maze = maze
