import random

"""
rock gets beaten by paper
paper gets beaten by scissors and
rock beats scissors
"""

xyz = ["Rock", "Paper", "Scissors"]

x = "rock"
y = "paper"
z = "scissors"

print("What is you're name? ")
w = input()
print("hi " + w)

print("What do you pick?\nRock\nPaper\nScissors: ")
a = input()

if a == "rock":
    print("You picked rock")
    
if a == "paper":
    print("You picked paper")
    
    
if a == "scissors":
    print("You picked scissors")
    
b = random.choice(xyz)
print("you opponent picked " + b)

if b == "Rock" and a == "paper":
    print("YOU WIN!")
   

if b == "Scissors" and a == "paper":
    print("YOU LOSE!")

if b == "Rock" and a == "scissors":
    print("YOU LOSE!")

if b == "Paper" and a == "rock":
    print("YOU LOSE!")
   

if b == "Paper" and a == "scissors":
    print("YOU WIN!")
    

if b == "Scissors" and a == "rock":
    print("YOU WIN!")

if b == "Rock" and a == "rock":
    print("It's a draw....")


if b == "Paper" and a == "paper":
    print("It's a draw....")


if b == "Scissors" and a == "scissors":
    print("It's a draw....")

