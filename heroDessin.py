import pygame

class HeroDessin():

    def __init__(self):
         self.X = 800
         self.Y = 415
         self.size = 30

    def moveUp(self, pixels, salle):
        self.Y -= pixels
        #Check that you are not going too far (off the screen)
        if salle == None:
            if self.Y < 30:
              self.Y = 30
        else:
            if self.Y < 30 and not(747<self.X<1018):
              self.Y = 30

    def moveDown(self, pixels, salle):
        self.Y += pixels
        #Check that you are not going too far (off the screen)
        if salle == None:
            if self.Y > 772:
                self.Y = 772
        else:
            if self.Y > 772 and not(747<self.X<1018):
              self.Y = 772

    def moveLeft(self, pixels, salle):
        self.X -= pixels
        #Check that you are not going too far (off the screen)
        if salle == None:
            if self.X < 234:
                self.X = 234
        else:
            if self.X < 234 and not(265<self.Y<535):
              self.X = 234
          
    def moveRight(self, pixels, salle):
        self.X += pixels
        #Check that you are not going too far (off the screen)
        if salle == None:
            if self.X > 1541:
                self.X = 1541
        else:
            if self.X > 1541 and not(265<self.Y<535):
              self.X = 1541
