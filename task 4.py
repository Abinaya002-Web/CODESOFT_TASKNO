import random
choices = ["rock","paper","scissors"]
user = input("enter rock,paper,or scissors:").lower()
computer = random.choice(choices)
print("computer:",computer)
if user == computer:
    print("Its tie!")
elif(user == "rock" and computer == "scissors") or  (user == "paper" and computer == "rock") or  (user == "scissors" and computer =="paper"):
    print("you win")
else:
    print("computer wins")
