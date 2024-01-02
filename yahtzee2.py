"""
This program lets the user play a shortened and simplified version of the game yahtzee.
This version includes the upper section and lower section of the game.
Author: Abhirami Binesh
When: November 3, 2023
"""
from random import randint
from collections import Counter

def make_roll() -> tuple:
    """
    Returns a tuple of five random values between 1 and 6.
    """
    roll = (randint(1,6),randint(1,6),randint(1,6),randint(1,6),randint(1,6))
    return roll


def sum_of_given_number(roll: tuple, number: int) -> int:
    """
    Returns the sum of the values in the roll that match the given number.
    Example: sum_of_given_number((2,6,2,6,1), 6) = 12
    """
    Total = 0
    for num in roll:
        if num == number:
            Total = Total + num
    return Total


def fill_upper_section(roll: tuple) -> list:
    """
    Returns a list of the sums of all values in the roll.
    """
    upper_section_scores = []
    for num in range(1,7):
        Total = sum_of_given_number(roll, num)
        upper_section_scores.append(Total)
    return upper_section_scores


def display_upper_section(C: list) -> None:
    """
    Displays the upper section.
    """
    names = ['Aces', 'Twos', 'Threes', 'Fours', 'Fives', 'Sixes']
    for i in range(len(names)):
        print(f"{names[i]}: {C[i]}")

def num_of_a_kind(roll: tuple, number: int) -> int:
    """
    If a roll has EXACTLY `number` dice of the same face value,
    returns the sum of all five values in the roll.
    Otherwise, returns 0.
    """
    Total = 0
    c=Counter(roll)  # counts the frequency of elements in roll
    counts = set(c.values())  # makes a set with frequency values
    # iterate over the set to check whether frequency is equal to number
    for i in counts:
        if i == number:
            # iterates over roll to add all values in the tuple
            for num in roll:
                Total += num
    return Total
    
        

def yahtzee(roll: tuple) -> int:
    """
    Returns 50 if the roll is a Yahtzee (all dice in the roll have the same
    face value). Otherwise, returns 0.
    """
    Total = 0
    c=Counter(roll)  # counts the frequency of elements in roll
    counts = set(c.values())  # makes a set with frequency values
    # iterate over the set and returns 50 points if frequency is 5
    for i in counts:
        if i == 5:
            Total += 50
    return Total    

def main():
    """
    Main function.
    """
    roll = make_roll()
    print(f"Rolling the dice... {roll}")
    score_list = fill_upper_section(roll)
    print("Upper section: ")
    display_upper_section(score_list)
    print("Lower section: ")
    print(f"Three of a kind: {num_of_a_kind(roll, 3)}")
    print(f"Four of a kind: {num_of_a_kind(roll, 4)}")
    print(f"Yahtzee: {yahtzee(roll)}")
    
if __name__ == "__main__":
    main()