with open("./day 3/input.txt", "r") as file:
    joltage_ratings = file.readlines()


# part 1
"""

joltages = []

for bank in joltage_ratings:
    
    candidate_one = int(bank[0])
    first_idx = 0
    
    for i in range(1, len(bank)-2):
        if int(bank[i]) > candidate_one:
            first_idx = i
            candidate_one = int(bank[i])
    
    # after we pick the maximum first digit, we pick the maximum second which follows 
    # the first since order matters
    candidate_two = int(bank[first_idx + 1]) # idk
    print(candidate_two)
    for j in range(first_idx + 1, len(bank) - 1):
        if int(bank[j]) > candidate_two:
            #print(f"new largest second candidate:{bank[j]}")
            candidate_two = int(bank[j])
    
    joltages.append(int(f"{candidate_one}{candidate_two}"))
    
print(sum(joltages))
"""

# part 2
# requirement is 12 digits
# greedy approach for 12 digits

cleaned_joltage_ratings = [
    [x.strip() for x in bank if x.strip() != '']
    for bank in joltage_ratings
]

joltages = []

for bank in cleaned_joltage_ratings:
    running_buf_length = 1
    joltage_buffer = ""
    END = 12
    dist_to_stop_from_end = END - running_buf_length
    
    prev = -1 # previous chosen idx 
    
    # bound = len(battery_voltages) - (12 - running buf)
     
    while running_buf_length <= 12: 
    
        candidate = int(bank[prev+1]) 
        cand_idx = prev + 1  

        for i in range(cand_idx + 1, (len(bank) - (END - running_buf_length))): 
            if int(bank[i]) > candidate:
                candidate = int(bank[i])
                cand_idx = i
        
        running_buf_length += 1
        joltage_buffer += str(candidate)
        prev = cand_idx
        
    joltages.append(joltage_buffer)
        
        
    
    # len(bank) minus what, need to ensure it doesnt gotoo far
    # every iteration need to recalculate how much we want to read up until
    
    # every iteration pick idx + 1 and search until bounds
    # repeat until size 12
    
    # search until bounds depends on length of running buffer
    
joltages = [int(_) for _ in joltages]
print(sum(joltages))
