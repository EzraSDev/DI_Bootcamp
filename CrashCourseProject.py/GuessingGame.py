import random

def number_guessing_game():
    MAX_ATTEMPTS = 7
    answer = random.randint(1, 100)
    greetings = "Lets play!!! Guess between 1-100:"
    for val in range(MAX_ATTEMPTS):
        guess = int(input(greetings))
        if guess == answer:
            print("NIce Guess you wont the game!")
            break
        elif val == MAX_ATTEMPTS - 1:
            print("too bad, the answer was:" + str(answer))
        elif guess > answer:
            print("Too high!")
        else:
            print("Too low!")
        greetings = "try again:"


number_guessing_game()
