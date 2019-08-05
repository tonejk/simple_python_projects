from random import randrange
from time import perf_counter

randNum = randrange(1, 101)
guess = 0
guessCount = 0
startTime = perf_counter()

while True:
    guess = int(input("Guess a number between 1-100: "))
    guessCount = guessCount + 1
    if guess < randNum:
        print("Your guess is lower!")
    elif guess > randNum:
        print("Your guess is higher!")
    else:
        print("Your guess is correct!")
        endTime = perf_counter() - startTime
        break

print("Number is", randNum)
print("You guessed", guessCount, "times!")
print("It took", endTime, "seconds!")
