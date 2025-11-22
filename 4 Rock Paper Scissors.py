import random

rock = "💎"
paper = "📰"
scissors = "✂"

game_images = [rock, paper, scissors]

user = int(input("""What do you choose?
Type 0 for Rock, 1 for Paper or 2
for Scissors."""))

#print user image
if user >= 0 and user <= 2:
    print(game_images[user])

#Create random value and print computer image
computer = random.randint(0, 2)
print(game_images[computer])

#Compare user choise to computer choice
if user >= 3 or user < 0:
    print("""You did not select a valid option.
Game over""")
elif user == 0 and computer == 2:
    print("You win!")
elif user == 2 and computer == 0:
    print("You lose!")
elif user < computer:
    print("You lose!")
elif user > computer:
    print("You win!")
elif user == computer:
    print("It's a draw")
