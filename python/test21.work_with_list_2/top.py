print("please enter the number of collaboration:")

my_list = input().split()

length = 0
for i in range(0,len(my_list)):
    
    if int(my_list.pop()) < 3 :
        
        length = length+1
    
length = length//3

print("the number of group is %i" % length)        