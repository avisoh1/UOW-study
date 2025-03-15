def question_1a():
    total = 0
    while True:
        userInput = input("Enter integer: ")      
        if userInput != "":
            total += int(userInput)
        else:
            break
    return total

def question_1b (start, end, step):  # cleanest way
    qns = str(start)
    ans = start
    counter = start + step
    while (counter < end):
      answer += counter
      qns += " + " + str(counter)
      counter += step
  
    return {"qns": qns, "ans": ans}

def question_1c(x:int,y:int):  # cleanest solution. 
    return x%y == 0

def question_1d(str_list):
    totalLength = 0
    for i in str_list:
        totalLength+=len(i)
    return totalLength

def question_1e(error_message):
    raise NotImplementedError(error_message)


def question_1f(dictionary):
    str_format = "!"
    for key in dictionary.keys():
        str_format += f"{key:^10}!"
    return str_format


# Question 2 
class Book:
  def __init__(self, _title: str, _author: str):
    self.title = _title
    self.author = _author
    
  @classmethod
  def from_dict(cls, _dict):
    title = _dict["title"]
    author = _dict["author"]
    return cls(title, author) # return cls(_dict["title"], _dict["author"])
    
  def __str__ (self):
    return (self.title + " by " + self.author)  # () not necessary
      # or
    # return f"{self.title} by {self.author}"
    
# Question 3
# Do not modify, do not remove
class NoDataError(Exception):
        pass

# Do not modify, do not remove 
class Employee():
    def __init__(self, name= "", sales: List[float] = None):
        self.__name = name
        self.__sales = sales

    def get_name(self) -> str:
        return self.name
    
    def get_sales(self) -> list[float]:
        if self.__sales == None:
            raise NoDataError()
        return self.__sales

def get_team_statistics(Employees: list):
    output = {"target_met_count": 0,
            "target_failed_count": 0,
            "invalid_count": 0}
  
    for employee in Employees:
        try:
            sales = employee.get_sales()    # list of sales for each employee
          
            # initialise the sum of sales for each employee with 0
            sales_sum = 0
            
            # loop through each sale in the list to add the number to sales_sum
            for num in sales:
                sales_sum = sales_sum + num
            
                # if the sum of sales >= 100, add 1 to the "target_met_count" key in the dictionary
                if sales_sum >= 100:
                    output["target_met_count"] = output["target_met_count"] + 1
                    # otherwise, add 1 to the "target_met_count" key in the dictionary
            
                else:
                    output["target_failed_count"] = output["target_failed_count"] + 1
              
        except NoDataError:
            # if the get_sales () raise the NoDataError
            output["invalid_count"] = output["invalid_count"] + 1
      
    return output
