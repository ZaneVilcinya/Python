print("Welcome to the unit converter")

kilometres = int(input("Enter kilometres"))

miles = int(kilometres * 0.621)
print(miles)

repeat = input("Would you like to make another conversion? (Y/N)")
while repeat == "Y":
    kilometres = int(input("Enter kilometres"))

    miles = int(kilometres * 0.621)
    print(miles)

    repeat = input("Would you like to make another conversion? (Y/N)")
else:
    print("Ok. Goodbye")