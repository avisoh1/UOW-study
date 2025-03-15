# Lecture 3 07/10/2024
class Point:
    pass

    def greet(self):
        return " ..."   # always go to terminal/console. No printing in function method
    
    def __str__(self):
        return "._str_." # will print str method instead of location if available
    
p1 = Point()
print(p1.greet())       # 10     # object.method() <== this is the way
print(Point.greet(p1))  # for this class Point, run greet() with this object p1
                        # p1 then become the self parameter.(self replaced by p1)
# Point.greet() # missing 1 argument
Point.greet(x) # correct version

pp = Person()   # does it work?
Point.greet(pp)

input()

print(p1)
print(type(p1))

p2 = Point()
p1.x = 3
p2.y = 6

print(p1.__dict__) # x = 3
print(p2.__dict__) # y = 6

print(p1.greet())
print(p2.greet())

import math
class Point:
    def __init__(self,x = 0,y = 0):
        # self.x = 0        # self.x is yhe instance
        # self.y = 0
        self.move(x,y)

    def move(self,x,y):
        self.x = x
        self.y = y

    def reset(self):
        self.move(0,0)

    def calculate_distance(self,other_point):
        return math.sqrt(self.x - other_point.x)**2 +(self.y - other_point.y)**2

# p1 is a Point object, or an instance of Point class
p1 = Point() # a Point object with x,y attributes, if have default on init then no need put also ok
p2 = Point(5,0) # a Point object with x,y attributes'
p1.reset()   # set the point to (0,0) # forget do reset point 1 and point 2 will have problem. Therefore the solution is declare the init function
p2.move(5,5) # no way to do this, so we have move function
print(p2.calculate_distance(p1))
print(p1.calculate_distance(p1))

import math
class Point:
    start_point_x = 0   # class_variables, pg18
    start_point_y = 0   # one copy shared among all Point objects

    def __init__(self,x=start_point_x, y=start_point_y):
        self.move(x,y)

    def move(self,x,y):
        self.x = x
        self.y = y

    def reset(self):
        self.move(Point.start_point_x,Point.start_point_y)

    def calculate_distance(self,other_point):
        return math.sqrt(self.x - other_point.x)**2 +(self.y - other_point.y)**2
    
    def change_start_point(self,x,y):
        Point.start_point_x = x
        Point.start_point_y = y
    
    @ classmethod
    def change_start_point(cls, other_point):
        
print(Point.start_point_x,Point.start_point_y) # 0,0
p1 = Point() #(0,0)
p1.change_start_point(1,1)
p2 = Point()    # stiLL(,1,)
print(p1.start_point_y,p2.start_point_y)
print(p1.__dict__)
print(p2.__dict__)
print(Point.start_point_x,Point.start_point_y)
p2.reset()  # moving to (1,1)
print(p2.__dict__)
print(Point.x,Point.y) # print787(p1.x,p1.y)

# Sentinel Default Value
print(Point.start_point_x,Point.start_point_y) # 0,0
p1.change_start_point(1,1)
p2 = Point()    # stiLL(1,1)
print(p1.start_point_x,p2.start_point_y)
print(p1.__dict__)
print(p2.__dict__)
p2.change_start_point(10,10)
p1.reset()
print(Point.start_point_x,Point.start_point_y)
print(p1.__dict__)
print(p2.__dict__)
Point.change_start_point(10,10)

# Final code for class Point

import math

class Point:
    _start_point_x = 0     # use protected, later child class can reference
    _start_point_y = 0
    
    def __init__(self, x=None, y=None):
        if x is None and y is None:
            self.move(Point._start_point_x, Point._start_point_y)
        else:
            self.move(x,y)
            
    def move(self, x, y):
        self.__x = y      # make instance variable private
        self.__y = y

    def reset(self):
        self.move(Point._start_point_x, Point._start_point_y)

    def calculate_distance(self, other_point):
        return math.sqrt((self.__x - other_point.__x)**2 + (self.__y - other_point.__y)**2)
    
    @classmethod
    def change_start_point(cls,x,y):   # cls is the shorthand for class
        cls._start_point_x = x
        cls._start_point_y = y
        
    @staticmethod
    def greet():
        print("Hello world")
    
    def __secret_message(self):
        print("This is a secret!")
        
    def __str__(self):
        return "({}, {})".format(self.__x, self.__y)
        

print(Point._start_point_x, Point._start_point_y)
p1 = Point()
print(p1.__str__())
p1._Point__secret_message()  # still can access this private method
                             # python do not restrict, but make it difficult

Point.change_start_point(10,10)  # call class method

p2 = Point()
print(p2)

print(p1.calculate_distance(p2))
