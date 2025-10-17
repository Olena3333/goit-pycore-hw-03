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
    
print(get_days_from_today('2020-10-09'))
print(get_days_from_today('2025-12-12'))
print(get_days_from_today('09-10-2020'))  
print(get_days_from_today('2020/10/09'))  
print(get_days_from_today('2020-13-01'))