class BMI_Calculator:
    @classmethod
    def compute_BMI(self, weight, height):
        return weight / (height * height)

    @classmethod
    def get_BMI_Rating(self, bmi):
        if bmi < 18.5:
            return "underweight"
        elif bmi >= 18.5 and bmi < 25:
            return "normal"
        elif bmi >= 25 and bmi < 30:
            return "overweight"
        else:  
            return "obese"

def main():
    try:
        height = float(input("Enter your height (meters): "))
        weight = float(input("Enter your weight (kg): "))
        bmi = BMI_Calculator.compute_BMI(weight, height)
    except ValueError:
        print("Please enter numbers for height/weight")
    except ZeroDivisionError as z:
        print("Don't be stupid, height cannot be 0")
        print(z)
    except Exception as e:  # safety net for all other type of exceptions
        print(type(e), e)
    else: # will be executed if no exceptions with the try: block
        rating = BMI_Calculator.get_BMI_Rating(bmi)
        print("Your BMI is {:.2f} which means you are {}.".format(bmi, rating))
    finally:  # will be executed regardless (e.g. housekeeping tasks)
        print("Live healthy")
        #oufile.close()

main()




=================


def exceptionDemo():
    x = [6,7,8,9]
    try:
        print('begin try')
        index = int(input('Enter index: '))
        x = x[index] / index
        print('end try')
        return  # still  need to go through finally
    except ZeroDivisionError as z:
        print("ZeroDivisionError block -", z)
        return  # still  need to go through finally only
    except ValueError as v:
        print('ValueError error block -', v)
    except Exception as e:
        print('except block - ', e)
    else:
        print('else block')
    finally:
        print('finally block')

    print('end exception demo')

def main():
    exceptionDemo()
    print("am here")
    
main()
