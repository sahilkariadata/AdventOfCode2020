import math
seat_locs = open("day5data.txt").read().splitlines()

#Thought about using recursion but opted for iteration for speed
def rowcol_finder(loc,lower_limit,upper_limit):
    for i in range(len(loc)):
        if loc[i] == 'B' or loc[i] == 'R':
            lower_limit = math.ceil((lower_limit+upper_limit)/2)
        elif loc[i] == 'F' or loc[i] == 'L':
            upper_limit = math.floor((lower_limit+upper_limit)/2)
        else:
            print("An error has occurred")
    return(lower_limit)

seat_ids = []

for loc in seat_locs:
    row_loc = rowcol_finder(loc[:7],0,127)
    col_loc = rowcol_finder(loc[7:],0,7)
    seat_ids.append((row_loc*8)+col_loc)

print(max(seat_ids))
