# day 1 brute force

with open("./day 5/input.txt", "r") as file:
    # need to strip new lines
    id_input = file.readlines()
    id_input = [s.strip('\n') for s in id_input]
    idx = id_input.index("")
    
    ranges = id_input[0:idx]
    numbers = id_input[idx+1::]
    

# sort ranges by start, then just iteratively go through and check

valid = set()


def in_range(range, number):
    range_split = range.split("-")
    
    number = int(number)
    # print(range_split[0])
    # print(range_split[1])
    
    return number >= int(range_split[0]) and number <= int(range_split[1])


for r in ranges:
    for number in numbers:
        if in_range(r, number):
            #print(f"{number} valid for {range}")
            valid.add(number)
             
        else:
            #print(f"{number} not valid for {range}")
            continue

print(len(valid))
 
# part 2 aggregate the ranges for faster processing? or just brute force it

# brute force attempt is too slow, need to aggregate the ranges and then take the difference in each range
# then take the sum of those differences for the answer
# fresh = set()

# for r in ranges:
#     range_split = r.split("-")

#     start = int(range_split[0]) 
#     end = int(range_split[1])
    
#     for num in range(start, end+1):
#         if num not in fresh:
#             fresh.add(num)
#         else:
#             continue
        
# print(len(fresh))
# sort ranges by start
# then parse through and then merge


def get_end(range):
    return int(range.split('-')[1])


sorted_ranges = sorted(ranges, key=lambda x: int((x.split('-')[0])))
fully_merged_ranges = []

to_be_merged = sorted_ranges[0]

# aish figure merging this out at home 
for i in range(1, len(sorted_ranges)+1):
    if get_end(to_be_merged) 
    
    pass
    
    
    # pick a range
    # go next, if merge, merge
    # go next, if not merge, add current finished merge
    # then pick next merge as next iter    
    

 



