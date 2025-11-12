# I acknowledge the use of ChatGPT (GPT-5, OpenAI, https://chat.openai.com)
# to review and improve my draft code.

import random

def guess_the_number():
    """A simple text-based 'Guess the Number' game."""
    
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    attempts = 0
    
    print("Welcome to Guess the Number!")
    print("I'm thinking of a number between 1 and 100.")
    
    while True:
        try:
            # Get the player's guess
            guess = int(input("Enter your guess: "))
            attempts += 1
            
            # Check the guess
            if guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the number {secret_number} in {attempts} attempts.")
                break
        except ValueError:
            print("Invalid input. Please enter a whole number.")

if __name__ == "__main__":
    guess_the_number()
