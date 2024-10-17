import random

options = ("rock","paper","scissor")

attempt = True
while attempt:
    user = None
    computer = random.choice(options)

    while user not in options:
        user = input("Enter a choice (rock,paper,scissor): ")

    print(f"user : {user}")
    print(f"computer: {computer}")

    if user == computer :
        print("It's a tie!")
    elif user == 'rock' and computer == 'scissor':
        print("You win!")
    elif user == 'scissor' and computer == 'paper':
        print("You win!")
    elif user == 'paper' and computer == 'rock':
        print("You win!")
    else:
        print("You lose!")

    print("Want to play again?")
    attempt = input("yes/no: ").lower() == 'yes'

