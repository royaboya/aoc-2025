with open("./day 1/input.txt", "r") as file:
    instructions = file.readlines()

start = 50
count = 0 

for instr in instructions:
    instr_type = instr[0]
    
    if instr_type == "R":
        start += int(instr[1::])
        
    elif instr_type == "L":
        start -= int(instr[1::])
    else:
        print("Invalid Instruction")
    
    start = start % 100
    if start == 0:
        count += 1
        
print(f"PART 1 PASSCODE: {count}")        

# part 2
start = 50
count = 0
for instr in instructions:
    instr_type = instr[0]
    moves = int(instr[1::])
    
    while moves > 99:
        moves -= 100
        count +=1
    
    if instr_type == "R":
        # negative = start < 0 
        start += moves
        if start > 100:
            count += 1
     
    elif instr_type == "L":
        pos = start > 0
        start -= moves
        
        if start < 0 and pos:
            count += 1
            
    start = start % 100
    
    if start == 0:
        count +=1

print(f"PART 2 PASSCODE: {count}")
    
    
    









