print("please enter your string:")
a=input()
a = a.upper()
first= "AB"
second="BA"
flag_AB=0
flag_BA=0

for i in range(0, len(a)-1):
    if a[i]==first[0] and a[i+1]==first[1]:
        flag_AB = 1
        
    elif a[i]==second[0] and a[i+1]==second[1]:
         flag_BA = 1
               
if flag_AB == 1 and flag_BA == 1 :
    
    print("YES")
    
else:
    
    print("NO")    