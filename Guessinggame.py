import random

highest = 10
quit = 0
answer = random.randint(1, 10)
print(answer)
print("Please guess a number between 1 and {}. You can quit by entering {}. ".format(highest, quit))
guess = int

while guess != answer:
    guess = int(input())

    if guess == 0:
        print("Goodbye")
        break
    if guess == answer:
        print("Correct")
        break
    if guess > answer:
        print("Too high")
    if guess < answer:
        print("Too low")

