# Qn 1

# temp = float(input("Enter water temperature: "))
# 
# if temp >= 100:
#     state = "gas"
# elif temp > 0:
#     state = "liquid"
# else:
#     state = "solid"
#     
# print(f"State of water at {temp} degree Celsius is {state}")


# Qn 2

# adultCost = 15
# childCost = 10
# showCost = 5
# freeSunshadePrice = 100
# discountPrice = 150
# discountPercent = 10
# 
# num_Adults = int(input("Enter no. for adults: "))
# num_Child= int(input("Enter no. for children: "))
# show = input("Animal show (y/n)?: ")
# friend = input("Friend of zoo (y/n): ")
# 
# total_Cost = adultCost*num_Adults + childCost*num_Child
# 
# 
# if (show =="y"):
#     total_Cost += showCost*(num_Adults+num_Child)
# 
# if (total_Cost >= freeSunshadePrice):
#     print("Free sunshade for everyone!")
#     
# if (total_Cost >= discountPrice or friend =="y"):
#     print(f"You got a {discountPercent}% discount")
#     total_Cost = total_Cost * (1-discountPercent/100)
#     
# print(f"Total cost:${total_Cost}")


# Qn 3

# names = ["alan", "peter","john"]
# 
# # Write the code to add ‘mary’ to the end of list
# names.append("mary")
# print(names)
# 
# # Write the code to add ‘bob’ as the first item of the list
# names.insert(0,"bob")
# print(names)
# 
# # Write the code to remove ‘peter’ from the list
# names.remove("peter")
# print(names)
# 
# # Write the code to remove the 2nd item from the current list
# del names[1]
# print(names)
# 
# # Write the code to print out the number of people in the list
# print(len(names))


# Qn 4

# c = 3
# while (c<=23):
#     print(c)
#     c+=4
# print()
# 
# c =	30
# while (c>=20):
#     print(c)
#     c-=2
# print()


# Qn 5

#range() => generate a number sequence
# print(list(range(10))) #0 to 10-1
# print(list(range(5,11))) # 5 to 11-1
# print(list(range(0,11,2))) # 1to 11-1 step of 2
# 
# print(list(range(12,25,3)))
# 
# for num in range(12,25,3):
#     print(num)
# print()
# 
# print(list(range(46,25,-4)))
# for num1 in range(46,25,-4):
#     print(num1)

#num_list = [12,15,18,21,24]

#for num in num_list:
#    print(num)



#aList=["a","b","c"]

#for item in aList:
    #print(item)


# Qn 6

# n=9
# for i in range(n):
#     print("A|"*n)
#     
# print()
# 
# n=5
# for i in range(1,n+1):
#     print("+="*i)

# n = 5
# for i in range(n,0,-1):
#     print("B|"*i)

#  n = 9
#  c = 1
#  for i in range(n,0,-1):
#      print(":>" * i + "   " + ":P" * c)
#      c+=1


# n = 9
# for i in range(n,0,-1):
#     c = (n+1)-i
#     print(":>" * i + "   " + ":P" * c)


# Qn 7

# n = 50000
# harmonic_sum=0
# 
# for i in range(1,n+1):
#     harmonic_sum += 1/i
# 
# print(harmonic_sum)


# Qn 8

# n = 30
# fibo1 = 0
# fibo2 = 1
# 
# print(fibo1)
# print(fibo2)
# 
# for i in range(n-2): # i=> 	0			1			2
#     fibo = fibo1 + fibo2 	# f=0+1 =1 	 f=1+1=2	f=1+2=3
#     print(fibo) 			# print(1)   p(2)		p(3)
#     fibo1 = fibo2 		#f1 = 1      f1 = 1
#     fibo2 = fibo 			#f2 = 1      f2 = 2


# Qn 9

# animals = ["fish","cat","dog","lion","tiger","mouse","cow"]
# 
# #  Using a for loop, print all the animals
# for animal in animals:
#     print(animal)
#     
# print()
# 
# # Using a for loop, print all the animals in reverse order
# print(len(animals))
# r_index = list(range(len(animals)))
# r_index.reverse()
# print(r_index)
# 
# for i in r_index:
#     print(animals[i])
# 
# # 				range (7-1,-1,-1) -> [6,5.....0]
# r_index = list(range(len(animals)-1,-1,-1))
# print(r_index)
# 
# for i in r_index:
#     print(animals[i])
# 
# print()
# 
# animals.reverse()
# for animal in animals:
#     if(len(animal)==3):
#         print(animal)


# Qn 10

# import statistics as stats
# numbers = []
# 
# carryOn = True
# while(carryOn):
#     
#     num = input("Enter a number or q to quit: ")
#     if (num=="q"):
#         carryOn = False
#     else:
#         num = float(num)
#         numbers.append(num)
#         
# print(numbers)
# 
# lowest = min(numbers)
# highest = max(numbers)
# print(lowest,highest)
# average = stats.mean(numbers)
# stdev = round(stats.stdev(numbers),3)
# print(average,stdev)

# check on python statistics


# Qn 11

#import math

# def area_circle(radius):
#     area = math.pi * radius ** 2
#     return area
# 
# def area_triangle(base,height):
#     area = 0.5 * base * height
#     return area
# 
# upper_area = area_triangle(10,5)-area_triangle(3,2)
# lower_area = area_circle(6)*2
# total = round(upper_area + lower_area,3)
# 
# print(f"Total shaded area {total} ")


# # Qn 12
# 
# def number_range(num_list):
#     lowest = min(num_list)
#     highest = max(num_list)
#     return lowest,highest
# 
# #use a loop
# def number_range2(num_list):
#     lowest = num_list[0]
#     highest = num_list[0]
#     for num in num_list:
#         if(num<lowest):
#             lowest = num
#         if(num>highest):
#             highest = num
#     return lowest,highest
# 
# # sort the list, first -> lowest, last -> highest
# def number_range3(num_list):
#     sorted_list = sorted(num_list)
#     lowest = sorted_list[0]
#     highest = sorted_list[-1]
#     return lowest,highest
# 
# aList = [5,4,3,4,5,6,7,2,6]
# lowest,highest = number_range(aList)
# print(lowest,highest)
# lowest,highest = number_range2(aList)
# print(lowest,highest)
# lowest,highest = number_range3(aList)
# print(lowest,highest)


# Qn 13

# laptops = {"acer":20, "hp":10, "toshiba":15, "apple":12}
# #
# 
# for brand in laptops.keys():
#     print(f"{brand}:{laptops[brand]}")
# print()
# 
# print("Brand with stock >= 15")
# for brand in laptops.keys():
#     if(laptops[brand]>=15):
#         print(f"{brand}:{laptops[brand]}")
#         
# print()
# 
# total = 0
# for stock in laptops.values():
#     total += stock
#     
# print(f"total:{total}")
# print(laptops["acer"])
# laptops["acer"] = 50
# print(laptops)
# 
# laptops["abc"] = 20
# print(laptops)
# 
# print(len(laptops))
# print(laptops.keys())
# print(laptops.values())


# Qn 14

#			0		1		2		3
# names = ["alan", "peter", "mary", "john"]
# ages = [17, 18, 19, 20]
# 
# friends = {}
# #len(names)=>4
# #range(4) => [0,1,2,3]
# for i in range(len(names)):
#     print(names[i],ages[i])
#     friends[names[i]] = ages [i]
#     
# print(friends)
    
