import random
# rules Rock > Scissors  ||  Scissors > Paper ||  Paper > Rock
def play():
    user = input("What is your choice?--> for rock ('R'), for paper ('P), for scissors ('S)\n").lower()
    computer = random.choice(['r', 'p', 's'])
    if user == computer:
        return 'tie=none of us win!!!'
    if is_win(user, computer):
        return 'You won comp!'
    return 'You lost, comp win!!!(('


def is_win(player, opponent):
    if (player =='r' and opponent =='s') or (player =='s' and opponent =='p')\
        or (player =='p' and opponent =='r'):
        return True
