import random

def guess_user(x):
    random_number = random.randint(1,x) # we create range of number from it we could retrive number
    guess=0 #default value which doesn't belong to range

    #loop is be alive while we'll guess right number(random number)
    while guess !=random_number:
        guess = int(input(f"Guess a number between 1 and {x}:  "))
        if guess < random_number:
            print("Sorry, guess again. Too low")
        elif guess>random_number:
            print("Sorry, guess again. Too high.")

    print(f"Yeah, congrats, You have guessed the number{random_number} rigth!!!")

#guess(10)

def computer_guess(x):
    low=1
    high=x
    guess=0

    feedback = '' # if we enter the 'c' letter Computer guess wright number!!
    while feedback !='c':
        # during computer guessing our range would be narrow and when high=low we break loop
        if low != high:
            guess = random.randint(low, high) # computer take number in range(low, high)
        else:
            guess=low
        # for normal conditions when high != low
        feedback = input(f'Is {guess} too high (H), too low (L) or correct? (C)').lower()
        if feedback == 'h':
            high = guess-1
        if feedback == 'l':
            low = guess+1
    print(f"Yay! The computer guessed your number, {guess}, correctly!")