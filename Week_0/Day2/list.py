# Task 1: Display each value in the list.
numbers = [1, 2, 3, 4]
print([value for value in numbers])

# Task 2: Display each value multiplied by 20.
print([value * 20 for value in numbers])

# Task 3: Get the first letter of each name.
names = ["Elie", "Tim", "Matt"]
first_letters = [name[0] for name in names]
print(first_letters)

# Task 4: Select the even numbers.
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = [number for number in numbers if number % 2 == 0]
print(even_numbers)

# Task 5: Find unique values shared by both lists, preserving list1 order.
list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
common_numbers = [
    number
    for index, number in enumerate(list1)
    if number in list2 and number not in list1[:index]
]
print(common_numbers)

# Task 6: Lowercase each name and reverse its letters.
lowercase_reversed = [name.lower()[::-1] for name in names]
print(lowercase_reversed)

# Task 7: Find unique letters shared by both strings, preserving first's order.
first = "first"
third = "third"
common_letters = [
    letter
    for index, letter in enumerate(first)
    if letter in third and letter not in first[:index]
]
print(common_letters)

# Task 8: Find numbers from 1 through 100 that are divisible by 12.
divisible_by_12 = [number for number in range(1, 101) if number % 12 == 0]
print(divisible_by_12)

# Task 9: Keep the non-vowel characters from the word.
word = "amazing"
vowels = "aeiou"
consonants = [letter for letter in word if letter not in vowels]
print(consonants)

# Task 10: Create a 3-by-3 nested list containing 0, 1, and 2 in each row.
three_by_three = [[column for column in range(3)] for row in range(3)]
print(three_by_three)

# Task 11: Create a 10-by-10 nested list containing 0 through 9 in each row.
ten_by_ten = [[column for column in range(10)] for row in range(10)]
print(ten_by_ten)
