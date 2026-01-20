import random

secret = random.randint(1, 10)
guess = int(input("Guess a number (1-10): "))

if guess == secret:
    print("Correct! You guessed the number!")
else:
    print(f"Wrong! The number was {secret}")
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Sum =", a + b)
print("Sub =", a - b)
print("Mul =", a * b)

if b != 0:
    print("Div =", a / b)
else:
    print("Cannot divide by zero")
