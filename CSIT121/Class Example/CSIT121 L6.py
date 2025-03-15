class BMIException(Exception):
    pass

class BMI_Calculator:
    @classmethod
    def compute_BMI(self,weight,height):
        if weight <= 0:
            raise BMIException("{} is a wrong input for your weight....".format(weight))
        if height <= 0:
            raise BMIException("{} is a wrong input for your height....".format(height))
        return weight/(height * height)
    
    @classmethod
    def get_BMI_Rating(self,bmi):
        if bmi < 18.5:
            return "underweight"
        elif bmi > 18.5 and bmi < 25:
            return "normal"
        elif bmi >= 25 and bmi < 30:
            return "overweight"
        else:
            return "obese"

class Person:
    """
    name
    height
    weight
    """

class Student:
    """
    name
    height
    weight
    """

def main():
    height = float(input("Enter your height (meters):"))
    weight = float(input("Enter your weight (kg): "))
    bmi = BMI_Calculator.compute_BMI(weight,height)
main()

def bmi():
    try:
        height = float(input("Enter your height (meters):"))
        weight = float(input("Enter your weight (kg): "))
        bmi = BMI_Calculator.compute_BMI(weight,height)
    except Exception as e:      # safety net for all other type of exceptions
        print(type(e),e)
    except ValueError as v:
        print("Please enter numbers for the height/weight:")
        print(type(v),v)
    except ZeroDivisionError as z:
        print("Height cannot be 0")
        print(type(z),z)
    else:                      # will be executed if nothing wrong with the try:block
        rating = BMI_Calculator.get_BMI_Rating(bmi)
        print("Your BMI is {:.2f} which means you are {}".format(bmi, rating))
    finally:                   # will be executed regardless
        print("Live a healthy lifestyle!")

main()

def sub_function():
    raise Exception("for demo")

def function1():
    try:
        sub_function()
    except Exception as e:
        print(e)

def main():
    function1()
main()