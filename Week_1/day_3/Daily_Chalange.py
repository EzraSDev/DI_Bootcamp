#Challenge 1

word = input("Please enter a word:")
my_dict = {}
for val in range(len(word)):
    char = word[val]
    if char in my_dict:
        my_dict[char].append(val)
    else:
        my_dict[char] = [val]
print(my_dict)

#Challenge 2

items_purchased = {"Water": "$1", "Bread": "$3", "TV": "$1,000", "Fertilizer": "$20"}
wallet = "$300"

items_purchased2 = {"Apple": "$4", "Honey": "$3", "Fan": "$14", "Bananas": "$4", "Pan": "$100", "Spoon": "$2"}
wallet2 = "$100"

items_purchased3 = {
"Phone": "$999", "Speakers": "$300", "Laptop": "$5,000", "PC": "$1200"
}
wallet3 = "$1"


def affordable_items(items_purchased, wallet):
    wallet = int(wallet.replace("$","").replace(",", ""))
    basket= []
    for item, price in items_purchased.items():
        price = int(price.replace("$","").replace(",", ""))
        if wallet >= price:
            basket.append(item)
            wallet-= price

    if not basket:
        return "Nothing"
    else:
        return(sorted(basket))

print(affordable_items(items_purchased, wallet))