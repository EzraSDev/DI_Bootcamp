# # Exrecise 1

keys = ["Ten", "Twenty", "Thirty"]
values = [10, 20, 30]
result = dict(zip(keys, values))
print(result)

# # Exercise 2

family = {"rick": 43, "beth": 13, "morty": 5, "summer": 8}
total_price = 0
for name, age in family.items():
    if age > 2 and age < 13:
        ticke_price = 10
        total_price += ticke_price
    elif age > 12:
        ticke_price = 15
        total_price += ticke_price
    else:
        ticke_price = 0

    family[name] = {"age": age, "ticke_price": ticke_price}

print(total_price)
print(family)

# # Exercise 3

brand = {
    "name": "Zara",
    "creation_date": 1975,
    "creator_name": "Amancio Ortega Gaona",
    "type_of_clothes": "men, women, children, home",
    "international_competitors": "Gap, H&M, Benetton",
    "number_stores": 7000,
    "major_color": {"France": "blue", "Spain": "red", "US": "pink, green"},
}

more_on_zara = {"creation_date": 1975,
                 "number_stores": 7000}

print(brand)
brand["number_stores"] = 2
print(brand)
print(
    f"Everyone can use zaras clothes they are a good fit for everyone and everywhere {brand["type_of_clothes"]} "
)
brand["country_creation"] = "Spain"
del brand["creation_date"]
print(brand["international_competitors"])
print(brand["major_color"]["US"])
print(len(brand))
print(brand.keys(), "\n")
zara = brand | more_on_zara
brand.update(more_on_zara)
print(brand)
print(zara)

# # Exercise 4

users = ["Mickey", "Minnie", "Donald", "Ariel", "Pluto"]
new_users = {users: i for i, users in enumerate(users)}
# or
# new_users = dict(zip(users, range(len(users))))
print(users)
users_2 = dict(enumerate(users))
print(users_2)
aplha_users = dict(zip(sorted(users), range(len(users))))
print(aplha_users)
