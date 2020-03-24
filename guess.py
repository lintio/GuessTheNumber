import random, os

answer = random.randint(1, 10)
guess = 100

os.system('cls' if os.name == 'nt' else 'clear')
print('Guess the number between 1 and 10 (type 0 to quit)')
while guess != 0:
    userInput = input('Your guess -> ')
    guess = int(userInput)
    if guess == 0:
        break
    elif guess == answer:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('Guess the number between 1 and 10 (type 0 to quit)')
        print('Well done!! you guessed the correct number (a new number has been selected)')
        answer = random.randint(1, 10)
    elif guess > answer:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('Guess the number between 1 and 10 (type 0 to quit)')
        print('Your guess was to high try again')
    elif guess < answer:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('Guess the number between 1 and 10 (type 0 to quit)')
        print('your guess is to low try again')