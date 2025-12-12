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

# brute force attempt is too slow/takes too much memory, need to aggregate the ranges and then take the difference in each range
# then take the sum of those differences for the answer


def get_end(range):
    return int(range.split('-')[1])

def get_start(range):
    return int(range.split('-')[0])

# range1 < range2
def merge_ranges(range1, range2):
    # aggregate ranges here
    start = min(get_start(range1), get_start(range2))
    end = max(get_end(range1), get_end(range2))
    
    return f"{start}-{end}"
    

sorted_ranges = sorted(ranges, key=lambda x: int((x.split('-')[0])))
fully_merged_ranges = []

curr_range = sorted_ranges[0]

# if curr.end >= next.start -> merge -> set to_be_merged = curr, increment i
# else, add to finished range

i = 1

while i <= (len(sorted_ranges) - 1):
    if get_end(curr_range) >= get_start(sorted_ranges[i]):
        merged = merge_ranges(curr_range, sorted_ranges[i])
        curr_range = merged
        i+=1
    else:
        fully_merged_ranges.append(curr_range)
        curr_range = sorted_ranges[i]
        i+=1

# add last range if a merge happens at the end
fully_merged_ranges.append(curr_range)

#print(fully_merged_ranges)

# for i in range(len(fully_merged_ranges) - 1):
#     print(get_end(fully_merged_ranges[i]) < get_start(fully_merged_ranges[i+1]))


    # pick a range
    # go next, if merge, merge
    # go next, if not merge, add current finished merge
    # then pick next merge as next iter    


count = 0
for i in fully_merged_ranges:
    count += (get_end(i) - get_start(i) + 1)

print(count)

 



