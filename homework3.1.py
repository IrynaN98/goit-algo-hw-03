from datetime import datetime

def get_days_from_today(date):
    try:
        input_date = datetime.strptime(date, "%Y-%m-%d").date()
        current_date = datetime.today().date()
        delta =  (input_date - current_date).days

        return delta
    except ValueError:
        print("Неправильний формат дати. Використовуйте формат 'РРРР-ММ-ДД'.")
        return None
    
input_date = '2024-05-15'
delta= get_days_from_today(input_date)
if delta is not None:
    print(f"Різниця у днях між заданою датою '{input_date}' і поточною датою:", delta)