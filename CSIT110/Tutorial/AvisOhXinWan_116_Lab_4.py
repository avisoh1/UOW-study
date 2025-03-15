# Full Name: Avis Oh Xin Wan
# Tutorial Group: 1 (116)
# Objective: This is lab 4.
# File name: AvisOhXinWan_116_lab_4.py
#
# Declarations: This is my own program. I gave not passed my program to anyone in this class. If I do so, I accept any penalty of mark.

# Create random
import random

# This function generates and returns single digit within range a and b.
def getSingleDigit(a,b):
    integer = random.randint(a,b)

    return integer

# This function generates and returns an operators (+ , - , *)
def getOperator():

    return random.choice(['+', '-', '*'])

# This function prints an arithmetic expression function
def printExpression(a, b, operator):

    return("{0} {1} {2} = ?".format(a,operator,b))

# This function generates an arithmetic expression result
def calculateResult(a, b, operator):
    if operator == '+':
        return a + b
    elif operator == '-':
        return a - b 
    else:
        return a * b  

# This function display the message after marking
def print_message(score, total_questions):
    percentage = (score / total_questions) * 100
    if percentage < 50:
        print("Marks = {0:.1f}%".format(percentage))
        print("You failed the test.\nWork harder!")
    elif percentage < 80:
        print("Marks = {0:.1f}%".format(percentage))
        print("You passed the test.\nPlease improve it.")
    elif percentage < 100:
        print("Marks = {0:.1f}%".format(percentage))
        print("Well done, keep it up.")
    else:
        print("Marks = {0:.1f}%".format(percentage))
        print("Excellent.")

# This function generates the number of questions and returns a number between c and d
def getQuestionNo(c,d):
    questionNo = random.randint(c,d)

    return questionNo

# Main function to run the arithmetic test
def main():

    # Generate information for welcome page
    total_questions = getQuestionNo(5,10)
    score = 0

    # Display welcome page
    print("Welcome to arithmetic test")
    print("\nYou have to do {0} questions".format(total_questions))
    print("Good Luck")

    # Create for loops to repeat the arithmetic questions
    for i in range(1,total_questions + 1):

        # Generate the information
        a = getSingleDigit(1,10)
        b = getSingleDigit(1,10)
        operator = getOperator()
        questions = printExpression(a, b, operator)

        # Display the questions and compare the answers
        print("\nQuestion {0}: {1}".format(i,questions))
        user_answer = int(input("Your answer: "))
        correct_answer = calculateResult(a, b, operator)
        if user_answer == correct_answer:
            print("ok")
            score += 1
        else:
            print("wrong")
        
    # Display the final results
    print("\nYour score: {0}/ {1}".format(score,total_questions))
    print_message(score,total_questions)
    # last statement of program
    input("\nPlease enter to terminate")

if __name__ == "__main__":
    main()
