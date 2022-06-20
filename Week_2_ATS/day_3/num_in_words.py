digits = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight",
        9: "nine"}
tens = {2: "twenty", 3: "thirty", 4: "forty", 5: "fifty", 6: "sixty", 7: "seventy", 8: "eighty",
        9: "ninety"}
exceptions = {0: "ten", 1: "eleven", 2: "twelve", 3: "thirteen", 5: "fifteen", 8: "eighteen"}

number = input("Enter a number between 0-9999 to convert: ")
# print(number)

result = ""
changing = len(number)
for num in number:
    last_digit = int(number[-1])
    if changing == 1 and int(number[0]) == 0:
        result += "zero"
        break
    if changing == 4:
        result += f"{digits[int(num)]} thousand"
        changing -= 1
        if number[1:] == '000':
            break
        continue
    if changing == 3:
        if int(num) == 0:
            changing -= 1
            continue
        if result != '':
            result += f", {digits[int(num)]} hundred"
            changing -= 1
            continue
        result += f"{digits[int(num)]} hundred"
        changing -= 1
        if number[1:] == '00': 
            break
        continue
    if changing == 2:
        if int(num) == 0:
            changing -= 1
            continue
        if int(num) == 1:
            if last_digit in exceptions:
                if result != '':
                    result += f" and {exceptions[last_digit]}"
                    break
                result += f"{exceptions[last_digit]}"
                break
            if result != '':
                result += f" and {digits[last_digit]}teen"
                break
            result += f"{digits[last_digit]}teen"
            break
        if result != '':
            changing -= 1
            if last_digit != 0:
                result += f" and {tens[int(num)]} {digits[int(number[-1])]}"
                break
            result += f" and {tens[int(num)]}"
            break
        if last_digit != 0:
            result += f"{tens[int(num)]} {digits[last_digit]}"
            break
        result += f"{tens[int(num)]}"
        break
    if result != '':
        if int(num) == 0:
            break
        result += f" and {digits[int(num)]}"
        continue
    result += f"{digits[int(num)]}"
print(result)

# print('2100'[2:])

