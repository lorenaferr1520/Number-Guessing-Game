# Number Guessing Game
from random import randint

computador = int()
user = int()
attempts = 0
nivel = {
    1 : 50,
    2: 100,
    3: 500   
}

while True:
    dificuldade = int(input('''Choose the difficulty:
            [1] EASY
            [2] MEDIUM
            [3] HARD    -->  '''))

    if dificuldade == 1:
        computador = randint(1, 50)
        break
    elif dificuldade == 2:
        computador = randint (1, 100)
        break
    elif dificuldade == 3:
        computador = randint (1, 500)
        break
    else:
        print('Invalid option!')

    
while True:
    while True:
        num = int(input('Guess the number: '))
        if num > nivel[dificuldade]:
            print(f'Enter a number less than {nivel[computador]} ')
        else: 
            break
    
    if num == computador:
        attempts += 1
        print(f'✨ Congratulations! You guessed it in {attempts} attempts!')
        break 
    elif num < computador:
        print('📈 Higher! Try again.')
        attempts += 1
    elif num > computador:
        print('📉 Lower! Try again.')
        attempts += 1