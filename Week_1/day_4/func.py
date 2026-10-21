from functools import reduce

# Predict all the values in expressions.
# Write a program that prints:
# 1. The number of True values in expressions['booleans']
# 2. The average of all positive numbers in expressions['numbers']


# expressions = {
#     "booleans": [
#         bool(None), #false
#         "a" > "?", #true
#         str(5) in "5", #true
#         float(0.99) == int(0.99), #false
#         not bool("A"), #fasle
#     ],
#     "numbers": [
#         (" " in "Hello World") * 3.5, #hello   World
#         True + 5, #6
#         "Magical".count("a") - 6.5 #4
#         sum(x for x in range(11)),
#         sum(x for x in range(3, 13, 3) if x % 3 < 2),
#     ],
# }
def fun(*args):      #that allows me to pass as many arguments as i want if i dont know how many i want to call
    sum = 0
    for i in args:
        sum += i
    return sum
# if i use 2 * i get a dictionary back, so **kwargs is KeyWordsArguments,

def calculation(*n, operation =  "+"):
    if len(n)<2:
        return "Something is wrong, try again!"
    if  operation == "+":
        return sum(n)
    if operation != "-":
        return "Something is wrong, try again!"

    return reduce(lambda a ,b: a -b, n)


print(calculation(1,2,3,4 ,operation="-")),
