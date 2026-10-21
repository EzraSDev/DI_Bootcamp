import random

# Exercise 1


def display_message():
    print("I am learning about functions in Python.")


display_message()

# Exercise 2


def favorite_book(title):
    print(f"One of my favorite books is {title}")


book = "Harry potter"
favorite_book(book)

# Exercise 3


def describe_city(city, country="unknown"):
    print(f"{city} is in {country}")


city1 = "SP"
country1 = "Brazil"

describe_city(city1, country1)
describe_city(
    city1,
)

# Exercise 4


def r(num):
    othernum = random.randint(1, 100)
    message = ""
    if num > 0 and num < 101 and othernum == num:
        message = "Yes the number match!"
    else:
        message = f"Fail! Your number {num}, random number {othernum}"

    return message


my_num = 18
print(r(my_num))

# Exercise 5


def make_shirt(size="large", text="I love python"):
    print(f"The size of this shirt is {size} and the text is {text}")


small_size = "small"
medium_size = "medium"
shirt_text = "Custom message"

make_shirt()
make_shirt(medium_size)
make_shirt(small_size, shirt_text)

# Exercise 6


def show_magicians(magicians):
    print(magicians)


def make_great(magicians):

    magicians = list(map(lambda name: "the great " + name, magicians))
    return show_magicians(magicians)


magician_names = ["Harry Houdini", "David Blaine", "Criss Angel"]

make_great(magician_names)


#  Exercise 7


def get_random_temp():
    temp = random.randint(-10, 40)
    return temp


def main():
    temp = get_random_temp()
    print(f"The temperature right now is {temp} degrees Celsius")
    if temp < 0:
        print("Brrr, that’s freezing! Wear some extra layers today.")
    elif temp < 17:
        print("Quite chilly! Don’t forget your coat")
    elif temp < 23:
        print("Nice weather")
    elif temp < 33:
        print("A bit warm, stay hydrated")
    else:
        print()
