#Exercise 1
print("Hello world\n" * 4, end = "")
#Exercise 2
print((99**3)*8)
#Exercise 3
# 5 < 3 False
# 3 == 3 True
# 3 == "3" False
# "3" > 3 Error/false
# "Hello" == "hello" false
#exercise 4
computer_brand = "HP"
print(f"I have a {computer_brand} computer")
#Exercise 5 
name = "Ezra"
age = 28
shoe_size = 44
info = f"Hello, my name is {name}, Im {age} and fun fact my shoe size is {shoe_size}"
print(info)
#Exercise 6
a=0
b=2
if a>b:
    print("Hello World")

# Exercise 7
num=int(input("Enter a number:"))
if num%2 == 0:
    print("Even number!")
else:
    print("Odd number!")

#Exercise 8
my_name = "Ezra"
your_name = input("Please enter your name:")
if my_name == your_name:
    print("Same name! we can be friends")
else:
    print("thats a weird name, why dont you try mine?")
# Exercise 9
min_height = 145
height = int(input("Please enter your height:"))
if height>min_height:
    print("Yay you can ride!!!")
else:
    print(f"Im sorry you need to ve over {min_height}cm tall to ride this")

