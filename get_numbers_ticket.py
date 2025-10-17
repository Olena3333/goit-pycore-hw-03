import random

def get_numbers_ticket(min_value, max_value, quantity):

    if type(min_value) != int or type(max_value) != int or type(quantity) != int:
        return []

    if min_value < 1 or max_value > 1000:
        return []
    
    if quantity < 1 or quantity > max_value - min_value + 1:
        return []
    
    numers = random.sample(range(min_value, max_value + 1), quantity)
    return sorted(numers)

lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)