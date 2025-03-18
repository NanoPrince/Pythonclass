import random

while True:
    choice = input('Roll the Dice now by choosing (y or n): ').lower()

    if choice == 'y':
        dice1 =random.randint(1,6)
        dice2 =random.randint(1,6)
        print('f({dice1},{dice2})')
    elif choice == 'n':
        print('Thank you for playing our rolloing dice game!')
        break
    else:
        print("Invalid input choice, please choose a 'yes' or 'no'")

'''
import random 

while True:
  choice = input('Roll the dice? (y/n): ').lower()
  if choice == 'y':
      die1 = random.randint(1, 6)
      die2 = random.randint(1, 6)
      print(f'({die1}, {die2})')
  elif choice == 'n':
      print('Thanks for playing!')
      break
  else:
      print('Invalid choice!')'
'''