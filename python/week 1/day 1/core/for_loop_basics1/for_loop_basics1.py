# Print all integers from 0 to 150 
for i in range(51) :
    print(i)



#Print all the multiples of 5 from 5 to 1,000
for i in range(5,1001) :
    if i % 5 == 0 :
        print(i)


#Print integers 1 to 100. If divisible by 5, print "Coding" instead. If divisible by 10, print "Coding Dojo".
for i in range(1,101) : 
    if i % 10 == 0 :
        print("Coding Dojo") 
    elif i % 5 == 0 :
        print("Coding")
    else :
        print(i)


#Add odd integers from 0 to 500,000, and print the final sum.
total_sum = 0
for i in range(501000) :
    if i % 2 != 0 :
        total_sum +=i 
print(total_sum)


# Print positive numbers starting at 2018, counting down by fours
for i in range(2018,-1,-4) :
    if i > 0 :
        print(i)




#Flexible Counter
lowNum = 20
highNum = 60
mult = 3
for i in range(lowNum,highNum) :
    if i % mult == 0 :
        print(i)