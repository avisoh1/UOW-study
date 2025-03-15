import math
class Point:
    def __init__(self,x:float,y:float):
        """
        constructor create a Point object given the x, y coordinates
        """
        self.__x = x
        self.__y = y
    
    def getX(self):
        return self.__x
    
    def getY(self):
        return self.__y
    
    def __str__(self):
        return "{},{}".format(self.__x,self.__y)
    
class Circle(Point):
    def __init__(self,center:Point,radius:float):
        """
        constructor create a circle object given the center (Point object) and the radius
        """
        self.__center = center
        self.__radius = radius

    def area(self):
        return math.pi * self.__radius * self.__radius
    
    def circumference(self):
        return 2 * self.__radius * math.pi
    
    def pointCoordinates(self,angle:float):
        x = self.__radius * math.cos(angle) + self.__center.getX()
        y = self.__radius * math.cos(angle) + self.__center.getY()
        return Point(x,y) # create a Point with x,y

if __name__=='__main__':

    p = Point(0,2)
    print(p)
    print(p.getX())

    c= Circle(p,5)
    print(c.area())
    print(c.circumference())
    print(c.pointCoordinates(30))

"""
next file
from PointCircle import Circle,Point
c = Circle(Point(5,5),6)
print(c.area())
print(c.circumference())
print(c.pointCoordinates(0))
"""