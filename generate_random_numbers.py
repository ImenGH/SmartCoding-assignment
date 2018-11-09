"""
This module contains the following functions to process a list of random
numbers.
"""
from random import randint


# Defining  integer range of the possible choices the random numbers from
# 1 to 99.
INTEGER_CHOICES_START = 1
INTEGER_CHOICES_END = 99


def get_random_numbers():
    '''
    Generate a list of 100 random numbers.

    Returns:
        random_numbers (list): A list of random numbers.
    '''
    random_numbers = []
    # Picking 20 random integers.
    for count in range(20):
        # Getting a random number.
        number = randint(INTEGER_CHOICES_START, INTEGER_CHOICES_END)
        # Adding the generated number to the random_numbers list.
        random_numbers.append(number)

    return random_numbers

# Making sure that we got 20 integers from the get_random_numbers function.
assert len(get_random_numbers()) == 20


def main():
    random_numbers = get_random_numbers()
    print(random_numbers)


main()
