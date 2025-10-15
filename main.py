# Task 1
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
    
print("Task 1")
print(get_days_from_today('2020-10-09'))
print(get_days_from_today('2025-12-12'))
print(get_days_from_today('09-10-2020'))  
print(get_days_from_today('2020/10/09'))  
print(get_days_from_today('2020-13-01'))  

# Task 2
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

print("Task 2")
lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)


# Task 3
import re

def normalize_phone(phone_number: str) -> str:
    phone_number = phone_number.strip()
    if phone_number.startswith('+'):
        format_number = '+' + re.sub(r'\D', '', phone_number[1:])
    else:
        format_number = re.sub(r'\D', '', phone_number)
        if format_number.startswith("380"):
            format_number = '+' + format_number
        else:
            format_number = '+38' + format_number

    return format_number

raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

print("Task 3")
sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)