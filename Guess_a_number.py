import random

def guess(a):
    random_no= random.randint(1,a)        #take the random value from the range of 1 and a(any value come through the function)
    guess = 0                          #intialize the value for guess before starting the loop    
    while guess != random_no:              #compare the guess value with the random value
        guess= int(input(f'Guess a number between 1 and {a}: '))
        #check the guessed number is high or low than the actual random number
        if guess > random_no:         
            print ("Please guess again, guess a smaller number")
        elif guess < random_no:
            print("Please guess again, guess a larger number")
    print(f'You have guess the correct number as {random_no}')

guess(10) 