print("please enter the number of comparison:")
my_list = []
n = int(input())
flag = 0
quality_ref = 0
price_ref=0

for i in range(0,n):
    print("please inter the %i cost and quality:" %(i+1))
    my_list.extend(input().split())
    
#print(my_list)    
for j in range(0,len(my_list),2):
    price_ref=int(my_list[j])
    quality_ref = int(my_list[j+1])
    
    print("price_ref is", price_ref)
    print("quality_ref is", quality_ref)

#    print("the j is ",j)
    for k in range(0,len(my_list),2):
#        print("the k is ",k)
#        print("my_list[k] is", my_list[k])
#        print("my_list[k+1] is", my_list[k+1]) 
        if flag == 1:
            break
               
        if (int(my_list[k])> price_ref) and (quality_ref>int(my_list[k+1])): 
            
            print("ok")
            flag = 1
            break
        
        elif (int(my_list[k])< price_ref) and (quality_ref < int(my_list[k+1])):
            
            print("ok")            
            flag = 1
            break
        

            
if flag == 1:
    print("happy irsa")
else:
    print("poor irsa")    