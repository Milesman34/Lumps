from collections import Counter
from typing import List

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

# Returns the number of points that should be gotten from a given number of dice of a specific number
# 10 points for 6 of a kind, 20 for 7 of a kind, 30 for 8 of a kind
def points_from_pair(die: int, count: int) -> int:
    return die * (count - 1) + 10 * max(0, count - 5)

# Determines if an array is either all even or all odd
def is_all_even_or_odd(ls: List[int]) -> bool:
    # This value is compared with all the other values to determine if they are all even or odd
    cmp = ls[0] % 2

    for i in range(1, len(ls)):
        test = ls[i] % 2

        if test != cmp:
            return False

    return True

# Gets the score of a game of lumps
# For each pair, you get points equal to the number in the pair
# If there are 3 or more of a kind, your points is equal to the number * (number in group - 1)
# 6 points for all evens or all odds
# 10 points for run of 6, 20 for run of 7, 30 for run of 8
# 10 points for 6 of a kind, 20 points for 7 of a kind, 30 points for 8 of a kind
def calculate_lumps_score(dice: List["Dice"]) -> int:
    dice = [i.value for i in dice]

    # Gets a sorted list of unique dice to help find runs
    unique_dice = list(set(sorted(dice)))

    # Creates a counter of all the dice
    counter = Counter(dice)

    # Start by getting the sum of the points for pairs
    answer = sum([points_from_pair(die, count) for die, count in counter.items()])

    # Now, iterate over the list of unique dice
    current_run = 1

    for i in range(len(unique_dice) - 1):
        if unique_dice[i] + 1 == unique_dice[i + 1]:
            current_run += 1
        else:
            # In this case, the run stopped short of the end, so check if it was long enough
            if current_run == 6:
                answer += 10
            elif current_run == 7:
                answer += 20

            current_run = 1

    # Check if there is an active run which is long enough
    if current_run > 5:
        answer += 10 * (current_run - 5)

    # Checks if all the values are even or odd
    if is_all_even_or_odd(unique_dice):
        answer += 6

    return answer

# Determines if a string can be converted to an int
def str_is_int(string: str) -> bool:
    return len([ch for ch in string if ch in "-0123456789"]) == len(string)

# Formats the string for the current rolls left
def format_rolls_left(rolls: int) -> str:
    if rolls == 0:
        return "No rolls left"
    elif rolls == 1:
        return "1 roll left"
    else:
        return f"{rolls} rolls left"

# Creates a generic push button
def create_push_button(parent, text: str, size: int=12) -> QPushButton:
    button = QPushButton(parent)
    button.setText(text)
    button.setFont(QFont("Arial", size))

    return button

# Adds a spacer to a layout
def add_spacer(layout, stretch: int=1):
    layout.addWidget(QFrame(), stretch=stretch)