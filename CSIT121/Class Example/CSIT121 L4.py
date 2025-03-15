# Inheritance
class Rectangle:
    def __init__(self,length,width):
        self.__length = length
        self.__width = width

    def area(self):
        return self.__length * self.__width
    
    def __str__(self):          # type(self) --> show what class the "self" is
        return "I am a {} and my area is {:.2f}".format(type(self),self.area())
    
class Square(Rectangle): # Square is-a Rectangle, inherit everything from Rectangle
    def __init__(self,length):
        super().__init__(length,length) # super inheritance
    
    def __str__(self):
        return "I am a {} and my area is {:.2f}".format("Square",self.area())


r = Rectangle(5,4)
print(r)
s=Square(5)
print(s)
