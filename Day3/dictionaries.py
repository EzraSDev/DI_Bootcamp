jlist = [("name", "Elie"),("job", "Instructor")]
jdic=dict(jlist)
print(jdic)

# for val in jlist:
#     jdic[val[0]]=val[1]
# print(jdic)


list1 = ["CA", "NJ", "RI"]
list2 = ["California", "New Jersey", "Rhode Island"]
newlist = list(zip(list1,list2))
print(newlist)


vowels = ['a', 'e', 'i', 'o', 'u']
new_dict = {}
for val in vowels:
    new_dict[val] = 0
print(new_dict)


alpha_dict = {}
for val in range(65, 91):
    alpha_dict[val - 64] = chr(val)
print(alpha_dict)
