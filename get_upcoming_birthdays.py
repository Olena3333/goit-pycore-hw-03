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