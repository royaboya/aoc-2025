with open("./day 2/input.txt", "r") as file:
    ids = file.readlines()
    ids = ids[0].split(",")

def is_invalid_pt1(id:str):
    id_len = len(id)
    
    if len(id) == 2:
        return id[0] == id[1]
    
    first = 0
    mid = id_len // 2
    
    return id[0:mid] == id[mid::]

 
total = 0 
for id_range in ids:

    ranges = id_range.split("-")
    start = int(ranges[0])
    end = int(ranges[1])
    
    for i in range(start, end+1):
        if is_invalid_pt1(str(i)):
            total += i
            

print(f"Part 1: {total}")


def is_invalid_pt2(id:str):
    mid = len(id) // 2
    
    # test all candidates
    for i in range(mid):
        # if the candidate block divides evenly, try to see if it makes the string
        if len(id) % (i+1) == 0:
            candidate = id[0:(i+1)]
            repeat_times = len(id) // (i+1)
            if candidate * repeat_times == id:
                return True
            else:
                #print(f"{candidate * repeat_times} != {id}")
                continue
        else:
            continue
        
        
    return False

total = 0 
for id_range in ids:

    ranges = id_range.split("-")
    start = int(ranges[0])
    end = int(ranges[1])
    
    for i in range(start, end+1):
        if is_invalid_pt2(str(i)):
            total += i
            

print(f"Part 2: {total}")
# print(is_invalid_pt2("123"))
# print(is_invalid_pt2("123123"))
# print(is_invalid_pt2("1231234"))

