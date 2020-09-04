import random

#Creates a random number from 1 to 20

def main():
    randomNum = random.randint(1, 20)
    guesses = 1
    guess = int(input("Guess a number from 1-20: "))
    while guess != randomNum:

        if guess < randomNum:
            print("Too Low.")
            guess = int(input("Try again. "))
            guesses += 1
        elif guess > randomNum:
            print("Too High.")
            guess = int(input("Try again. "))
            guesses += 1
       

    if guess == randomNum:
        print("You guessed correctly! It took you " + str(guesses) + " tries!")
    

main()

    
