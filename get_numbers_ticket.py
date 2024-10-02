import random

def get_numbers_ticket(min: int, max: int, quantity: int)->list:
    # Check entry value, where min >=1 and max <= 1000
    if min >= max or quantity > max-min or min < 1 or max > 1000:
        return []

    # Generate unique random numbers
    return sorted(random.sample(range(min, max+1), quantity))

print(get_numbers_ticket(10, 100, 10))
print(get_numbers_ticket(0, 100, 100))
print(get_numbers_ticket(10, 100, 100))