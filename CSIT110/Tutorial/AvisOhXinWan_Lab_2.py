#Name: Avis Oh Xin Wan
#Number:116
#Objective: This is an exercise of Lab 2
#File name: AvisOhXinWan_Lab_2.py
#
#Declarations: This is my own program. I gave not passed my program to anyone in this class. If I do so, I accept any penalty of marks.

#Let the user enter a number
number = int(input("Enter a 4 digits integer for encryption: ").zfill(4))

# Add 7 to each digit and take modulo 10
digit1 = ((number//1000)%10+7)%10
digit2 = ((number//100)%10+7)%10
digit3 = ((number//10)%10+7)%10
digit4 = (number%10+7)%10 

# Swap the 1st and 3rd digits, and the 2nd and 4th digits
digit1, digit3 = digit3, digit1
digit2, digit4 = digit4, digit2

# Convert the list of digits back to an integer
a1 = digit1*1000
b1 = digit2*100
c1 = digit3*10
d1 = digit4
encrypted_integer = a1+b1+c1+d1

# Print the result
print("==> Encrypted integer is {0:04d}".format(encrypted_integer))

#Let the user to enter a number
encrypted_number = int(input("\nEnter a 4 digits integer for encryption: ").zfill(4))

# Add 3 to each digit and take modulo 10
e_digit1 = ((encrypted_number//1000)+3)%10
e_digit2= ((encrypted_number//100)+3)%10
e_digit3= ((encrypted_number//10)+3)%10
e_digit4= (encrypted_number+3)%10 

# Swap the 1st and 3rd digits, and the 2nd and 4th digits back
e_digit1,e_digit3 = e_digit3,e_digit1
e_digit2,e_digit4 = e_digit4,e_digit2

# Convert the list of digits back to an integer
a2 = e_digit1*1000
b2 = e_digit2*100
c2 = e_digit3*10
d2 = e_digit4
decrypted_integer = a2+b2+c2+d2

# Print the result
print("==> Decrypted integer is {0:04d}".format(decrypted_integer))

#Insert the following statement for every submission
input("\nPlease enter to terminate.")
