answers = open("day6data.txt").read().split('\n\n')
total_sum = 0
for group in answers:
    unique_answers = set(group)
    unique_answers.discard("\n")
    total_sum += len(unique_answers)

print(total_sum)
