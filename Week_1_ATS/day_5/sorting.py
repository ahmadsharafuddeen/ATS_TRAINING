def sort_sentence(sentence):
    split_sent = sentence.split('-')
    split_sent.sort()
    return "-".join(split_sent)

# print(['green', 'red', 'yellow', 'black', 'white'].sort())

print(sort_sentence('green-red-yellow-black-white'))