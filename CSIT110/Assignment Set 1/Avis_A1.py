# Full Name: Avis Oh Xin Wan
# Tutorial Group: 1 (116)
# Objective: This is assignment 1
# File name: Avis_A1.py
#
# Declarations: This is my own program. I gave not passed my program to anyone in this class. If I do so, I accept any penalty of mark.

# Task 1: Enter the email
# Display Welcome Page 
print("Welcome to our online services\n")
print("*" * 9)
print("* Task 1 *")
print("*" * 9)

# Prompt the user to enter an email address
email = input("\n\nEnter an email address for validation: ")

# Output after user enter email address
print("==> Please validate a link sent to your email to continue :)")

# Let the user enter to continue
input("Press any key or enter to continue\n\n")


# Task 2: Prompt "user" to enter the services and also the costs for each service
# Display it is Task 2
print("*" * 9)
print("* Task 2 *")
print("*" * 9)

# List down services provided
# S = Service
print("\n\nWe provide the following three services")
print("=" * 40)
S1 = input("\tBooking of Service 1:\t")
S2 = input("\tBooking of Service 2:\t")
S3 = input("\tBooking of Service 3:\t")

# List the charges of each service
# UC = Unit Charged
print("\nCost of various services (cents per second)")
print("=" * 42)
UC_S1 = int(input("\tCost of service {0}:\t".format(S1)))
UC_S2 = int(input("\tCost of service {0}:\t".format(S2)))
UC_S3 = int(input("\tCost of service {0}:\t".format(S3)))

# Display summary of various costs
print("\nSummary of various costs")
print("=" * 25)
print()
print("{0:28} {1:<12}".format("Service","Cost per sec"))
print("-" * 41)
print("{0:30} {1:<2} cent(s)".format(S1,UC_S1))
print("{0:30} {1:<2} cent(s)".format(S2,UC_S2))
print("{0:30} {1:<2} cent(s)".format(S3,UC_S3))
print("\n\n")


# Task 3: Prompt the users to enter timing for each service
# Display it is Task 3
print("*" * 9)
print("* Task 3 *")
print("*" * 9)
print()

# Request the user to enter the number of hours/ minutes/ seconds
print("Booking of various services (hours minutes seconds)")
print("=" * 52)
print()

Hours_S1,Minutes_S1,Seconds_S1 = map(int, input("Enter hours minutes seconds for {0}:\t ".format(S1)).split())
Hours_S2,Minutes_S2,Seconds_S2 = map(int, input("Enter hours minutes seconds for {0}:\t ".format(S2)).split())
Hours_S3,Minutes_S3,Seconds_S3 = map(int, input("Enter hours minutes seconds for {0}:\t ".format(S3)).split())

# Display the summary booking
print("\nYou have booked the following services")
print("=" * 40)
print()
print("{0:<19} {1:<9} {2:<9} {3:<10}".format("Service","Hours","Minutes","Seconds"))
print("-" * 50)
print("{0:<19} {1:<9} {2:<9} {3:<10}".format(S1,Hours_S1,Minutes_S1,Seconds_S1))
print("{0:<19} {1:<9} {2:<9} {3:<10}".format(S2,Hours_S2,Minutes_S2,Seconds_S2))
print("{0:<19} {1:<9} {2:<9} {3:<10}".format(S3,Hours_S3,Minutes_S3,Seconds_S3))
print("\n\n")


# Task 4: Perform some swappings
# Display it is Task 4
print("*" * 9)
print("* Task 4 *")
print("*" * 9)

# Swap the first and third service timing
[Hours_S1,Minutes_S1,Seconds_S1], [Hours_S3,Minutes_S3,Seconds_S3] = [Hours_S3,Minutes_S3,Seconds_S3], [Hours_S1,Minutes_S1,Seconds_S1]

# Display the updated bookings
print("\n\nAfter the swaps of timings")
print("=" * 28)
print()
print("{0:<19} {1:<9} {2:<9} {3:<10}".format("Service","Hours","Minutes","Seconds"))
print("-" * 50)
print("{0:<19} {1:<9} {2:<9} {3:<10}".format(S1,Hours_S1,Minutes_S1,Seconds_S1))
print("{0:<19} {1:<9} {2:<9} {3:<10}".format(S2,Hours_S2,Minutes_S2,Seconds_S2))
print("{0:<19} {1:<9} {2:<9} {3:<10}".format(S3,Hours_S3,Minutes_S3,Seconds_S3))
print("\n\n")


# Task 5: Compute the charges and display a table for final charges
# Display it is Task 5
print("*" * 9)
print("* Task 5 *")
print("*" * 9)

# Calculation for time usage and total costs
# Time Usage
Usage_S1 = Hours_S1 * 3600 + Minutes_S1 * 60 + Seconds_S1
Usage_S2 = Hours_S2 * 3600 + Minutes_S2 * 60 + Seconds_S2
Usage_S3 = Hours_S3 * 3600 + Minutes_S3 * 60 + Seconds_S3
# TC = Total Costs
TC_S1 = Usage_S1 * UC_S1
TC_S2 = Usage_S2 * UC_S2
TC_S3 = Usage_S3 * UC_S3
TC = (TC_S1+TC_S2+TC_S3)/100

# Display summary of charges
print("\n\nSummary of charges")
print("=" * 20)
print()
print("{0:20}{1:<10}{2:<10}{3:<10}{4:<15}{5:<15}{6:15}".format("Service","Hours","Minutes","Seconds","Usage (secs)","Unit charge", "Total costs"))
print("-" * 90)
print("{0:20}{1:<10}{2:<10}{3:<10}{4:<15}{5:<15}{6:<15}".format(S1,Hours_S1,Minutes_S1,Seconds_S1,Usage_S1,UC_S1,TC_S1))
print("{0:20}{1:<10}{2:<10}{3:<10}{4:<15}{5:<15}{6:<15}".format(S2,Hours_S2,Minutes_S2,Seconds_S2,Usage_S2,UC_S2,TC_S2))
print("{0:20}{1:<10}{2:<10}{3:<10}{4:<15}{5:<15}{6:<15}".format(S3,Hours_S3,Minutes_S3,Seconds_S3,Usage_S3,UC_S3,TC_S3))
print("=" * 90)
print("{0:80}{1:<15}".format("Total cost",TC_S1+TC_S2+TC_S3))
print("{0:80}{1:<15.2f}".format("Singapore $",TC))
print("\nThank you for using our service")
print("An invoice of payment $ {0} will be sent to {1}".format(TC,email))

# last statement of program
input("\nEnter any character to end")