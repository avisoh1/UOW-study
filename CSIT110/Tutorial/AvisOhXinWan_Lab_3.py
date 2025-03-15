# Name: Avis Oh Xin Wan
# Tutorial Group: 1 (116)
# Objective: This is lab 3.
# File name: AvisOhXinWan_Lab_3.py
# 
# Declarations: This is my own program. I gave not passed my program to anyone in this class. If I do so, I accept any penalty of mark.

# Set condition to continue or finish loop
repeat = 0

# Create loops 
while repeat == 0:
    
# Prompt the user to enter x-y coordinates
    x,y = map(float, input("Enter x and y: ").split())

# Output the location of the points
    if x > 0 and y > 0:
        print("==> ({0:.2f}, {1:.2f}) is above X-axis".format(x,y))
        print("==> It is at first quadrant")
    elif x < 0 and y > 0:
        print("==> ({0:.2f}, {1:.2f}) is above X-axis".format(x,y))
        print("==> It is at second quadrant")
    elif x < 0 and y < 0:
        print("==> ({0:.2f}, {1:.2f}) is below X-axis".format(x,y))
        print("==> It is at third quadrant")
    elif x > 0 and y < 0:
        print("==> ({0:.2f}, {1:.2f}) is below X-axis".format(x,y))
        print("==> It is at forth quadrant")
    elif x != 0 and y == 0:
        print("==> ({0:.2f}, {1:.2f}) is at X-axis".format(x,y))
    elif x == 0 and y != 0:
        print("==> ({0:.2f}, {1:.2f}) is at Y-axis".format(x,y))
    else:
        print("==> ({0:.2f},{1:.2f}) is at origin".format(x,y))
        repeat = repeat + 1
    
# last statement of program
input("\nPlease enter to terminate")
