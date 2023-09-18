# Rock, Paper, Scissor game
# using random library

import random


def play():
    user = input("Pick: 'R'(rock), 'P'(paper), 'S'(scissor): ")
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return 'It\'s a tie\n' + 'Computer\'s pick: ' + computer

    if winner(user, computer):
        return 'You won!\n' + 'Computer\'s pick: ' + computer

    return 'You lost!\n' + 'Computer\'s pick: ' + computer


def winner(user, computer):
    if (user == 'r' and computer == 's') or (user == 's' and computer == 'p') \
            or (user == 'p' and computer == 'r'):
        return True


print(play())

""" I find that the input is case sensitive.
Logic error occurs when you type in capital letters wherein
computer's selection is small letters. There is a tendency 
computer still wins.
"""
