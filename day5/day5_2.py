from day5_1 import seat_ids
sorted_ids = sorted(seat_ids)
my_id = (len(sorted_ids)+1)*(sorted_ids[0]+sorted_ids[-1])/2 - sum(seat_ids)
print(my_id)