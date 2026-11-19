# Exercise 1: Create a dictionary from the key-value pairs.
pairs = [("name", "Elie"), ("job", "Instructor")]
person = {key: value for key, value in pairs}
print(person)

# Exercise 2: Pair each state abbreviation with its full name.
abbreviations = ["CA", "NJ", "RI"]
state_names = ["California", "New Jersey", "Rhode Island"]
states = {abbreviation: name for abbreviation, name in zip(abbreviations, state_names)}
print(states)

# Exercise 3: Create a dictionary with each vowel mapped to zero.
vowels = ["a", "e", "i", "o", "u"]
vowel_counts = {vowel: 0 for vowel in vowels}
print(vowel_counts)

# Exercise 4: Map the numbers 1 through 26 to lowercase letters.
alphabet = {number: chr(number + 96) for number in range(1, 27)}
print(alphabet)

# Exercise 5: Count each vowel in the phrase.
phrase = "awesome sauce"
phrase_vowel_counts = {vowel: phrase.count(vowel) for vowel in "aeiou"}
print(phrase_vowel_counts)
