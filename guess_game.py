# I acknowledge the use of ChatGPT (GPT-5, OpenAI, https://chat.openai.com)
# to review and improve my draft code.

import random
def select_difficulty():
    """Allows the user to select a difficulty level."""
    while True:
        print("\nSelect Difficulty:")
        print("1: Easy (1-50)")
        print("2: Medium (1-100)")
        print("3: Hard (1-200)")
        choice = input("Enter choice (1, 2, or 3): ")
        
        if choice == '1':
            return 50
        elif choice == '2':
            return 100
        elif choice == '3':
            return 200
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")
def guess_the_number(max_range):
    """A simple text-based 'Guess the Number' game."""
    
    # Generate a random number
    secret_number = random.randint(1, max_range)

    attempts = 0
    
    print("Welcome to Guess the Number!")
    print(f"I'm thinking of a number between 1 and {max_range}.")
    
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
    guess_the_number(select_difficulty())
