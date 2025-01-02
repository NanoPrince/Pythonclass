#  Rock paper Scissors
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


