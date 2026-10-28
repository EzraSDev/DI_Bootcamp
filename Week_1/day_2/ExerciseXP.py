# # Exercise 1

my_fav_numbers = {1,2,3,4}
print(my_fav_numbers)
last_element = list(my_fav_numbers)[-1]
my_fav_numbers.remove(last_element)
print(my_fav_numbers)
my_fav_numbers.remove(2)
print(my_fav_numbers)
friend_fav_numbers = {9,8,7,6}
our_fav_numbers = my_fav_numbers | friend_fav_numbers
print(our_fav_numbers)

# # Exercise 2

my_tuple = (1, 2, 3, 4)
# my_tuple.add(5)

# # Exercise 3

basket = ["Banana", "Apples", "Oranges", "Blueberries"]
basket.remove("Banana")
print(basket)
basket.pop()
print(basket)
basket.append("Kiwi")
print(basket)
basket.insert("Apples")
print(basket)
basket.count("Apples")
print(basket)
basket.clear()
print(basket)

# Exercise 4

float_list = [

]
num = 1.5
while num != 5.5:
    float_list.append(num)
    num += 0.5
print(float_list)

# Exercise 5

num = 1
while num <= 20:
    print(num)
    if num % 2 == 0:
        print(num)
    num += 1

# Exercise 6

while True:
    name = input("Enter your name:")
    if len(name) > 2  and not name.isdigit():
        print("Thank you")
        break
    else:
        continue

# Exercise 7

favorite_fruits = input("Enter your favorite fruits, separated by spaces: ").split()

fruit = input("Enter the name of any fruit: ")

if fruit in favorite_fruits:
    print("You chose one of your favorite fruits! Enjoy!")
else:
    print("You chose a new fruit. I hope you enjoy it!")

# Exercise 8

toppings = []
base_price = 10
topping_price = 2.50

while True:
    topping = input("Enter a pizza topping (or 'quit' to finish): ")

    if topping == "quit":
        break

    toppings.append(topping)
    print(f"Adding {topping} to your pizza.")

total_cost = base_price + len(toppings) * topping_price

print("Your toppings:", toppings)
print(f"Total cost: ${total_cost:.2f}")

# Exercise 9

ages = []
total_cost = 0

family_size = int(input("How many people are in your family? "))

for i in range(family_size):
    age = int(input("Enter the person's age: "))
    ages.append(age)

    if age < 3:
        total_cost += 0
    elif age <= 12:
        total_cost += 10
    else:
        total_cost += 15

print(f"Total ticket cost: ${total_cost}")