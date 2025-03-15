""" ASSIGNMENT 1"""
name = 'John Snow'
student_num = '1234567'  # UOW Student number 
subject_code = 'CSIT110'

def question_1():
    text1 = input("Enter a text: ")
    text2 = input("Enter another text:")
    text3 = input("Last text:")
    num1 = input("Enter number:")
    num2 = input("Enter another number:")
    print(f"A new virus, {text1+text2+text3}, has been detected! {int(num1)+int(num2)} cases have been confirmed.")
    #### UNCOMMENT THE LINE ABOVE AND INSERT YOUR SOLUTION HERE ####


def question_2():
    travel_overseas = input("Enter Y if you have travelled overseas within the past two weeks: ")
    if travel_overseas.lower() == "y":
        print("You are not allowed to enter the mall.")
    else:
        serving_shn = input("Enter Y if anyone in your household is currently serving stay home notice: ")
        if serving_shn.lower() == "y":
            print("You are not allowed to enter the mall.")
        else:
            temp = float(input("Enter your temperature in degrees Celcius: "))
            if temp>= 37.5:
                print("You are not allowed to enter the mall.")
            else:
                print("Welcome to Lion City Mall")

    #### UNCOMMENT THE LINE ABOVE AND INSERT YOUR SOLUTION HERE ####

def question_3():
    X = int(input("Please enter the value for X: "))
    N = int(input("Please enter the value for N: "))
    print(f"The {X} multiplication table")
    for i in range(0,N+1):
        print(f"{X} x {i} = {X*i}")
    #### UNCOMMENT THE LINE ABOVE AND INSERT YOUR SOLUTION HERE ####

def question_4():
    num_single_rm = int(input("Number of Single room: "))
    num_twin_rm = int(input("Number of Twin room: "))
    num_deluxe_rm = int(input("Number of Deluxe room: "))
    num_nights = int(input("Length of stay(number of nights): "))
    print()
    print(f"Summary of your booking for {num_nights}night(s)")
    def format_money(num):
        return f"${num:.2f}"
    print(f"{'Single room':<12}{num_single_rm:^3}{format_money(num_single_rm*90*num_nights):>9}")
    print(f"{'Twin room':<12}{num_twin_rm:^3}{format_money(num_twin_rm*160*num_nights):>9}")
    print(f"{'Deluxe room':<12}{num_deluxe_rm:^3}{format_money(num_deluxe_rm*250*num_nights):>9}")
    subtotal = num_nights*(num_single_rm*90
            + num_twin_rm*160
            + num_deluxe_rm*250)
    print(f"{'Subtotal':<12}"
        + f"{num_single_rm+num_twin_rm+num_deluxe_rm:^3}"
        + f"{format_money(subtotal):>9}")
    print(f"{'Total(7% g.s.t)':<15}{format_money(subtotal*1.07):>9}")
    #### UNCOMMENT THE LINE ABOVE AND INSERT YOUR SOLUTION HERE ####

def question_5():   
    cleaned = ""
    while True:
        filename = input()
        if filename == "":
            break
        while filename.find("[") != -1:
            start = filename.rfind("[")
            end = filename[start:].find("]") + start
            filename = filename[:start] + filename[end+1:]
        if len(cleaned) > 1:
            cleaned += "," + filename
        else:
            cleaned = filename
    print(cleaned)
    #### UNCOMMENT THE LINE ABOVE AND INSERT YOUR SOLUTION HERE ####


def main():  # DO NOT MODIFY THIS LINE
    print("Assignment 1")  # DO NOT MODIFY THIS LINE
    # UNCOMMENT THE FOLLOWING TO TEST YOUR SOLUTION
    # question_1()
    #question_2()
    # question_3()
    # question_4()
    question_5()

if __name__ == '__main__':  # DO NOT MODIFY THIS LINE
    main()  # DO NOT MODIFY THIS LINE