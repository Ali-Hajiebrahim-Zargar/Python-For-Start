import statistics

class student :
    
    def __init__(self, n , age, weight, height):
        
        self.number = n
        self.age    = list(map(float,age))
        self.weight = list(map(float,weight))
        self.height = list(map(float,height))
        
    def print_mean (self) :
        
        print (statistics.fmean(self.age))    
        print ( statistics.fmean(self.height))    
        print ( statistics.fmean(self.weight))  
        
    def return_mean_weight(self):
        
        return  statistics.mean(self.weight)  
    
    def return_mean_height(self):
        
        return  statistics.mean(self.height)  
        
##################################################################
print("please enter the number of students in the first class:")

n1 = int(input())

print("please enter the age of students in class 1:")

age1 = input().split()

print("please enter the height of students in class 1:")

height1 = input().split()    

print("please enter the weight of students in class 1:")

weight1 = input().split()                   

class1 = student(n1,age1,weight1,height1)
##################################################################
print("please enter the number of students in the second class:")

n2 = int(input())

print("please enter the age of students in class 2:")

age2 = input().split()

print("please enter the height of students in class 2:")

height2 = input().split()    

print("please enter the weight of students in class 2:")

weight2 = input().split()                 

  

class2 = student(n2,age2,weight2,height2)
##################################################################
class1.print_mean()
class2.print_mean()

if (class1.return_mean_height() > class2.return_mean_height()):
    
    print("class 1")
    
elif  (class2.return_mean_height() > class1.return_mean_height()): 
    
    print("class 2")
    
elif  (class2.return_mean_height() == class1.return_mean_height()): 
    
    if  (class2.return_mean_weight() > class1.return_mean_weight()):
        
        print("class 1")
        
    elif  (class1.return_mean_weight() > class2.return_mean_weight()):     
    
        print("class 2")
        
    else:
        
        print("same")    