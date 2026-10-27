import random

# Validate a 10-character string, display it progressively, and shuffle it.
##################   daily challenge     ##########################

phrase = input("Please enter a string with exactly 10 characters:")
if len(phrase) < 10:
    print("String not long enough.")
elif len(phrase) > 10:
    print("String too long.")
else:
    print("Perfect string")
    print(phrase[0], phrase[-1])
    new_phrase = []
    for val in phrase:
        new_phrase.append(val)
        print("".join(new_phrase))

    shuffled_phrase = list(phrase)
    random.shuffle(shuffled_phrase)
    print("Shuffled string:", "".join(shuffled_phrase))
