b = 0
a = 0
win = 0
draw = 0
defeat = 0

for i in range (1,31):
    print("please inter the score which obtained in",i," match: ")
    a = int(input())
    b = b + a
    
    if a == 3:
        win =win +1
        
    elif a==1:
        
        draw =draw+ 1
        
    elif a==0:
        
        defeat= defeat+1
        
    else:
        
        b = b - a;
        print("invalid score value")
        
print ("the number of totla score is ", b)
print ("the number of totla victory is ", win)
print ("the number of totla draw is ", draw)
print ("the number of totla defeat is ", defeat)

                
