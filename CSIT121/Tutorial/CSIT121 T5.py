# Lab 5
import datetime

class CourseOffering:
    _sch_id = 1

    def __init__(self,start_date,days,course:Course,instructors=[]):
        self.__start_date = datetime 
        self.__days = days
        self.__course = Course
        self.__instructors = []

    @classmethod
    def change_sch_id(cls,new_id):
        return cls._sch_id == new_id
    
    def schedule_id(self):
        pass
    
    @property
    def start_date(self):               # property method
        return self.__start_date
    
    @start_date.setter
    def start_date(self,newDate):       # property setter method
        self.__start_date = newDate

    def get_course_fee(self):    # method signature
        self.__course.cost
        total_inst_fee = 0
        for inst in self.__instructors:   # a list
            total_inst_fee += inst._rate_per_day * self.__days
        return self.__course_cost + total_inst_fee
    
    def __str__(self):
        pass

