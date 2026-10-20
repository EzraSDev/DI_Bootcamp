# sample_dict = {"name": "Kelly", "age": 25, "salary": 8000, "city": "New york"}
# keys_to_remove = ["name", "salary"]
# for keys in keys_to_remove:
#    del  sample_dict[keys]
# print(sample_dict)


# my_new_list= []
# for i in range(5):
#    my_new_list.append (i * 2)
# #same as the one above
# my_new_list = [i * 2 for i in range(5)]


# my_string = "Hello World"
# #a, e, i, o, u

my_dict = {"first_name" : "John"
           ,"last_name" : "Doe"
           ,"age" :30}
new_name = ["New Name", "New Last Name"]
my_new_dictionary = {}
my_new_dictionary = my_dict.copy()
my_new_dictionary.update(zip(["first_name","last_name"],new_name))
# my_new_dictionary.update(new_name)
print(my_new_dictionary)
