# Exercise 1
print("Hello Wolrd\n" *4 + "I love python\n" * 4, end = "")
#Exercise 2
month = int(input("Please enter a month from 1-12:"))
if month > 2 and month < 6:
    print("Spring")
elif month > 5 and month < 9:
    print("Summer")
elif month >8 and month < 12:
    print("Autumn")
else:
    print("Winter")
