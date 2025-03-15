# add_student
# add_course

students = [Student(...),Student(...)]
courses = [Course(...),Course(...)]
ac = AcadTerm(....,students:list,courses:list)

ac.add_student(Student(...))
r1 = Result(Student(4),Course(121))     # ok to create
ac.add_result(result:Result)       # not ok to add, False or exception student 4 not in students

a = "hello"
a[0] = "M"
a.replace("h","m")
print(a)
# Still cannot change, because is immutable

# Can use this
b = a.replace("h","m")

l1 = [1,2,1]
l2 = [1,2,1]

print(l1 == l2)
print(id(l1),id(l2))

class Rectangle:
    def __init__(self,l,w):
        self.__length = l
        self.__width = w

    def area(self):
        return self.__length * self.__width
    
    def __eq__(self,other):
        if self.area() == other.area():
            return True
        return False
    
r1 = Rectangle(5,3)
r2 = Rectangle(5,3)
print(r1 == r2)
