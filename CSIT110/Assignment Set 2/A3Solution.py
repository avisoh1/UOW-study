""" Template for Assignment 3
    Use this template for submission.
    - This template includes an example function.
    - Note that the template uses 4 space for indenation
      which you may choose to replace as tabs

    student_name = ''
    student_uow_id = ''
    course_code = 'SCIT110'

"""
import random

name = "John Snow"
student_num = "1234567"  # uow student number
course_code = "SCIT110"


def myClass_demo_unit_test(class_ref):
    """ 1. This example takes in a class definition as input,
        2. it instantiates a class object and
        3. call the instance method, .demo() in a try-except block.
    """
    try:
        obj = class_ref()
        obj.demo()
    except ValueError as e:
        print('A ValueError was raised because ' + str(e))


def example():
    # A class with one method
    class MyClass():
        def __init__(self):
            pass

        def demo(self):
            raise ValueError('Wrong input given!')
    # test the demo method
    myClass_demo_unit_test(MyClass)


class Student():
    def __init__(self, dict):
        self.name = dict["name"]
        self.results = dict["results"]

    def get_weighted_result(self, weights: dict):
        """ weights - this parameter is a dictionary
                its keys are assessment names
                its values are the weightage of each assessment
            e.g. If
                weights is  {"English": 1, "Math": 2, "Science": 0.5}
                Student.results is {"English": 75, "Math": 81, "Science": 60,
                 "Humanities": 80}
                the return value is 267. Because 1*75 + 2*81 + 0.5*60 = 267
        """
        results = 0
        for each_assessment in weights.keys():
            if each_assessment not in self.results:
                raise AssessmentNotFoundError(each_assessment, self.name)
            results += self.results[each_assessment]*weights[each_assessment]
        return results

# ==================== Insert your solution after this line =================#


def myClass_get_int_unit_test(class_ref):
    try:
        obj = class_ref()
        number = obj.get_integer()
    except AttributeError:
        return "A"
    except ValueError:
        return "V"
    except Exception:
        return "O"
    else:
        return number


def compute_unit_prices(catalogue: dict, items: list):
    return_dict = {}
    for each_item in items:
        try:
            price_info = catalogue[each_item]
            unit_price = price_info[0]/price_info[1]
        except KeyError:
            return_dict[each_item] = None
        except ZeroDivisionError:
            return_dict[each_item] = -1
        except Exception:  # except:
            return {}
        else:
            return_dict[each_item] = unit_price
    return return_dict


class AssessmentNotFoundError(Exception):
    def __init__(self, name_assessment: str, name_student: str):
        self.name_assessement = name_assessment
        self.name_student = name_student

    def __str__(self):
        return f"{self.name_assessement} cannot be found" + \
         f" in {self.name_student}'s results"


class InvalidDepthError(Exception):
    def __str__(self):
        return "Invalid Depth"


class WaterBody:
    RHO = 997
    G = 9.81

    def __init__(self, vol):
        self.volume = vol

    @classmethod
    def get_hydrostatic_pressure(cls, depth: float):
        if depth < 0:
            raise InvalidDepthError()
        return cls.RHO*cls.G*depth

    def get_water_mass(self):
        return WaterBody.RHO*self.volume

    @staticmethod
    def is_large(volume: float):
        return volume > 100

    @staticmethod
    def is_medium(volume: float):
        return 50 <= volume <= 100

    @staticmethod
    def is_small(volume: float):
        return volume < 50

    @classmethod
    def spawn(cls):
        return cls(random.randint(1, 999))


class SingaporeNumbers:
    @staticmethod
    def car_plate_checksum(carplate: str):
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        six_numbers = [0, 0]
        prefix = ""
        number_list = []
        weights = [9, 4, 5, 4, 3, 2]
        checksum = "AZYXUTSRPMLKJHGEDCB"
        for each_char in carplate:
            try:
                number = int(each_char)
            except ValueError:
                prefix += each_char
            else:
                number_list.append(number)

        # sort prefixes out first
        if len(prefix) == 3:
            six_numbers[0] = alphabet.find(prefix[1].lower()) + 1
            six_numbers[1] = alphabet.find(prefix[2].lower()) + 1
        elif len(prefix) == 2:
            six_numbers[0] = alphabet.find(prefix[0].lower()) + 1
            six_numbers[1] = alphabet.find(prefix[1].lower()) + 1
        else:
            six_numbers[1] = alphabet.find(prefix[0].lower()) + 1

        # sort numbers out next
        if len(number_list) == 4:
            six_numbers.extend(number_list)
        else:
            six_numbers.extend(
                [0]*(4 - len(number_list))
                + number_list
            )

        # multiply six numbers by weights
        total = 0
        for i in range(0, 6):
            total += weights[i]*six_numbers[i]

        # get remainder
        remainder = total % 19
        return checksum[remainder]

    @staticmethod
    def magic_num_checksum(data: str):
        weights = [2, 7, 6, 5, 4, 3, 2]
        total_sum = 0
        checksum = "JZIHGFEDCBA"
        # get weighted sum
        for idx in range(0, len(data)):
            total_sum += int(data[idx])*weights[idx]
        # get remainder
        remainder = total_sum % 11
        return checksum[remainder]


# ==================== Insert your solution before this line =================#


def main():
    print("Assignment3")
    """
    To test your code, create your own test classes
    similaar to MyClass that raise different errors."""
    example()

    class TestValueError():
        def __init__(self):
            pass

        def get_integer(self):
            raise ValueError('Wrong input given!')

    class TestAttributeError():
        def __init__(self):
            pass

        def get_integer(self):
            raise AttributeError('Wrong input given!')

    class TestOtherError():
        def __init__(self):
            pass

        def get_integer(self):
            raise KeyError('Wrong input given!')

    class TestNoError():
        def __init__(self):
            pass

        def get_integer(self):
            return 6
    # test the demo method
    print("V" == myClass_get_int_unit_test(TestValueError))
    print("A" == myClass_get_int_unit_test(TestAttributeError))
    print("O" == myClass_get_int_unit_test(TestOtherError))
    print(6 == myClass_get_int_unit_test(TestNoError))

    # q2_arg1 = {
    #     "Popsicle": [120.0, 100],
    #     "Lollipop": [950, 1000],
    #     "Chips": [850,1100],
    #     "TIME Magazine": [1050, 0]
    # }
    # q2_arg2 = ["Popsicle", "TIME Magazine", "Newspaper"]
    # q2_sol = {
    #     "Popsicle": 1.2,
    #     "TIME Magazine": -1,
    #     "Newspaper": None }
    # print(compute_unit_prices(q2_arg1, q2_arg2) == q2_sol)
    # pool = WaterBody(10)

    # print(pool.get_hydrostatic_pressure(1)) # prints 9780.57

    # print(pool.get_water_mass())  # prints 9970

    # water_body = WaterBody.spawn()

    # print(f"water_body is a WaterBody object:{
    # isinstance(water_body, WaterBody)}")

    # try:
    #     pool.get_hydrostatic_pressure(-1)
    # except Exception as e:
    #     print(e)  # prints Invalid Depth
    backie_yellow = Student(
        {"name": "Backie Yellow",
            "results": {
                "assignment_1": 9,
                "assignment_2": 12,
                "test_1": 10,
                "project": 32,
                "examination_1": 20,
            }})
    try:
        backie_yellow.get_weighted_result({
            "assignment_1": 1,
            "assignment_2": 1,
            "test_1": 1,
            "project": 1,
            "examination_1": 1})
    except Exception as e:
        print(e)


if __name__ == '__main__':  # DO NOT EDIT THESE TWO LINES.
    main()