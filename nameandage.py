name = input("What is your name?")
print("Hello " + name)
age = int(input("How old are you?"))
if 31 > age >= 18:
    # if age is between 18 and 31
    print("Welcome to the holiday, {}".format(name))
else:
    print("Sorry, no entry")

