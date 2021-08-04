# This is a guess the number game
import random

print('Hello. What is your name?')
name = input()

print('Well, ' + name + ', I am thinking of a number from 1 to 20.')
secretNumber = random.randint(1, 20)

# Ask the player to guess 6 times.
for guessesTaken in range(1, 7):
    print('Take a guess.')
    guess = int(input())

    if guess < secretNumber:
        print('Your guess is too low.')
    elif guess > secretNumber:
        print('Your guess is too high.')
    else: 
        break # Correct guess

if guess == secretNumber:
    print('Good job ' + name + '! You guessed my number in ' + str(guessesTaken) + ' guesses!')
else:
    print('Nope. The number I was thinking of was ' +str(secretNumber))