# Challenge 1

words = input("Enter a few words:").split(",")
def sort_join(words):
    words.sort()
    print(",".join(words))
    print(words)

sort_join(words)

# Challenge 2

def longest_word(sentence):
    words = sentence.split()
    longest = ""
    for word in words:
        if len(word) > len(longest):
            longest = word
    
    return longest

pharese= input("Enter a sentence:")
print(longest_word(pharese))