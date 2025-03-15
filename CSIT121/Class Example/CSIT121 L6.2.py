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
        rating = BMI_Calculator.get_BMI_Rating(bmi)
        print("Your BMI is {:.2f} which means you are {}".format(bmi,rating))
    except Exception as e:
        print("oops something is wrong")
        print(type(e),e)
    print("Live a healthy lifestyle!!")
main()




=================


def exceptionDemo():
    x = [6,7,8,9]
    try:
        print('begin try')
        index = int(input('Enter index: '))
        x = x[index] / index
        print('end try')
        return
    except ZeroDivisionError as z:
        print("ZeroDivisionError block -", z)
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

def getIntegerRange(prompt,min,max):
    while True:
        try:
            value = int(input(prompt))

            if min <= value <= max:
                return value
            else:
                print("Sorry, please re-enter within range ({},{})".\
                      format(min,max))
        
        except:
            print("Sorry, I don't understand that. PLease try again.")

print(getIntegerRange("Enter 1-6: ",1,6))