print("Please inset a 3 digit number : ")
a= int(input())

b = a%10
c = (a%100 - b)/10
d = a//100

if d > 9 :
    print ("forbidden value")
    
else :
    e= 2*((100*b)+(c*10)+d)
    print ("double of inverse number is : ", e )    