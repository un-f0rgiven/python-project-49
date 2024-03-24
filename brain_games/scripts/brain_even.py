#!/usr/bin/env python3

import sys
sys.path.insert(0, '/home/alexander/python-project-49')

import random

from brain_games.engine import tell_rules
from brain_games.engine import check_answer
from brain_games.games.game_brain_even import brain_even

print("Welcome to the Brain Games!")
player = input('May I have your name? ')
print(f'Hello, {player}!')

game = 'brain_even'

tell_rules(game)

i = 1
while i < 4:

    a = random.randint(0, 100)

    question = a

    correct_answer = brain_even(a)

    print(f'Question: {question}')

    answer = input('Your answer: ')

    check_answer(answer, correct_answer, player)
    i = i + 1
else:
    print(f'Congratulations, {player}!')
