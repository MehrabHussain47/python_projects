import random

choices = ["Rock", "Paper", "Scissors"] # 3 choices nilam 
computer = random.choice(choices)   # Choices theke randomly choose korba
player = False  # player loop er jonno nilam
cpu_score = 0   # Initially cpu and player er score zero
player_score = 0

while True:
    player = input("Rock, Paper or Scissors ? ").capitalize()