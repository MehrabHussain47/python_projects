# Now CPU uses many choices for whole program 
import random

choices = ["Rock", "Paper", "Scissors"] 
player = False
cpu_score = 0
player_score = 0

while True:
    computer = random.choice(choices)
    player = input("Rock, Paper or Scissors ? ").capitalize()

    # Conditions of the game
    if player == computer:
        print("Tie")
    elif player == "Rock":
        if computer == "Paper":
            print("You lose!", computer, "covers", player)
            cpu_score += 1
        else:
            print("You win!", player, "smashes", computer)
            player_score += 1
    elif player == "Paper":
        if computer == "Scissors":
            print("You lose!", computer, "cuts", player)
            cpu_score += 1
        else:
            print("You win!", player, "covers", computer)
            player_score += 1
    elif player == "Scissors":
        if computer == "Rock":
            print("You lose!", computer, "smashes", player)
            cpu_score += 1
        else:
            print("You win!", player, "cuts", computer)
            player_score += 1

# rock and paper => paper
# rock and scissors => rock
# paper and scissors => scissors
# otherwise tie

    elif player == "End":
        print("\nFinal Score:")
        print(f"CPU: {cpu_score}")
        print(f"Player: {player_score}")
        if cpu_score > player_score:
            print("CPU wins the match.")
        elif cpu_score < player_score:
            print("You wins the match.")
        else:
            print("Match tied.")
        break
