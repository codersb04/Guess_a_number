import random
print("User guessing computer's number")
#user guessing the computer number
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

guess(10050) 

#computer guessing the user number

print("Computer guessing user's choosen number")
def comp_num(a):
    low=1   #setting the range as low and high in order to help computer to guess the number
    high=a
    respond='' #intializing variable computer respong
    while respond != 'c':   #checking if the respond is correct or not 
        if low !=high:  #loop to avoid error caused same low and high value
            guess= random.randint(low,high)
        else:
            guess=low  #if high and low both as same we can assign either value in guess
        respond= input(f'Computer guessed number is {guess}, Is the guessed number larger(l), smaller(s) or correct(c)').lower()
        if respond == 'l':
            high = guess -1   #reducing the upper limit of the range with guess-1, narrowing down the range 
        elif respond == 's':   #increasing the lower limit of the range with guess + 1
            low=guess+1
    
    print(f'Computer has guess the right number{guess} ')


comp_num(1000)


