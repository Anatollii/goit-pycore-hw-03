import random
def get_numbers_ticket(min: int, max: int, quantity: int) -> list:
    if not (1 <= min <= max <= 1000 and min <= quantity <= (max - min + 1)):
    #if (1 <= min <= max <= 1000) or not (min <= quantity <= (max - min + 1)):
        return []
    numbers = random.sample(range(min, max+1), quantity)
    return sorted(numbers)




lottery_numbers = get_numbers_ticket(1, 1000, 6)
print("Ваші лотерейні числа:", lottery_numbers)