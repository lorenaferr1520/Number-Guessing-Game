# Number Guessing Game
from random import randint

def linha():
    print('-=-' * 30)
niveis_config = {1: 50, 2: 100, 3: 500}
computador = int()
user = int()
attempts = 0
nivel = {
    1 : 50,
    2: 100,
    3: 500   
}
# nivel select
linha()
nivel = int()
while True:
    try:
        dificuldade = int(input('''Choose the difficulty:
                [1] EASY
                [2] MEDIUM
                [3] HARD    -->  '''))
    except ValueError:
        print('ERROR! only numbers! [1-2-3]')
        continue

    if dificuldade == 1:
        computador = randint(1, 50)
        nivel = 50
        break
    elif dificuldade == 2:
        computador = randint (1, 100)
        nivel = 100
        break
    elif dificuldade == 3:
        computador = randint (1, 500)
        nivel = 500
        break
    else:
        print('Invalid option!')

linha()
# verificação
while True:
    while True:
        try:
            num = int(input('Guess the number: '))
            if num >  nivel:
                print(f'Enter a number less than {nivel} ')
        except ValueError:
            print("❌ Invalid input! Please type a whole number.")
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
linha()