from random import randint


def guessing_game():
    num = randint(1, 100)
    attempts = 0
    max_attempts = 7
    
    while attempts < max_attempts:
        guess = int(input("Guess a number between 1 and 100: "))

        if guess < num:
            print("Too low!")
        elif guess > num:
            print("Too high!")
        else:
            print(f"Congratulations! You guessed the number in {attempts + 1} attempt(s).")
            return

        attempts += 1

    print(f"Sorry, you've used all your attempts. The number was {num}.")

if __name__ == "__main__":
    guessing_game()