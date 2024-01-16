print("please enter your string: ")
a= input()
a=a.lower()
tool=len(a)
print(tool)
for i in range(0,tool):
#    print(i,'  ', a[i])

    if a[i]== 'a' or a[i]== 'e' or a[i]== 'i' or a[i]== 'o' or a[i]== 'u' :    
        if i == 0 :
            a = '.'+a[1:]            
        elif i == tool:
            a= a[(tool-2):]+'.'
        else:        
            a = a[:(i)]+'.'+a[(i+1):]    
            
    else:
        
        continue            
    
                          
print(a)    