numbers = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen',
        14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen'}
tens = {2: "twenty", 3: "thirty", 4: "forty", 5: "fifty", 6: "sixty", 7: "seventy", 8: "eighty",
        9: "ninety"}

def convert_to_words(number):
    words = ""
    if number == 0:
        return "Zero"
    if number < 0:
        return f"minus {abs(number)}"
    if number // 1000 > 0:
        process = number // 1000
        words += f"{convert_to_words(process)} thousand "
        number %= 1000
    if number // 100 > 0:
        process = number // 100
        words += f"{convert_to_words(process)} hundred "
        number %= 100
    if number > 0:
        if number < 20:
            words += numbers[number]
        else:
            words += tens[number // 10]
            if number % 10 > 0:
                words += " " + numbers[number % 10]
    return words

print(convert_to_words(1125))
# print(1125 // 100)

import pyinputplus