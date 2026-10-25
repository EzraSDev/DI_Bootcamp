import random

list_of_numbers = [random.randint(0, 10000) for _ in range(20000)]

target_number   = 3728

def find_pairs(list_of_numbers, target_number):
    pairs =[]
    for i in list_of_numbers:
        for j in range(i + 1, len(list_of_numbers)):
            if list_of_numbers[i] + list_of_numbers[j] == target_number:
                pair = (list_of_numbers[i], list_of_numbers[j])
                if pair not in pairs:
                    pairs.append((list_of_numbers[i],list_of_numbers[j]))
                    print(list_of_numbers[i], "and", list_of_numbers[j], "sums to the target_number", target_number)
    
find_pairs(list_of_numbers, target_number)
