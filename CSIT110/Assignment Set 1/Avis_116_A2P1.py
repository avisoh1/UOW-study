# Full Name: Avis Oh Xin Wan
# Tutorial Group: 1 (116)
# Objective: This is assignment 2.
# File name: Avis_116_A2P1.py
#
# Declarations: This is my own program. I gave not passed my program to anyone in this class. If I do so, I accept any penalty of mark.

# This function gets the credit card number from user, and checks if a credit card is valid.
# It will display response when the number is not valid. 
# For the valid number, it will return value to be used in the next function.
def get_CreditCard_No():

    # Let the user to enter a credit card number to validate
    card_number = input("Enter a credit card: ")
    parts = card_number.split('-')
        
    # Display info when the credit card number is invalid.
    if len(parts) < 4:
        print("==>  Too few tokens")
        return None
    elif len(parts) > 4:
        print("==>  Too many tokens")
        return None
    elif not all(part.isdigit() for part in parts):
        print("==>  Non digits in card")
        return None
    elif not all(len(part) == 4 for part in parts):
        print("==>  In valid length")
        return None
    # Check and return variables for those valid credit card number
    else:
        n1, n2, n3, n4 = card_number.split('-')
        if len(n1) == 4 and len(n2) == 4 and len(n3) == 4 and len(n4) == 4:
            c1 = int(n1)
            c2 = int(n2)
            c3 = int(n3)
            c4 = int(n4)
        return c1, c2, c3, c4

# This function helps to get reverse of a positive integer
def getReverse(n):

    rev = int(str(n)[::-1] )
    if n < 10:
        reverse = str(rev * 1000)
    elif n < 100:
        reverse = str(rev * 100)
    elif n < 1000:
        reverse = str(rev * 10)
    else:
        reverse = str(rev).zfill(4)
    
    return reverse

# The function to form a new integer so that the 2nd the 4th digits are doubles.
def double_Even(reverse):

    digits = list(reverse)
    if len(digits) >= 2:
        digits[1] = str(int(digits[1]) * 2)
    if len(digits) >= 4:
        digits[3] = str(int(digits[3]) * 2)
    double_digit = ''.join(digits)
    return double_digit

# This function finds the sum of digits of a given positive integer.
def get_Digit_Sum(double_digit):

    sum = 0
    double_digit = int(double_digit)
    while double_digit > 0:
        lastDigit = double_digit % 10
        sum = sum + lastDigit
        double_digit = double_digit // 10
    
    return sum

# This function checks if a credit card number is valid.
def validate_Card(c1,c2,c3,c4,total_sum):
    
    # Valid for those total that has the remainder 0 when divide by 10
    operator = total_sum % 10
    if operator == 0:
        print("\t{0:04d}-{1:04d}-{2:04d}-{3:04d} is a valid credit card because {4} % 10 = 0"\
              .format(c1,c2,c3,c4,total_sum))
    else:
        print("\t{0:04d}-{1:04d}-{2:04d}-{3:04d} is an invalid credit card because {4} % 10 != 0"\
              .format(c1,c2,c3,c4,total_sum))

def main():
    print("Welcome to ABC credit card company\n")
    # Create while loop
    i = 0
    while i == 0:

        # Start display details
        card_details = get_CreditCard_No()
        if card_details is not None:
            c1,c2,c3,c4 = card_details
            
            # Display the information
            for n in [c1, c2, c3, c4]:
                reverse = getReverse(n)
                double_digit = double_Even(reverse)
                sum = get_Digit_Sum(double_digit)            
                total_sum = get_Digit_Sum(double_Even(getReverse(c1))) + get_Digit_Sum(double_Even(getReverse(c2))) + \
                            get_Digit_Sum(double_Even(getReverse(c3))) + get_Digit_Sum(double_Even(getReverse(c4)))
            
            # Invoke the function
            print("\nAnalysis:")
            print("\t(a) To get the reverse of each 4 digits \n\t\t {0}\t\t{1}\t\t{2}\t\t{3}  "\
                .format(getReverse(c1),getReverse(c2),getReverse(c3),getReverse(c4)))
            print("\t(b) To multiply by 2 of each even digit position \n\t\t {0}\t\t{1}\t\t{2}\t\t{3}"\
                .format(double_Even(getReverse(c1)),double_Even(getReverse(c2)),double_Even(getReverse(c3)),double_Even(getReverse(c4))))
            print("\t(c) To get the sum of all digits in card elements \n\t\t {0}\t\t{1}\t\t{2}\t\t{3}"\
                .format(get_Digit_Sum(double_Even(getReverse(c1))),get_Digit_Sum(double_Even(getReverse(c2))),\
                        get_Digit_Sum(double_Even(getReverse(c3))),get_Digit_Sum(double_Even(getReverse(c4)))))
            print("\t(d) To find the sum of all elements in card ")
            print("\t\tThe special sum is {0}".format(total_sum))
            print()
            print("Conclusion:")
            validate_Card(c1,c2,c3,c4,total_sum)

        # Let the user choose need to continue or not
        another_card = input("\nAnother card (y/Y/n/N): ")
        if another_card == 'Y' or another_card == 'y':
            print("-" * 90)
        
        # Out of loop
        else:
            i = i + 1
            # last statement of program
            input("Please enter to terminate")
        
if __name__ == "__main__":
    main()