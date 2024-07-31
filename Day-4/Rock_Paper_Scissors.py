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
---'    ____)____
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
options = [rock, paper, scissors]

ans = ""
while ans != "no":

    print("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.")
    person = int(input())

    computer = random.randint(0, 2)

    # BRUTE - MY SOLVE
    # if person == computer:
    #     print(f"You choose:\n{options[person]}\nComputer choose:\n{options[computer]}\n\nMATCH TIE.")
    # else:
    #     if person == 0 and computer == 1:
    #         print(f"You choose:\n{options[person]}\nComputer choose:\n{options[computer]}\n\nYOU LOSE.")
    #     elif person == 0 and computer == 2:
    #         print(f"You choose:\n{options[person]}\nComputer choose:\n{options[computer]}\n\nYOU WIN.")
    #     elif person == 1 and computer == 0:
    #         print(f"You choose:\n{options[person]}\nComputer choose:\n{options[computer]}\n\nYOU WIN.")
    #     elif person == 1 and computer == 2:
    #         print(f"You choose:\n{options[person]}\nComputer choose:\n{options[computer]}\n\nYOU LOSE.")
    #     elif person == 2 and computer == 0:
    #         print(f"You choose:\n{options[person]}\nComputer choose:\n{options[computer]}\n\nYOU LOSE.")
    #     elif person == 2 and computer == 1:
    #         print(f"You choose:\n{options[person]}\nComputer choose:\n{options[computer]}\n\nYOU WIN.")

    # EFFICIENT
    if person >= 3 or person < 0:
        print("You typed an invalid, try again")
    elif person == 0 and computer == 2:
        print(f"You choose:\n{options[person]}\nComputer choose:\n{options[computer]}\n\nYOU WIN.")
    elif computer == 0 and person == 2:
        print(f"You choose:\n{options[person]}\nComputer choose:\n{options[computer]}\n\nYOU LOSE.")
    elif computer > person:
        print(f"You choose:\n{options[person]}\nComputer choose:\n{options[computer]}\n\nYOU LOSE.")
    elif person > computer:
        print(f"You choose:\n{options[person]}\nComputer choose:\n{options[computer]}\n\nYOU WIN.")
    elif computer == person:
        print(f"You choose:\n{options[person]}\nComputer choose:\n{options[computer]}\n\nMATCH TIE.")

    print("Play again? no for quit. anything else for keep playing.")
    ans = input("Answer- ")

print("Thank you for playing!")
