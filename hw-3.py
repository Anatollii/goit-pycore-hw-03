import re

def normalize_phone(phone_number: str) -> str:

    cleaned_number = re.sub(r"[^\d+]", "", phone_number) #видаляємо всі елементи окрім чисел та +
    cleaned_number = re.sub(r"^380", r"+380", cleaned_number ) #заміняємо замість 380 на +380
    cleaned_number = re.sub(r"^(?!\+380)(\d{9,10})$", lambda m: "+38" + m.group(1), cleaned_number) #беремо все окрім елементів з +380 та додаємо до них +38
    return cleaned_number


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

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)