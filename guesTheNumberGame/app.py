# gues the random number from 0-10, u've got 3 try's
import random
secretNumber = random.randint(0,10)
guessCount = 0
guessLimit = 3
print('Guess the number from 0 - 10')
while guessCount < guessLimit:

    guess = int(input('Guess: '))
    guessCount += 1
    if guess == secretNumber:
        print('Congratulations! U won! ')
        print(f'Guess times:{guessCount}')
        break
    else:
        print('Failed! Try again')