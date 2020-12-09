numbers = open("day9data.txt").read().splitlines()
preamble = 25

for loc in range(preamble,len(numbers)):
    found = 0
    for i in range(preamble):
        for j in range(i+1,preamble):
            interval = numbers[loc-preamble:loc]
            if int(interval[i]) + int(interval[j]) == int(numbers[loc]):
                found = 1
    
    if found == 0:
        invalid_no = int(numbers[loc])
        print(invalid_no)
