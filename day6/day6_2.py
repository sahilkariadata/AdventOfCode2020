answers = open("day6data.txt").read().split('\n\n')
total_sum = 0

for group in answers:
    individuals = group.split('\n')
    if len(individuals) == 1:
        total_sum += len(set(individuals[0]))
    else:
        crossover = set(individuals[0])
        for i in individuals:
            crossover = crossover.intersection(set(i))
        crossover.discard('\n')
        total_sum += len(crossover)

print(total_sum)
