from unittest import result


def determine_ordinal(num: int):
    to_append = {1: 'st', 2: 'nd', 3: 'rd'}
    exceptions = [11, 12, 13]
    app = ''
    last_num = num % 10
    if last_num in to_append and num % 100 not in exceptions:
        app = to_append[last_num]
    else:
        app = 'th'
    return f"{num}{app}"

    
    