# 1) product_code + product_name + product_size
# 2) 377B product_name 250mL
# 3) 377B, Beef Liquid Stock, + product_size
# 4) 377B, Beef Liquid Stock, 250mL
# 5) print(f"{product_code}: {product_name}, {product_size}")
# 6) print(f'"{product_name}", {product_size}')
# or q = "\""
# print(f"{q}{product_name}{q}, {product_size}")
# 7) print(f"{product_name}, {product_size}, ${product_price}")

#q2
def question2():
    string_output = "You have selected the following fruits: "
    selection_num = int(input("How many fruits would you like to select? "))
    for i in range(selection_num):
        string_output += input("Enter fruit name: ")
        if(i < selection_num-1):
            string_output += ", "
    print(string_output, end=".")

# or 
subject=int(input("How many fruits would you like to select? "))
fruits_list=[]
for i in range(0, subject):
    fruit_name=input("Enter fruit name: ")
    fruits_list.append(fruit_name)
print(f"You have selected the following fruits: {','.join(fruits_list)}")

#q3
def format_date(date: int, month: int, year: int):
    return f"{date:>02d}-{month:>02d}-{year}"

# or
def format_date(date, month, year):
    # format date
    date_str = ""
    if date < 10:
        date_str = f"0{date}-"
    else:
        date_str = str(date) + "-"
    # format month
    if month < 10:
        date_str += f"0{month}-"
    else:
        date_str += str(month) + "-"
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
        print f"Solution found. duck: {duck}, cow:{headCount-duck}"
        found = True
        break
if not found:
    print "No solution found."     


#q5
numbers = {"one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6",
        "seven":"7", "eight":"8", "nine": "9", "zero":"0"}
while True:
    user_input = str(input("Enter a digit word (zero-nine) or q to quit: "))
    if(user_input.lower() == "q"):
        print("Good bye!")
        break
    else:
        print(f"You have entered: {numbers.get(user_input.lower())}")

# or 
numbers = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
while True:
    user_input = str(input("Enter a digit word (zero-nine) or q to quit: "))
    if(user_input.lower() == "q"):
        print("Good bye!")
        break
    else:
        print(f"You have entered: {numbers.index(user_input)}")

# or
quitprogram = False

while quitprogram == False:
    digit_word = input("Enter a digit word (zero-nine) or q to quit: ")
    if digit_word == "zero":
        print("You have entered: 0")
    elif digit_word == "one":
        print("You have entered: 1")
    elif digit_word == "two":
        print("You have entered: 2")
    elif digit_word == "three":
        print("You have entered: 3")
    elif digit_word == "four":
        print("You have entered: 4")
    elif digit_word == "five":
        print("You have entered: 5")
    elif digit_word == "six":
        print("You have entered: 6")
    elif digit_word == "seven":
        print("You have entered: 7")
    elif digit_word == "eight":
        print("You have entered: 8")
    elif digit_word == "nine":
        print("You have entered: 9")
    elif digit_word == "q":
        print("Good bye!")
        quitprogram = True