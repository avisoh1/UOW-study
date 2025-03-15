import math

class Point:
    def __init__(self, xValue: float, yValue: float): 
        # self - represents the object to be created
        """ 
        constuctor that create a Point object given the x,y coordinates
        """
        self.__x = xValue   # __ (dunder) ==> PRIVATE attribute
        self.__y = yValue 

    def getX(self):  # accessor
        return self.__x

    def getY(self):
        return self.__y

    def __str__(self):
        """
        returns a string representation of the Point object
        """
        return "({}, {})".format(self.__x, self.__y)


class Circle:
    def __init__(self, center: Point, radius: float): 
        """ 
        constuctor that create a circle object given the center point and radius
        """
        self.__center = center
        self.__radius = radius 

    def area(self):  
        return math.pi * self.__radius * self.__radius

    def circumference(self):
        return 2 * math.pi * self.__radius

    def pointCoordinates(self, angle: float) -> Point:
        x = self.__radius * math.cos(angle) + self.__center.getX()
        y = self.__radius * math.sin(angle) + self.__center.getY()
        return Point(x,y)

if __name__ == "__main__":
    # the following will be executed if running in main domain space
    p = Point(0,0)
    print( p.getX() )
    print(p)
    
    c = Circle(p, 1)
    print( c.circumference() )
    print( c.area() )
    result = c.pointCoordinates(0)
    print( type(result) )
    print( result )

