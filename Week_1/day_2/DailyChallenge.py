#Challenge 1

num = int(input("Enter a number:"))
length = int(input("Enter a length:"))
new_num = 0
num_list = []
for i in range(length):
    new_num += num
    num_list.append(new_num)

print(num_list)

# Challenge 2

word = input("Enter a string: ")
new_word = word[0]

for i in range(1, len(word)):
    if word[i] != word[i - 1]:
        new_word += word[i]

print(new_word)
