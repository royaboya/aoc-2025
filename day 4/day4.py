with open("./day 4/input.txt","r") as file:
    # need to parse into 2d array
    rolls = file.readlines()
    #rolls = [line.rstrip("\n") for line in file if line.strip() != ""]

    rolls = [s.strip('\n') for s in rolls]
    #rolls = [line.rstrip("\n") for line in file if line.strip() != ""]

    rolls = [i for i in rolls if i != ""]

# how to check if out of bounds?

# (y, x), (x,y) doesnt matter
possible_edge_directions = [
    (-1,-1), (-1, 0), (-1, 1),
    (0, -1), (0, 1),
    (1, -1), (1, 0), (1,1)  
]

def is_valid_coord(x, y, len_rolls, len_row):
    return 0 <= x < len_rolls and 0 <= y < len_row

#print(rolls[10])


total = 0


for i in range(len(rolls)):
    row_of_rolls = rolls[i]
    
    for j in range(len(row_of_rolls)):
        
        # invalid if x < 0, x > len(row) - 1
        # invalid if y < 0, y > range(rolls) - 1
        
        count = 0
        for dir in possible_edge_directions:
            x = i + dir[0] 
            y = j + dir[1]
            
            try:
                if is_valid_coord(x, y, len(rolls), len(row_of_rolls)):
                    if rolls[x][y] == "@":
                        count += 1
                        #print(f"{x}, {y} is good ")
                        #rolls[x][y] = "x"                 
            except IndexError:
                #print(f"({x}, {y}) to {len(rolls)} and {len(row_of_rolls)}")
                pass
                
                # oh my god the logic to check is so aids
        
        if count < 4 and rolls[i][j] == "@":
            total += 1
            
            
print(total)





