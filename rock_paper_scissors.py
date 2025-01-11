#  Rock paper Scissors
# Ask the user to make a choice
#if the choice is not valid
    #print an error
#Let the computer to make a choice
#print choices (emojis)
#detrmine the winner
#Ask the user if they want to continue
#if not
    #Terminate
import random
choice_dic = {'r':'Rock','p':'Paper','s':'Scissors'}
choices = ('r''p''s')

while True:
    user_choice = input('Rock, Paper or Scissors? (r/p/s): ').lower()
    # user coice validation
    if user_choice not in choices:
        print('please choose a valid option')
        continue
    comp_choice = random.choice(choices)

    print(f'computer chose {choice_dic[comp_choice]}' )
    print(f'You chose {choice_dic[user_choice]}' )
    #inorder to map the if statements to each of these choices. 
    # In python we can deploy the dictionary instead of 3 lines of the IF statements

    if user_choice == comp_choice:
        print('you have a tie break')
    elif (
    (user_choice =='r' and comp_choice == 's') or 
    (user_choice == 's' and comp_choice == 'p') or 
    (user_choice == 'p' and comp_choice == 'r')):
        print('You Win!')
    else:
        print('You Lose!')

    should_continue = input('Do you want to continue (y/n): ').lower()
    if should_continue  == 'n':
        break 
 




""" Kylie Ying Code
import random

def play():
    user = input("what is your choice: 'r' for rock, 'p' for paper, 's' for scissors: s")
    comp = random.choice(['r', 'p', 's'])
    if user == comp:
        return "it's a tie"
    #Rule of the game: r > s, s > p, p > r
    if is_win(user,comp):
        return "You won!"
    return "You lost!"
    
def is_win(player, opponent):

    #return true if playerr wins
    if (player =='r' and opponent == 's') or (player == 's' and opponent =='p') or (player == 'p' and opponent =='r'):
        return True


print(play())

"""
