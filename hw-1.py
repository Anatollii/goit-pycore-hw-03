from datetime import datetime
import sys

def get_days_from_today(date: str) -> str:
    input_date = datetime.strptime(date, "%Y-%m-%d").date()
    today_date = datetime.today().date()
    delta = today_date - input_date
    return delta.days

if len(sys.argv) < 2:
    print("No argument provided. Please provide an argument.")
else:
    try:
        print("Days:", get_days_from_today(sys.argv[1]))
    except ValueError as e:
        print("Input error:", e)
