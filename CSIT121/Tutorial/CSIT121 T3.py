from abc import ABC, abstractmethod
from datetime import datetime

class Employee(ABC):
    _NEXT_ID = 1

    def __init__(self,name,dob,date_hired):
        self.__emp_id = "EMP{:03d}".format(Employee._NEXT_ID)
        Employee._NEXT_ID += 1
        self.__name = name
        self.__dob = dob
        self.__date_hired = date_hired

    @property
    def empId(self):
        return self.__emp_id
    
    @property
    def age(self):
        return datetime.now().year - self.__dob.year
    
    @property
    def dateHired(self):
        return self.__date_hired
    
    @abstractmethod
    def get_annual_leave(self):
        pass
    
    def get_cpf_contribution(self):
        if self.age <= 50:
            return 0.2
        elif self.age <= 60:
            return 0.12
        else:
            return 0.05
        
    def __str__(self):
        """string representation of the object"""
        return "ID: {}\tName: {}\tAge:{}\tHired:{:%Y-%m-%d}\n CPF%: {}\tAnnual leave: {} days".\
        format(self.__emp_id,self.__name,self.age,self.__date_hired,
               self.get_cpf_contribution(),self.get_annual_leave())
    
class ProfessionalEmp(Employee):
    def __init__(self, name, dob, date_hired,position):
        super().__init__(name, dob, date_hired)
        self.__position = position
    
    @property
    def position(self):
        return self.__position
    
    def get_annual_leave(self):
       yearsOfEmployment = datetime.now().year - self.dateHired.year
       if yearsOfEmployment < 2:
           return 15
       elif yearsOfEmployment < 4:
           return 18
       else:
           return 21
    
    def __str__(self):
        """  string representation of the object"""
        return super().__str__() + "\tPosition: {}".format(self.__position)

class AcademicEmp(Employee):
    def __init__(self, name, dob, date_hired):
        super().__init__(name, dob, date_hired)
        self.__teaching_subjects = [ ]
    
    def has_subject(self,search_key:str):
        for s in self.__teaching_subjects:
            if s.lower() == search_key.lower():
                return True
        return False
    
    def add_subject(self,subject:str):
        if not self.has_subject(subject):
            self.__teaching_subjects.append(subject)

    def get_annual_leave(self):
        return 14
    
    def __str__(self):
        return super().__str__() + "\n\tTeaching Subjects: {}".format(self.__teaching_subjects)
 
class School:
    def __init__(self,name,first_emp):
        self.__name = name
        self.__employees = [first_emp]

    def find_emp(self,id):
        for e in self.__employees:
            if e.empId == id:
                return e
        return None
    
    def add_emp(self,emp:Employee):
        if self.find_emp(emp.empId):
            return False
        
        self.__employees.append(emp)
        return True
    
    def delete_emp(self,id:int):
        e = self.find_emp(id)
        if e is None:
            return False
        self.__employees.remove(e)
        return True

    def search_acad_emp(self,subject:str):
        match_list = []
        for e in self.__employees:
            if isinstance(e,AcademicEmp) and e.has_subject(subject):
                match_list.append(e)
        return match_list
    
class AnotherSchool:
    def __init__(self,name,first_emp):
        self.__name = name
        self.__employees = { }
        self.__employees[first_emp.empId] = first_emp

    def find_emp(self,id):
        return self.__employees.get(id,None)
    
    def add_emp(self,emp:Employee):
        if self.find_emp(emp.empId):
            return False
        
        self.__employees.append(emp)
        return True
    
    def delete_emp(self,id:int):
        e = self.find_emp(id)
        if e is None:
            return False
        del self.__employees[id]
        return True
    
    def search_acad_emp(self,subject:str):
        match_list = []
        for e in self.__employees.values():
            if isinstance(e,AcademicEmp) and e.has_subject(subject):
                match_list.append(e)
        return match_list

def main():
    p1 = ProfessionalEmp("John",datetime(1980,1,1),datetime(2021,1,1),"Manager")
    a1 = AcademicEmp("Jane",datetime(1980,1,1),datetime(2021,1,1))
    a2 = AcademicEmp("Jill",datetime(1970,1,1),datetime(2023,1,1))
    p2 = ProfessionalEmp("Jim",datetime(1960,1,1),datetime(2015,1,1),"Admin")
    p3 = ProfessionalEmp("Jack",datetime(1960,1,1),datetime(2015,1,1),"Security")
    a3 = AcademicEmp("Jenny",datetime(1960,1,1),datetime(2015,1,1))
    a1.add_subject("OOP")
    a1.add_subject("WebTech")
    a2.add_subject("OOP")
    a2.add_subject("OOAD")
    a2.add_subject("WebTech")
    a3.add_subject("OOP")
    a3.add_subject("OOAD")

    uow = School("UOW",p1)
    uow.add_emp(a1)
    uow.add_emp(p2)
    uow.add_emp(a2)
    uow.add_emp(a3)
    uow.add_emp(p3)

    while True:
        id = input("Enter id to search: ")
        if id == "":
            break

        result = uow.find_emp(id)
        if result is None:
            print("No such employee")
        else:
            print(result)
    
    while True:
        subject = input("Enter subject to search: ")
        if subject == "":
            break
        result = uow.search_acad_emp(subject)
        for e in result:
            print(e)

main()