#A Class which has two responsibility
#this Voilates the SRP

class Rectangle:
    def __init__(self, width = 0, height = 0):
        self.width = width
        self.heigth = height

    def draw(self):
        #Let's do some drawing
        pass

    def area(self):
        return self.width * self.heigth

#Correction
#Splitting classes into 2

class GeometricRectangle:
    def __init__(self, width = 0, height = 0):
        self.width = width
        self.heigth = height

    def area(self):
        return self.width * self.heigth

class DrawRectangle:
    def draw(self):
        #Let's do some drawing
        pass
