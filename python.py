import time
import random

# --------------------------------------------
# Simple Text Adventure Game (100 lines approx)
# --------------------------------------------

def slow(text):
    for c in text:
        print(c, end="", flush=True)
        time.sleep(0.01)
    print()

def intro():
    slow("Welcome to the Adventure Game!")
    slow("Your goal is to survive and find the treasure.\n")
    player = {
        "name": input("Enter your character name: "),
        "health": 100,
        "coins": 0,
        "items": []
    }
    slow(f"\nGreetings, {player['name']}! Your journey begins...\n")
    return player

def choose_path():
    slow("You are at a crossroads.")
    slow("1) Go into the forest")
    slow("2) Walk towards the old village")
    slow("3) Enter the cave")
    choice = input("Choose (1/2/3): ")
    return choice

def forest(player):
    slow("\nYou enter the forest...")
    time.sleep(1)
    event = random.choice(["coins", "apple", "nothing"])
    if event == "coins":
        amount = random.randint(5, 20)
        player["coins"] += amount
        slow(f"You found {amount} coins!")
    elif event == "apple":
        slow("You found an apple and gained 10 health!")
        player["health"] = min(player["health"] + 10, 100)
    else:
        slow("Nothing interesting happened.")
    return player

def village(player):
    slow("\nYou arrive at the old village.")
    time.sleep(1)
    shop_choice = input("A merchant offers a potion for 10 coins. Buy? (y/n): ")
    if shop_choice.lower() == "y" and player["coins"] >= 10:
        player["coins"] -= 10
        player["health"] = min(player["health"] + 20, 100)
        slow("You bought the potion and restored 20 health!")
    else:
        slow("You walk away.")
    return player

def cave(player):
    slow("\nYou enter the cave...")
    time.sleep(1)
    encounter = random.choice(["treasure", "trap", "nothing"])
    if encounter == "treasure":
        slow("You found the treasure chest!!!")
        slow("Congratulations, you win!")
        player["items"].append("Treasure")
        player["win"] = True
    elif encounter == "trap":
        damage = random.randint(20, 40)
        player["health"] -= damage
        slow(f"A trap triggers! You lose {damage} health!")
        if player["health"] <= 0:
            slow("You couldn't survive the trap... Game Over.")
            player["dead"] = True
    else:
        slow("The cave is empty and quiet.")
    return player

def status(player):
    print("\n--- STATUS ---")
    print(f"Health: {player['health']}")
    print(f"Coins: {player['coins']}")
    print(f"Items: {player['items']}")
    print("--------------\n")

def game_loop():
    player = intro()
    player["win"] = False
    player["dead"] = False

    while not player["win"] and not player["dead"]:
        status(player)
        choice = choose_path()

        if choice == "1":
            player = forest(player)
        elif choice == "2":
            player = village(player)
        elif choice == "3":
            player = cave(player)
        else:
            slow("Invalid choice. Try again.")
            continue

        time.sleep(1)

        if player["health"] <= 0:
            player["dead"] = True
            slow("You ran out of health... Game Over.")

    slow("\nThanks for playing!")
    slow("Goodbye!")

# Run the game
game_loop()
num = int(input("Enter a number: "))

if num % 2 == 0:
    print(num, "is Even")
else:
    print(num, "is Odd")

if num > 0:
    print("Number is Positive")
elif num < 0:
    print("Number is Negative")
else:
    print("Number is Zero")
