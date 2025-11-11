class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def getWidth(self):
        return self.width

    def getHeight(self):
        return self.height

    def getArea(self):
        return self.height * self.width

class Circle:
    def __init__(self, r):
        self.r = r

    def getAreaCircle(self):
        return 3.14 * self.r ** 2

class Triangle:
    def __init__(self, a, h):
        self.a = a
        self.h = h

    def getAreaTriangle(self):
        return self.a * self.h

