#   Exercise 1 Lists
l=[1,2,3,4]
for val in l:
    print(val)

for val in l:
    print(val*20)


names = ["Elie", "Tim", "Matt"]
f_letter = []
for val in names:
    f_letter.append(val[0])

print(f_letter)
numbers = [1,2,3,4,5,6]
new_num = []
for val in numbers:
    if val%2==0:
        new_num.append(val)

list1 = [1,2,3,4]
list2 = [3,4,5,6]
list3 = []
for val in list1:
    for val2 in list2:
        if val == val2:
            list3.append(val)

low_invers= []
for val in names:
    val = val.lower()
    val = val[::-1]
    low_invers.append(val)

print(low_invers)

first = "first"
third = "third"
pos = []
for val in first:
    for val2 in third:
        if val == val2:
            pos.append(val)
print(pos)
div12 = []
for i in range(1,101):
    if i%12 ==0:
        div12.append(i)

print(div12)
stg = "amazing"
vowels = "aeiou"
consonants = []
for letter in stg:
    if letter not in vowels:
        consonants.append(letter)
print(consonants)


full_list = []
for i in range(3):
    list1 = []
    for j in range(3):
        list1.append(j)
    full_list.append(list1)

print(full_list)


full_list = []
for i in range(10):
    list1 = []
    for j in range(10):
        list1.append(j)
    full_list.append(list1)

print(full_list)
