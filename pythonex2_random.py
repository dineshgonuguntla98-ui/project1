import random

# Generate a random target between 1 and 20
secret_number = random.randint(1, 20)
print("I am thinking of a number between 1 and 20.")

while True:
    guess = int(input("Take a guess: "))
    
    if guess < secret_number:
        print("Your guess is too low.")
    elif guess > secret_number:
        print("Your guess is too high.")
    else:
        print("Good job! You guessed my number!")
        break
