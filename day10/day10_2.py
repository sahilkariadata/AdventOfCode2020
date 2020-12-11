from day10_1 import differences
import numpy as np
differences = differences.tolist()
oneset = []
c = 0

possibility_dict = {1:1,2:2,3:4,4:7,5:11}

for i in differences: 
    if i == 1:
        c += 1
    else:
        if c > 0:
            oneset.append(possibility_dict[c])
            c = 0

combinations = np.prod(np.array(oneset))
print(combinations)
