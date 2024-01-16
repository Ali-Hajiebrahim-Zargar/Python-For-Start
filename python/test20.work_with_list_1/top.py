print("please enter the first location:")
x1= input()

print("please enter the second location:")
x2= input()

print("please enter the third location:")
x3= input()

my_list=[x1,x2,x3]

my_list.sort()

dis= int(my_list[2]) - int(my_list[0])

print(dis)
