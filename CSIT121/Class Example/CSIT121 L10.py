class Sample:
    def __init__(self,aaa,bbb):
        self.__aaa = aaa
        self.__bbb = bbb
    
    @property
    def aaa(self):
        return self.__aaa
    
    @property
    def bbb(self):
        return self.__bbb
    
    @bbb.setter
    def bbb(self,newValue):            # property come first
        self.__bbb == newValue
    
    def otherMethod(self,param=2):     # overloading : put a default parameter
        return self.__aaa * param
    
    def __str__(self):
        return "aaa: {} bbb:{}".format(self.__aaa,self.__bbb)

s = Sample()
s.otherMethod()
s.otherMethod(3)

from abc import ABC,abstractmethod
class Sample(ABC):
    _NEXT_ID = 1    # Other than ID no. that is runnning, use type(self)
    _BONUS = 2      # _ means protected, so that the child classes can use

    def __init__(self,aaa,bbb):
        self.__id = Sample._NEXT_ID
        Sample._NEXT_ID += 1    # increment by creating an object
        self.__aaa = aaa
        self.__bbb = bbb
    
    @classmethod
    def bonus(cls):
        return cls._BONUS
    
    def otherMethod(self,param1=2):
        return type(self)._BONUS * self.__bbb * 2
    # don't hardcord otherwise your subclasses cannot have its own bonus rate
    # Other than ID no. that is runnning, use type(self)
    
    @property
    def aaa(self):
        return self.__aaa
    
    @property
    def bbb(self):
        return self.__bbb
    
    @bbb.setter
    def bbb(self,newValue):            # property come first
        self.__bbb == newValue
    
    def otherMethod(self,param=2):     # overloading : put a default parameter
        return self.__aaa * param
    
    def __str__(self):
        return "aaa: {} bbb:{}".format(self.__aaa,self.__bbb)