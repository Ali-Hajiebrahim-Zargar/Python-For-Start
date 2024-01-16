print("please enter your desired word:")
a=input()
b="hello"
j=0
for letter in range(0,len(a)):
    if a[letter]==b[j]:
        j=j+1;
    else:
        continue
    
if j == 5:
    print("Yes")

else:
    print("No")            