
import random
import os

# ---------- COLORS ----------
RESET = "\033[0m"
BOLD = "\033[1m"
CYAN = "\033[96m"
GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
PURPLE = "\033[95m"
BLUE = "\033[94m"

# ---------- GAME SETTINGS ----------
choices = ["rock", "paper", "scissors"]

emojis = {
    "rock": "🪨",
    "paper": "📄",
    "scissors": "✂️"
}

player_score = 0
computer_score = 0
draws = 0
round_number = 0


# ---------- CLEAR SCREEN ----------
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


# ---------- HEADER ----------
def show_header():
    print(CYAN + BOLD + "=" * 44)
    print("       ROCK  PAPER  SCISSORS")
    print("          GDG GAME ZONE")
    print("=" * 44 + RESET)


# ---------- SCOREBOARD ----------
def show_score():
    print(BLUE + "\n              SCOREBOARD")
    print("-" * 44 + RESET)
    print(f"  {GREEN}YOU       : {player_score}{RESET}")
    print(f"  {RED}COMPUTER   : {computer_score}{RESET}")
    print(f"  {YELLOW}DRAWS      : {draws}{RESET}")
    print("-" * 44)


# ---------- PLAY GAME ----------
while True:
    clear_screen()
    show_header()
    show_score()

    print(PURPLE + f"\n  ROUND {round_number + 1}" + RESET)
    print("\n  1. 🪨  Rock")
    print("  2. 📄  Paper")
    print("  3. ✂️  Scissors")
    print("  4. Exit")

    user_input = input(
        YELLOW + "\n  Enter your choice (1-4): " + RESET
    ).strip()

    if user_input == "4":
        break

    if user_input not in ["1", "2", "3"]:
        print(RED + "\n  Invalid choice! Try again." + RESET)
        input("\n  Press Enter to continue...")
        continue

    player = choices[int(user_input) - 1]
    computer = random.choice(choices)

    round_number += 1

    print("\n" + CYAN + "=" * 44 + RESET)
    print(f"\n  YOU      : {emojis[player]} {player.upper()}")
    print(f"  COMPUTER : {emojis[computer]} {computer.upper()}")

    if player == computer:
        print(YELLOW + BOLD + "\n  RESULT: IT'S A DRAW!" + RESET)
        draws += 1

    elif (
        (player == "rock" and computer == "scissors")
        or (player == "paper" and computer == "rock")
        or (player == "scissors" and computer == "paper")
    ):
        print(GREEN + BOLD + "\n  RESULT: YOU WIN!" + RESET)
        player_score += 1

    else:
        print(RED + BOLD + "\n  RESULT: COMPUTER WINS!" + RESET)
        computer_score += 1

    print(CYAN + "\n" + "=" * 44 + RESET)
    input("\n  Press Enter for the next round...")


# ---------- FINAL RESULTS ----------
clear_screen()
show_header()
show_score()

print(PURPLE + BOLD + "\n             GAME OVER" + RESET)

if player_score > computer_score:
    print(GREEN + "\n  CHAMPION: YOU! WELL PLAYED!" + RESET)
elif computer_score > player_score:
    print(RED + "\n  COMPUTER WINS THIS MATCH!" + RESET)
else:
    print(YELLOW + "\n  THE MATCH ENDS IN A DRAW!" + RESET)

print(CYAN + "\n  Thanks for playing!")
print("  Built with Python | GDG Project")
print("=" * 44 + RESET)
