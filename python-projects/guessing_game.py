import math
# 3 tries to guess a random number

secret_number = 3
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess = int(input('Guess: '))
    guess_count += 1
    if guess == secret_number:
        print('You win!')
        break
else:
    print('Game over')



