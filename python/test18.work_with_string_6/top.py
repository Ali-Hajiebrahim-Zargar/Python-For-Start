print("please enter your string")
a= input()
check_flg = 0
for i in range(0,len(a)//2):
    
    if a[i]==a[len(a)-i-1] :
        
        continue
        
    else:
        
        print("not palindrome")
        check_flg = 1
        break
    
if check_flg == 0:
       print("palindrome")    
    