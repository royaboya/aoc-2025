# part 1 
# just read into an array and assuming the input is m x n and # operations are equal then we can just 
# use indices to do the operations
import math

with open("./day 6/input.txt","r") as file:
    numbers = file.readlines()
    
    numbers = [s.strip("\n").strip(' ') for s in numbers]
    numbers = [s.split(' ') for s in numbers]
    numbers = [[element for element in row if element != ""] for row in numbers]        

"""
columns = [[row[i] for row in numbers] for i in range(len(numbers[0]))]

total = 0
for arr in columns:
    op = arr[-1]
    print(op)
    
    arr = [int(n) for n in arr[:-1] if n not in "*+"]

    
    if op == "*":
        result = math.prod(arr)
        #print(f"Adding {result} from *")

    elif op == "+":
        result = sum(arr) 
        #print(f"Adding {result} from +")
        
        
    #print(arr)
    total += result
        
print(f"part 1: {total}")
"""


# part 2
# reading right to left




with open("./day 6/test.txt","r") as file:
    numbers = file.readlines()
    
    numbers = [s.strip("\n").strip(' ') for s in numbers]
    numbers = [s.split(' ') for s in numbers]
    numbers = [[element for element in row if element != ""] for row in numbers]   

columns = [[row[i] for row in numbers] for i in range(len(numbers[0]))]


for col in columns:
    print(col)

"""
Plan is to continue grouping each number together with their respective operators

Addition:
- place digits are read from the right
- right to left would be ones, tens, hundredths, etc, need to find length of longest str, etc

Multiplication:
 - same logic as addition but mutliplication


top to bottom order matters so read array of input as same?
i.e read left to right?

get max length of int?

"""

