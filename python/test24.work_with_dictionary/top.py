print("please enter the number of vocabulary")
n = int(input())
my_dict = dict()
my_list=[]
my_list_sentence=[]
sentence = ''
for i in range(0,2*n,2):
    
    print("please inter the %i key and value for your dictionary:" %i)
    my_list.extend(input().split())
    key = my_list[i]
    value = my_list[i+1]
    my_dict[key]= value
    
print("please enter your sentences which should be translated:")
my_list_sentence.extend(input().split()) 

for i in range(0, len(my_list_sentence)):
    
    sentence = sentence + ' ' + my_dict.get(my_list_sentence[i],my_list_sentence[i])
    
print(sentence)    
      