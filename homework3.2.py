from random import randint, sample
min = 1 
max = 36
quantity = 5

result_array = set()
while len(result_array) != quantity:
    result_array.add(randint(min, max))

def get_numbers_ticket(min, max, quantity):
    if not (1 <= min <= max <= 100) or not (1. <= quantity <= (max - min +1)):
       print(sorted(list(result_array)))

print(sorted(sample(range(min, max), quantity)))
    


    



