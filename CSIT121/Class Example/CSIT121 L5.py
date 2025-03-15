class WorkIssueException(Exception):
    pass

class Employee:
    _ALLOCATED_LEAVE = 21 # children can access it
    _OT_BONUS = 1.5
    _OT_HRS = 8
    _MAX_RATE = 999

    def __init__(self,id,rate):
        """ constructor that execute when an object is created"""
        self.__id = id
        self.__rate = rate
        self.rate = rate
        self.__leaveBalance = type(self)._ALLOCATED_LEAVE    # cannot hardcord this class name

    @property
    def rate(self):
        return self.__rate
    
    @ rate.setter
    def rate(self,newRate:float):
        if newRate <= 0:
            raise WorkIssueException("unreasonable rate!!!")
        if newRate > 500:
            raise WorkIssueException("Sorry rate cannot be that high!!!")
        self.__rate = newRate

    def setLeaveBalance(self,newValue):
        self.__leaveBalance = newValue
    
    def computePay(self,hours):
        print("In Employee compute pay")
        if hours > type(self)._OT_HRS:
            return self.__rate *8 + self.__rate * (hours - 8) * type(self)._OT_BONUS
        else:
            return self.__rate * hours
    
    def __str__(self):
        return "ID:{} \t Rate:{} \t Leave:{} \t".format(self.__id, self.__rate,self.__leaveBalance)

class Manager(Employee):
    _ALLOCATED_LEAVE = 25 # children can access it, no need setter anymore
    _OT_BONUS = 1

    def __init__(self,id,rate,dept):
        super().__init__(id,rate)
        self.__dept = dept
        # self.setLeaveBalance(25)

    # Not necessary if OT_BONUS is added
    def compute_pay(self,hours):    # override by REPLACEMENT(other already have such method)
        """ Override the parent's computePay method, use our own method"""
        return self.getRate() * hours # no OT pay for manager
    
    def __str__(self):              # overriding by REFINEMENT (add-on to the parent's method)
        return super().__str__() + "\t Dept:{}".format(self.__dept)
    
e1 = Employee("111",19.50)
print(e1)
m1 = Manager("111",20.5,"SS")
print(m1)
print(m1.getRate())
# issubclass(m1,e1)
# issubclass(e1,m1)
print(e1.computepay(10))
print(m1.computepay(10))
# using property
m1.rate = 26 # look like assigning 26 to rate (will call the setter)
print(m1.rate,e1.rate) # m1.get_rate()