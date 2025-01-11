"""
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
"""
import random

while True:
	choices = input("please roll the dice by choosing a 'y' or 'n': ").lower()
	
	if choices == 'y':
		roll1 = random.randint(1,6)
		roll2 = random.randint(1,6)
		print(f'{roll1},{roll2}')
	elif choices == 'n':
		print('Thank you for playing our rolling dice game!')
		break
	else:
		print("Invalid input choice, please choose a 'y' or 'n'")
		
        