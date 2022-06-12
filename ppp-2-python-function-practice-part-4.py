from cmath import pi
from re import I

#Utils
def int_or_default(number,default):
    if type(number) == int:
        return number
    return int_or_default(default,0)

def fancy_print_list(numList):
    if isinstance(numList,list) == False:
        print(0)
    if len(numList) == 0:
        print(0)    
    fancy_display = ""
    for num in numList:
        fancy_display = f"{fancy_display} {num}"
    print(fancy_display)

# Write a Python function called max_num()to find the maximum of three numbers.

def max_num_pair(a,b):    
    if int_or_default(a,0) < int_or_default(b,0):
        return b
    return a

def max_num(x,y,z):
    v = max_num_pair(x,y)
    v = max_num_pair(v,z)   
    return v

max_num_results1 = max_num(10,20,30)
print(max_num_results1)
max_num_results2 = max_num(11,33,22)
print(max_num_results2)
max_num_results3 = max_num(88,77,66)
print(max_num_results3)
max_num_results4 = max_num(1,1,1)
print(max_num_results4)
max_num_results5 = max_num('A','99',1)
print(max_num_results5)
max_num_results6 = max_num('A',99,1)
print(max_num_results6)
max_num_results7 = max_num('A','B','C')
print(max_num_results7)

# Write a Python function called mult_list() to multiply all the numbers in a list.
def mult_list(numList):
    if isinstance(numList,list) == False:
        return 0
    if len(numList) == 0:
        return 0    
    mult_result = 1
    for num in numList:
        mult_result = mult_result * int_or_default(num,1)
    return mult_result
mult_list_result1 = mult_list([1,2,3])
print(mult_list_result1)
mult_list_result2 = mult_list([1,'2',3])
print(mult_list_result2)
mult_list_result3 = mult_list([1,2,3,4,5,6,7,8,9])
print(mult_list_result3)

# Write a Python function called rev_string() to reverse a string.
def rev_string(text):
    rev_text = ""
    for index in range(len(text)-1,-1,-1):
        rev_text = rev_text + text[index]
    return rev_text

print(rev_string('araz'))
print(rev_string('shahinian'))
print(rev_string('nicole'))

# Write a Python function called pascal() that prints out the first n rows of Pascal's triangle.

def pascal(n):
    base_num = 1
    myList = [base_num]
    prevList = []
    fancy_print_list(myList)
    for x in range(base_num,int_or_default(n,1)+1):
        for y in range(base_num,x):
            myList.append(y)                   
        for z in range(x,base_num-1,-1):
            myList.append(z)
        newList = []
        prevNum = 0
        for i in prevList:
            newList.append(i+prevNum)
            prevNum = i
        if len(prevList)==0:
            fancy_print_list(myList)
            prevList = myList 
        else:
            newList.append(1)
            fancy_print_list(newList)
            prevList = newList               
        myList = []     
        
        
pascal(3)
pascal(5)
pascal(7)