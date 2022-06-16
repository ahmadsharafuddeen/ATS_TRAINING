digits = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight",
        9: "nine", 10: "ten"}
tens = {2: "twenty", 3: "thirty", 4: "fourty", 5: "fifty", 6: "sixty", 7: "seventy", 8: "eighty",
        9: "ninety"}
exceptions = {1: "eleven", 2: "twelve", 5: "fifteen", 8: "eighteen"}

number = list(input("Enter a number to convert to words: "))
# print(number)

result = ""
changing = len(number)
for num in number:
    if changing == 4:
        result += f"{digits[int(num)]} thousand, "
        changing -= 1
        continue
    if changing == 3:
        result += f"{digits[int(num)]} hundred and "
        changing -= 1
        continue
    if changing == 2:
        if int(num) == 1:
            last_digit = int(number[-1])
            if last_digit in exceptions.keys():
                result += exceptions[last_digit]
                break
            result += f"{digits[last_digit]}teen"
            break
        result += f"{tens[int(num)]} "
        changing -= 1
        continue
    result += f"{digits[int(num)]}"
    
print(result)