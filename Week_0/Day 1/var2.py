# Exercise 2
years = int(input("Enter a number:"))
dog_years = 0
cat_years = 0
all_years = []
for i in range(years):
    if i < 1:
        dog_years += 15
        cat_years += 15
    elif i == 1:
        dog_years += 9
        cat_years += 9
    else:
        dog_years += 5
        cat_years += 4
all_years = [years, cat_years, dog_years]
print(all_years)
