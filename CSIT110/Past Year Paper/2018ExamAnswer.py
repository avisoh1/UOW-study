# 1) product_code + product_name + product_made
# 2) 247B product_name Made in Australia
# 3) 247B, Real Beef Stock, + product_made
# 4) 247B, Real Beef Stock, Made in Australia
# 5) print(product_code + ": " + product_name + ", " + product_made)
# 6) print('"' + product_name + '", ' + product_made)
# 7) print(product_name + ", $" + str(product_price) + ", " + product_made)

#q2
def question2():
    string_output = "You have selected the following subjects: "
    num_of_subject = int(input("How many subjects would you like to enroll? "))
    for i in range(num_of_subject):
        string_output += input("Enter subject code: ")
        if(i < num_of_subject-1):
            string_output += ", "
    print(string_output, end=".")

# or 
num_of_subject=int(input("How many subject would you like to enroll? "))
subject_list=[]
for i in range(0, num_of_subject):
    subject_code=input("Enter subject code: ")
    subject_list.append(subject_code)
print(f"You have selected the following subjects: {','.join(subject_list)}")

#q3
def format_date(date: int, month: int, year: int):
    return f"{date:>02d}/{month:>02d}/{year}"

# or
def format_date(date, month, year):
    # format date
    date_str = ""
    if date < 10:
        date_str = f"0{date}/"
    else:
        date_str = str(date) + "/"
    # format month
    if month < 10:
        date_str += f"0{month}/"
    else:
        date_str += str(month) + "/"
    # format year
    date_string +=  string(year)

    return date_string

# q3
date = input("Enter date:" )
month = input("Enter month:" )
year = input("Enter year:" )
print(f"You have entered: {format_date(int(date),int(month),int(year))}")

    
# q4
headCount = int(input("Enter head count: "))
legCount = int(input("Enter leg count: "))
found = False
for duck in range(0,headCount + 1):
    if ((duck*2) + (headCount-duck)*4 == legCount):
        print(f"Solution found. duck: {duck}, cow:{headCount-duck}")
        found = True
        break
if not found:
    print("No solution found.")  


#q5
numbers = {"1": "one", "2": "two", "3": "three", "4": "four", "5": "five", "6": "six",
        "7": "seven", "8": "eight", "9": "nine", "0": "zero"}
while True:
    user_input = str(input("Enter a digit (0-9) or q to quit: "))
    if(user_input.lower() == "q"):
        print("Good bye!")
        break
    else:
        print(f"You have entered: {numbers.get(user_input)}")

# or 
numbers = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
while True:
    user_input = str(input("Enter a digit (0-9) or q to quit: "))
    if(user_input.lower() == "q"):
        print("Good bye!")
        break
    else:
        print(f"You have entered: {numbers[int(user_input)]}")

# or
quitprogram = False

while quitprogram == False:
    enter_digit = input("Enter a digit (0-9) or q to quit: ")
    if enter_digit == "0":
        print("You have entered: zero")
    elif enter_digit == "1":
        print("You have entered: one")
    elif enter_digit == "2":
        print("You have entered: two")
    elif enter_digit == "3":
        print("You have entered: three")
    elif enter_digit == "4":
        print("You have entered: four")
    elif enter_digit == "5":
        print("You have entered: five")
    elif enter_digit == "6":
        print("You have entered: six")
    elif enter_digit == "7":
        print("You have entered: seven")
    elif enter_digit == "8":
        print("You have entered: eight")
    elif enter_digit == "9":
        print("You have entered: nine")
    elif enter_digit == "q":
        print("Good bye!")
        quitprogram = True