name = "John Snow"
student_uow_id = "1234567" # UOW student number
course_code = "CSIT110" # CSIT110 or SP420

def question_1a(list_1, list_2):
    return list_1 + list_2 # or list_1.extend(list_2)

def question_1b(a_list, item):
    return a_list.index(item)
print(question_1b([1,4,"abc",3,2,9,-1,4],4))

def question_1c(x, N):
    return [x]*N

def question_1d(a_list, X_int):
    return a_list.count(X_int)

def dot_product(list1, list2):
    answer = 0
    for index in range(len(list1)):
        answer += list1[index]*list2[index]
    return answer


def root_mean_square(a_list):
    answer = 0
    for num in a_list:
        answer += num**2
    answer /= len(a_list)
    answer = answer**0.5
    return answer

def list_to_dict(a_list):
    data = {}
    for item in a_list:
        data[item[0]] = item[1]

    return data

def question_1h(message):
    raise ValueError(message)

def question_1i():
    size = input("Enter size: ")
    size = float(size)
    if size < 8:
        return "XS"
    elif 8 <= size <=10:
        return "S"
    elif 10 <= size <=14:
        return "M"
    else:
        return "L"

import random
def question_1j(N):
    sol = {"qns": "", "ans": 1}
    for i in range(N):
        num = random.randint(2,99)
        sol["qns"] += str(num)
        if i < N-1:
            sol["qns"] += " + "
        sol["ans"] *= num
    return sol


class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    @classmethod
    def from_dict(cls, arg):
        return cls(arg["name"], arg["price"])
    

# Do not modify, do not remove
class Student():
    def __init__(self, name = "", grades=None):
        self.name: str = name  # name is of str type. 
        self.__grades = grades  # grades will be a list of floats

    class NoGradesError(Exception):
        pass

    def get_grades(self):  #This function will return a list of floats
        if self.__grades == None:
            raise Student.NoGradesError()
        return self.__grades

def get_class_statistics(std_list):
	class_stats = {
		"pass_count" :0,
		"fail_count" :0,
		"invalid_count" :0
	}
	for each_std in std_list:
		try:
			grade = each_std.get_grades()
		except:
			class_stats["invalid_count"] += 1
		else:
			if sum(grade)>=50:
				class_stats["pass_count"] += 1
			else:
				class_stats["fail_count"] += 1

	return class_stats

class Staff:
    def __init__(self, name, staff_num, salary, staff_benefits=True):
        self.name = name
        self.staff_num = staff_num
        self.salary = salary
        self.staff_benefits = staff_benefits
    
    def get_paycheck(self):
        return self.salary


class ContractStaff(Staff):
    def __init__(self, name, staff_num, hourly_rate):
        super().__init__(name, staff_num, None, False)
        self.hours_worked = 0
        self.hourly_rate = hourly_rate
    
    def add_hours_worked(self, hours):
        self.hours_worked += hours
    
    def get_paycheck(self):
        return self.hourly_rate*self.hours_worked


class HighSchoolStudent():
    def __init__(self, name, grades):
        # READ ME!
        # the parameter, name, will be of str type. 
        # the parameter, grades, will be a dictionary with string as keys and float as values.
        #         e.g. {"qwe": 1.1, "asd":5.9}
        self.__name = name
        self.__grades = grades

    def get_name(self):  # The function will return a string
        return self.__name

    def get_grades(self):  #The function returns a dictionary with string as keys and float as values.
        return self.__grades

def get_student_report(student: HighSchoolStudent):
    report = student.get_name() + "\n"
    grades = student.get_grades()
    
    # get each column's width
    width_column1 = len("Total Grade")
    total_grade = 0
    for subject in grades:
        if len(subject)> width_column1:
            width_column1 = len(subject)
        total_grade += grades[subject]
    width_column2 = len(f"{total_grade:>.1f}")

    # format grade content
    for subject in grades:
        report += f"{subject:>{width_column1}}: {grades[subject]:>{width_column2}.1f}\n"
    
    # add dashes
    # +2 for : and the space following it.
    report += '-'*(width_column1 +width_column2 + 2) +"\n"
    
    # add last line
    report += f"{'Total Grade':>{width_column1}}: {total_grade:>{width_column2}.1f}\n"

    return report

student = HighSchoolStudent(
"StudentA",
{
 "Art History": 1.2,
 "Spanish": 23.4,
 "Computer Science": 45,
}
)
print(get_student_report(student))
