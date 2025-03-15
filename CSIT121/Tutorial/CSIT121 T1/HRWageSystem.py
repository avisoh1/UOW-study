class Staff:
    
    # constructors
    def __init__(self,name,department,position,grade,monthly_salary,performance_score):
        # instant variable - belongs to object
        self.name = name
        self.department = department
        self.position = position
        self.grade = grade
        self.monthly_salary = monthly_salary
        self.performance_score = performance_score
        
    # instant method - need to include "self"
    # if no self - class or static method
    # rule of thumb
    # if a method need to use the instant variable
    # it must be an instant method
    def display(self):
        print(f"Name:{self.name}")
        print(f"Department:{self.department}")
        print(f"Position:{self.position}")
        print(f"Grade:{self.grade}")
    
    def calculateMonthlySalary(self,overtime=0):
        if(self.grade<=3):
            return self.monthly_salary
        elif(self.grade==4):
            overtime_pay = min([overtime*10,200])
            return self.monthly_salary + overtime_pay
        elif(self.grade==5):
            overtime_pay = min([overtime*5,300])
            return self.monthly_salary + overtime_pay
    
    def calculateYearEndBonus(self):
        bonus = self.monthly_salary*2/self.grade * self.performance_score
        return round(bonus,2)
        
if __name__ == "__main__":
    staff1 = Staff("John","IT","Engineer",4,5000,7.5) # call constructor
    staff2 = Staff("Bob","Sales","Manager",3,4000,8) # call constructor
   
    staff1.display() # display(staff1)
    s1 = staff1.calculateMonthlySalary(30)
    b1 = staff1.calculateYearEndBonus()
    print(s1,b1)
    print()
    staff2.display()
    s2 = staff2.calculateMonthlySalary()
    b2 = staff2.calculateYearEndBonus()
    print(s2,b2)
        