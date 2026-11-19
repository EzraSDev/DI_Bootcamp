import random

list_of_numbers = [random.randint(0, 10000) for _ in range(20000)]

target_number   = 3728

def find_pairs(list_of_numbers, target_number):
    found_pairs = []
    unique_pairs = set()
    seen_numbers = set()

    for number in list_of_numbers:
        complement = target_number - number
        if complement in seen_numbers:
            pair = (min(number, complement), max(number, complement))
            if pair not in unique_pairs:
                found_pairs.append(pair)
                unique_pairs.add(pair)
        seen_numbers.add(number)

    return found_pairs


if __name__ == "__main__":
    pairs = find_pairs(list_of_numbers, target_number)
    for first_number, second_number in pairs:
        print(
            first_number,
            "and",
            second_number,
            "sum to the target number",
            target_number,
        )
