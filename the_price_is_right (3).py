import random

def display_welcome_message():
    print("Welcome to The Price Is Right!")
    print("Guess the price of the item. You have 5 attempts.")
    print("The price is between $1 and $100.")

def get_player_guess():
    while True:
        try:
            guess = int(input("Enter your guess: $"))
            if 1 <= guess <= 100:
                return guess
            else:
                print("Please enter a number between 1 and 100.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def main():
    actual_price = random.randint(1, 100)
    attempts = 10

    display_welcome_message()

    for attempt in range(attempts):
        guess = get_player_guess()

        if guess < actual_price:
            print("Too low!")
        elif guess > actual_price:
            print("Too high!")
        else:
            print("Congratulations! You've guessed the correct price! You Win!")
            break
    else:
        print(f"Sorry, you've used all your attempts. The correct price was ${actual_price}. Try Again!")

if __name__ == "__main__":
    main()
