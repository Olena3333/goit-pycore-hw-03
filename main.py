# Task 1
from datetime import datetime

def get_days_from_today(date_str: str)-> int:
    try:
        date = datetime.strptime(date_str, "%Y-%m-%d").date() 
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

# Task 4
from datetime import datetime, timedelta

def get_upcoming_birthdays(users):
    result = []

    today = datetime.today().date()
    print(f"today {today}")
    end_date = today + timedelta(days=7)
    print(f"end_date {end_date}")

    for user in users:
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        birthday_this_year = birthday.replace(year=today.year)
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)
        if today <= birthday_this_year <= end_date:
            congratulation_date = birthday_this_year
            if congratulation_date.weekday() in (5, 6): 
                days_to_monday = 7 - congratulation_date.weekday()
                congratulation_date += timedelta(days=days_to_monday)
            result.append({
                "name": user["name"],
                "congratulation_date": congratulation_date.strftime("%Y.%m.%d")
            })

    return result

print("Task 4")    
users = [
    {"name": "Андрій Яблуко", "birthday": "1990.10.15"},    
    {"name": "Марина Апельсин", "birthday": "1992.10.16"},  
    {"name": "Олег Банан", "birthday": "1985.10.18"},       
    {"name": "Інна Груша", "birthday": "1991.10.19"},       
    {"name": "Сергій Ківі", "birthday": "1988.10.20"},      
    {"name": "Тетяна Персик", "birthday": "1993.10.25"},    
]

birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", birthdays)