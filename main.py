from datetime import datetime

def get_days_from_today(date_str: str)-> int:
    try:
        date = datetime.strptime(date_str, "%Y-%m-%d").date() #str parse date
        today = datetime.today().date()
        resalt= (today - date).days
        print(resalt)
        return resalt
    except ValueError:
        print("Помилка: Неправильний формат дати. Використовуйте формат 'РРРР-ММ-ДД'.")
        return None
print(get_days_from_today('2020-10-09'))
print(get_days_from_today('2025-12-12'))
print(get_days_from_today('09-10-2020'))  
print(get_days_from_today('2020/10/09'))  
print(get_days_from_today('2020-13-01'))  

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
