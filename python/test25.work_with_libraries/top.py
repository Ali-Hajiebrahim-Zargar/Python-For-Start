import math
my_list = []

print("please inter the number of numbers:")
n = int(input())

for i in range(0,n):
    print("please enter %i number:" %(i+1))
    my_list.extend(input())

for j in range(0,n):
    
    print('{:.4f}'.format(math.sqrt(int(my_list[j]))))
    
