import random

wordslist = ['correction', 'childish', 'beach', 'python', 'assertive', 'interference',
             'complete', 'share', 'credit card', 'rush', 'south']
body_parts = ["head", "body", "left arm", "right arm", "left leg", "right leg"]


def guess_letter(guessed_letters):
    while True:
        letter = input("Guess your letter: ").lower()
        if len(letter) != 1:
            print("Nope! Enter ONE letter")
            continue
        if letter in guessed_letters:
            print("You have already tried that letter")
            continue
        return letter


def display(word, guessed_letters):
    outline = ""
    for char in word:
        if char in guessed_letters or char == " ":
            outline += char
        else:
            outline += "_"
    return outline

def show_mistakes(mistakes, body_parts):
    print("Body parts:",", ".join(body_parts[:mistakes]))
    print(f"You have {6 - mistakes} guesses left")

def check_end_game(mistakes, word, outline):
    if outline == word:
        print("Congratulations, you won!!!!!")
    elif mistakes ==6:
        print(f"Too bad, Youre out of tried, better luck next time, youur word was {word}")


def play():
    word = random.choice(wordslist)
    mistakes = 0
    guessed_letters = []
    outline = ""

    while mistakes < 6 and "_" in display(word, guessed_letters):
        print(f"\nGuessed: {', '.join(guessed_letters)}")
        print(display(word, guessed_letters))
        letter = guess_letter(guessed_letters)
        guessed_letters.append(letter)
        if letter not in word:
            mistakes += 1
        outline = display(word, guessed_letters)
        show_mistakes(mistakes, body_parts)
        print("-" * 30)

    check_end_game(mistakes, word, outline)



play()