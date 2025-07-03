import random

print("🎲 Welcome to the Coin Flip Guessing Game!")
print("Guess the result: Heads or Tails")

# Get user input
user_guess = input("Your guess: ").capitalize()

# Flip the coin
flip = random.choice(["Heads", "Tails"])
print(f"The coin landed on: {flip}")

# Check result
if user_guess == flip:
    print("✅ You guessed it right!")
else:
    print("❌ Oops! Better luck next time.")
