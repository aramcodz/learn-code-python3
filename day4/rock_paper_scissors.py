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

game_images = [rock, paper, scissors]
computer_throw_index = random.randint(0,2)

user_input = input("Rock, Paper, Scissors Game: What do you choose? "
                   "Choose 0 for Rock, 1 for Paper, 2 for Scissors: \n")
user_throw_index = int(user_input)
if user_throw_index >= 0 and user_throw_index <= 2:
    print(f"You Chose: \n", game_images[user_throw_index])
    print("Computer Chose: \n", game_images[computer_throw_index])

if user_throw_index > 3 or computer_throw_index < 0:
    print("You entered an invalid number, You Lose!")
elif user_throw_index == computer_throw_index:
    print("It's a draw!")
elif ((user_throw_index == 0 and computer_throw_index == 2)
        or (user_throw_index == 2 and computer_throw_index == 1)
        or (user_throw_index == 1 and computer_throw_index == 0)):
    print("You Win!")
else:
    print("Computer wins, You Lose!")
