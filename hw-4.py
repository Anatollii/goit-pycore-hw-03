from datetime import datetime, timedelta
def get_upcoming_birthdays(users):
    today = datetime.today().date()
    next_week = today + timedelta(days=7)

    upcoming_birthdays = []

    for user in users:
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()

        # перевіряємо чи не пройшов день народження
        # перевіряємо чи не піздніше 7 днів день народження
        if (birthday.month, birthday.day) >= (today.month, today.day) and \
            (birthday.month, birthday.day) <= (next_week.month, next_week.day):

            upcoming_birthdays.append({
                "name": user["name"],
                "congratulations_date": f"{today.year}.{birthday.month:02}.{birthday.day:02}"
            })

    return upcoming_birthdays

users = [
    {"name": "John Doe", "birthday": "1985.03.12"},  # Завтра
    {"name": "Jane Smith", "birthday": "1990.03.15"},  # Через 4 дні
    {"name": "Alice Brown", "birthday": "1995.04.01"}  # Далеко за 7 днів
]

print(get_upcoming_birthdays(users))


