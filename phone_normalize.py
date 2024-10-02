import re

def phone_normalize(phone: str) -> str:
    # Remove all characters except digits using regular expression
    number = re.sub(r'[^0-9]', '', phone)


    # If the number starts with "380", return it as is with a "+" prefix
    if number.startswith("380"):
        return "+" + number

    # If the number starts with "38", add a "+" in front of it
    elif number.startswith("38"):
        return "+" + number

    # Otherwise, add "+38" to the beginning of the number
    else:
        return "+38" + number


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

sanitized_numbers = [phone_normalize(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)
