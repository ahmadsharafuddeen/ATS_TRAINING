import pprint

message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
counts = {}

for char in message:
    counts.setdefault(char, 0)
    counts[char] += 1
    
# pprint.pprint(counts)
print(pprint.pformat(counts))