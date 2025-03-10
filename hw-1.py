from datetime import datetime
try:
    def get_days_from_today(date: str) -> str:
        input_date = datetime.strptime(date, "%Y-%m-%d").date()
        today_date = datetime.today().date()
        delta = today_date - input_date
        return delta.days

except ValueError:
    raise ValueError("Некорректный формат даты. Используйте формат 'YYYY-MM-DD'.")
print(get_days_from_today("2025-03-15"))
