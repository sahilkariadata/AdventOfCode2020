from day9_1 import numbers, invalid_no

for i in range(len(numbers)):
    finalset = []
    c = 0
    while sum(finalset) < invalid_no:
        if int(numbers[i]) == invalid_no:
            continue

        finalset.append(int(numbers[i+c]))
        c += 1
        if sum(finalset) == invalid_no:
            e_weakness = min(finalset) + max(finalset)
            print(e_weakness)
            break



