import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


game_image = [rock, paper, scissors]

user_choice  = int(input("Do you want choose? Type 0 for Rock, 1 for Paper, 2 for Scissors \n"))
if user_choice >= 0 and user_choice <= 2:
    print(game_image[user_choice])

computer_choice =  random.randint(0, 2)
print(f"Computer choice: ")
print(game_image[computer_choice])

if user_choice >= 3 and user_choice < 0:
    print("You type invalid number. You lose.!")
elif user_choice == 0 and computer_choice == 2:
    print("You Win.!")
elif computer_choice == 0 and  user_choice == 2:
    print("You lose.!")
elif user_choice < computer_choice:
    print("You win.!")
elif computer_choice < user_choice:
    print("You lose.!")
elif user_choice == computer_choice:
    print("Match is draw")