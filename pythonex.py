# Ask the user for their name
name = input("Enter your name: ")

# Greet the user
print(f"Hello, {name}! Let's play a quick number game.")

# Ask the user for a number and convert it to an integer
number_input = input("Enter your favorite integer: ")
number = int(number_input)

# Check if the number is even or odd
if number % 2 == 0:
    print(f"The number {number} is Even!")
else:
    print(f"The number {number} is Odd!")