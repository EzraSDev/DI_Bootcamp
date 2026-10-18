##################   daily challenge     ##########################

phrase = input("Please enter a string with exaclty 10 characters:")
if len(phrase) <10:
    print("String not long enough.")
elif len(phrase) > 10:
    print("String too long.")
else: 
    print("Perfect string")
    print(phrase[0],phrase[-1])
    newpharese=""
    for val in phrase:
        newpharese+=val
        print(newpharese)
