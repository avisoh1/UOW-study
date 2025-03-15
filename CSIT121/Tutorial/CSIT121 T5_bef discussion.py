# CSIT121 T5 Revision 13/11/2024
# 1a)
import datetime
class Course:
    """Constructor that shows the attributes of Course class"""
    def __init__(self,code,name,cost):
        self.__code = code
        self.__name = name
        self.__cost = cost

    @property
    def code(self):
        return self.__code
    
    @property
    def cost(self):
        return self.__cost
    
    def __str__(self):
        return f"Course: {self.__code} Name: {self.__name}"
    
class TeachingStaff:
    def __init__(self,staff_id,name,rate):
        self.__staff_id = staff_id
        self.__name = name
        self.__rate_per_day = rate

    @property
    def staff_id(self):
        return self.__staff_id
    
    @property
    def rate_per_day(self):
        self.__rate_per_day
    
    @rate_per_day.setter
    def rate_per_day(self,new_rate):
        self.__rate_per_day = new_rate
    
    def __str__(self):
        return f"Staff ID:{self.__staff_id} Name:{self.__name}"

class CourseOffering:
    _sch_id = 1

    def __init__(self,course:Course,instructors = [TeachingStaff],start_date=6/1/2024,days=1):
        self.__schedule_id = course.code + "_" + str(CourseOffering.__sch_id)
        CourseOffering._sch_id += 1
        self.__course = course
        self.__instructors = instructors
        self.__start_date = start_date
        self.__days = days

    @classmethod
    def change_sch_id(cls,new_id):
        return cls.__sch_id == new_id
    
    @property
    def schedule_id(self):
        return self.__schedule_id
    
    @property
    def start_date(self):
        return self.__start_date
    
    @start_date.setter
    def start_date(self,newDate):
        self.__start_date = newDate
    
    def get_course_fee(self):
        # self.course_fee = self.__course.cost + self.__days * self.__instructors.rate_per_day
        #return self.course_fee
        instructors_cost = 0
        for inst in self.__instructors:
            instructors_cost += inst.rate_per_day * self.__days
        return self.__course.cost + instructors_cost
    
    def __str__(self):
        """
        cost = 0
        course_fee = self._get_course_fee()
        course_offered = f"Schedule ID:{self.__schedule_id} \tStart Date: {self.__start_date}\tDuration: {self.__days}"
        course_offered += f"{self.__course}"
        for i in self.__instructors:
            course_offered += i
            cost += course_fee
        course_offered += f"Basic cost: ${cost:.2f}"
        return course_offered
        """
        instructors = " "
        for i in self.__instructors:
            instructors += i.__str__() + "\n"
        return "Schedule Id: {}\tStart Date: {}\tDuration: {} days\n".format(\
            self.__schedule_id,self.__start_date,self.__days)\
            + self.__course.__str__() + "\n" + instructors + \
            "Basic Cost: {:.2f}".format(self.get_course_fee())