import random

c= 1
b= 100
i= 0
while (1):
    
    a = random.randint(c+1,b-1)
    print(a)
    i+=1
    print(i,".is this number equal to your supposed number?")
    string = input()
    if ( string == 'k'):
        
        b = a;
        
    elif ( string == 'b'):
        
        c = a;
        
    else:
        
        print("nice job!!")
        break;
                
        
        