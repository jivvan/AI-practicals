import random

words = ['pathaan', 'jawan', 'mohabbatein', 'raees', 'Raone'
         , 'don', 'fan', 'devdas', 'darr', 'swades', 'chamatkar',
          'pardes', 'baazigar']

word = random.choice(words)

print('Guess the characters:')

guessed_chars = ''

chances = 5

while chances > 0:
    failed = 0

    for char in word:
        if char in guessed_chars:
            print(char, end='')
        else:
            print("_", end='')
            failed+=1
    if failed == 0:
       print() 
       print('You Win.')
       print(f'The word is {word}.')
       break

    print()
    guess = input('guess a character:')
    guess = guess.lower()

    if guess not in word:
        chances -= 1
        print('Wrong')
        print(f'You have {chances} more guesses.')

        if chances == 0:
            print('You lose.')
            break
    else:
        guessed_chars += guess