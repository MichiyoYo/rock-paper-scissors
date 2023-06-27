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

#Write your code below this line 👇

import random

weapons = [rock, paper, scissors]
scores = [[-1,1,0], [1,-1,2], [0,2,-1]]
quit = False

print("Welcome to Rock, Paper, Scissors! 🪨 📄 ✂️")
while quit == False:
  player = int(input("\nWhat's your choice?\n(0) Rock 🪨\n(1) Paper 📄\n(2) Scissors ✂️\n"))
  cpu = random.randint(0,2)
  
  print(f"\nYou chose:\n{weapons[player]}")
  print(f"CPU chose:\n{weapons[cpu]}")
  
  result = scores[player][cpu]
  
  if result < 0:
    print('Tie, no one wins...\n')
  else:
    print(f"{'You' if player == result else 'CPU'} win{'s' if cpu == result else ''}!\n")

  retry = input('Do you want to go again? (y/n): ')
  if retry == 'n':
    quit = True
    
print("Bye!")
