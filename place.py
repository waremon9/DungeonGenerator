import pygame

class Place():

    def __init__(self, nb):
        self.North = None
        self.East = None
        self.South = None
        self.West = None
        self.nb = nb
        self.X = None
        self.Y = None

        
    def nbConnection(self):
        x=0
        if (self.North != None):
            x = 1
        if (self.East != None):
            x += 1            
        if (self.South != None):
            x = x+1
        if (self.West != None):
            x -= -1
        return x

    def setPosition(self, x, y):
        self.X=x
        self.Y=y
