#Countdown 
def countdown_list(num):
    countDown_list = [] 
    for i in range(num, -1, -1):
        countDown_list.append(i)  
    return countDown_list  
num = int(input("Enter a number: ")) 
result = countdown_list(num) 
print(result) 

#print and return 
def print_return(list) :
    print(list[0])
    return(list[1])
x = print_return([88,6])
print(x)



#first plus length
def first_length(lst) :
    return lst[0]+ lst[len(lst)-1]
y = first_length([5,12,4,23])
print(y)


#Values Greater than Second
def greater_than_second(lst):
    if len(lst) < 2 :
        return False 
    second_value = lst[1]
    arr = []
    for value in lst :
        if value > second_value :
            arr.append(value)
    return arr
x = greater_than_second([12,5,0,-5,79]) 
print(x)


#This Length, That Value 
def length_value(length,value) :
    if length == 0 :
        return []
    arr = [value] * length 
    return arr 
z= length_value(5,3) 
print(z)

