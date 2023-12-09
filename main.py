import random
number = random.randint(1, 100)
print(number)

from art import logo
print(logo)


print("Welcome to number guessing game!".title())
print("I am Thinking of a number between 1 and 100.".title())
#user_choice = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

def hard_select():
    """This function is use to check the user guess number against the random number. and print result base on the result."""
    user_choice = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if user_choice == "hard":
        print("You have 5 attempts to answer")
        hard_life = 5
        while hard_life != 0:
            user_choice = int(input("Make a Guess: "))
            if user_choice == number:
                print("You won!")
                hard_life = 0
            elif user_choice > number:
                hard_life -= 1
                if hard_life == 0:
                    print("You've ran out of Guesses. Game Over!")
                else:
                    print(f"Too high\nGuess again.\nYou have {hard_life} attempts remaining to guess the number.")
            elif user_choice < number:
                hard_life -= 1
                if hard_life == 0:
                    print("You've ran out of Guesses. Game Over!")
                else:
                    print(f"Too Low\nGuess again.\nYou have {hard_life} attempts remaining to guess the number.")
    elif user_choice == "easy":
        print("You have 10 attempts to answer")
        easy_life = 10
        while easy_life != 0:
            user_choice = int(input("Make a Guess: "))
            if user_choice == number:
                print("You won!")
                easy_life = 0
            elif user_choice > number:
                easy_life -= 1
                if easy_life == 0:
                    print("You've ran out off Guesses. Game Over!")
                else:
                    print(f"Too high\nGuess again.\nYou have {easy_life} attempts remaining to guess the number.")
            elif user_choice < number:
                easy_life -= 1
                if easy_life == 0:
                    print("You've ran out off Guesses. Game Over!")
                else:
                    print(f"Too Low\nGuess again.\nYou have {easy_life} attempts remaining to guess the number.")
    else:
        print("You have entered wrong input. Try again")


hard_select()