num_list = [1,2,3,4,5]

doubled_list = []
for n in num_list:
    doubled_list.append(n*2)
    
print(doubled_list)
    
doubled_list = [n*2 for n in num_list]
print(doubled_list)


doubled_odd_list = []
for n in num_list:
    if (n%2==1):
        doubled_odd_list.append(n*2)
print(doubled_odd_list)

doubled_odd_list = [n*2 for n in num_list if n%2 == 1]
print(doubled_odd_list)

name_list = ["John","Bob","Charles"]
name_char = []
# for name in name list, tell us the length of the name
for name in name_list:
    name_char.append(len(name))
    
print(name_char)

name_char = [len(name) for name in name_list]
print(name_char)

namelist = ["John","Bob","Charles"]
name_char = []
for name in namelist:
    if len(name)>=4:
        name_char.append(len(name))
print(name_char)

name_char = [len(name) for name in namelist if len(name)>=4]
print(name_char)
print()

print()

square_list = [n*n for n in range(1,11)]
print(square_list)

print()
num_list = [4,7,9]
triple_list = [n*3 for n in num_list]
print(triple_list)

print()


def double(x):
    return x*2

doubled_list = [double(n) for n in num_list]
print(doubled_list)

print()
names = ["Arthur","King","Of","Britons"]
initials = [s[0] for s in names]
print(initials)
print()
names = ["Arthur","King","Of","Britons"]
initials = [s[0] for s in names if len(s)>=4]
print(initials)

lowered = [s.lower() for s in ["JOHN","PETER","BOB"]]
print(lowered)

uppered = [s.upper() for s in ["asd","qwe","whee"]]
print(uppered)