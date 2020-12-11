import numpy as np
adapters = open("day10data.txt").read().splitlines()
adapters = [int(i) for i in adapters]
adapters.sort()
adaptershift = adapters[1:]
adaptershift.append(adapters[-1]+3)

differences = np.array(adaptershift) - np.array(adapters)
differences = np.append(differences,min(adapters))
ones = np.count_nonzero(differences == 1)
threes = np.count_nonzero(differences == 3)
print(ones*threes)