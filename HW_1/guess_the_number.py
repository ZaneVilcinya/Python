from random import randint

guess = randint(0, 100)
number = int(input("Imagine the number: "))

while guess != number:
    print("Let the computer guess: ", guess)
    if guess > number:
        guess = randint(0, 100)
        print("L")
    elif guess < number:
        guess = randint(0, 100)
        print("M")

print(guess, number)
print("P")
