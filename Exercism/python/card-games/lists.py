"""Functions for tracking poker hands and assorted card tasks.

Python list documentation: https://docs.python.org/3/tutorial/datastructures.html
"""


def get_rounds(number):
    """Create a list containing the current and next two round numbers.

    Parameters:
        number (int): The current round number.

    Returns:
        list: The current round number and the two that follow.
    """

    list_of_rounds = [number, number + 1, number + 2]


    return list_of_rounds


def concatenate_rounds(rounds_1, rounds_2):
    """Concatenate two lists of round numbers.

    Parameters:
        rounds_1 (list): The first rounds played.
        rounds_2 (list): The second group of rounds played.

    Returns:
        list:  All rounds played.
    """

    concatenate_lists = rounds_1 + rounds_2

    return concatenate_lists


def list_contains_round(rounds, number):
    """Check if the list of rounds contains the specified number.

    Parameters:
        rounds (list): The rounds played.
        number (int): The round number.

    Returns:
        bool: Was the round played?
    """

    contains_round = False

    for round in rounds:
        if round == number:
            contains_round = True

    return contains_round


def card_average(hand):
    """Calculate and returns the average card value from the list.

    Parameters:
        hand (list): The cards in the hand.

    Returns:
        float: The average value of the cards in the hand.
    """

    average = sum(hand)/len(hand)

    return average


def approx_average_is_average(hand):
    """Return if the (average of first and last card values) OR ('middle' card) == calculated average.

    Parameters:
        hand (list): The cards in the hand.

    Returns:
        bool: Does one of the approximate averages equal the `true average`?
    """

    actual_average = sum(hand)/len(hand)

    average_first_last = ((hand[0] + hand[len(hand) - 1])/2)

    list_middle = len(hand) // 2

    middle_card = hand[list_middle]

    if average_first_last == actual_average or middle_card == actual_average:
        is_approximate_averages_equal = True
    else:
        is_approximate_averages_equal = False

    return is_approximate_averages_equal


def average_even_is_average_odd(hand):
    """Return if the (average of even indexed card values) == (average of odd indexed card values).

    Parameters:
        hand (list): The cards in the hand.

    Returns:
        bool: Are the even and odd averages equal?
    """

    is_avarage_even_equal_avarage_odd = False
    even_index_cards = []
    odd_index_cards = []    
    i = 0

    for item in hand:

        i += 1
        if i % 2 == 0:
            even_index_cards.append(item)
        else:
            odd_index_cards.append(item)

    if sum(even_index_cards)/len(even_index_cards) == sum(odd_index_cards)/len(odd_index_cards):
        is_avarage_even_equal_avarage_odd = True


    return is_avarage_even_equal_avarage_odd


def maybe_double_last(hand):
    """Multiply a Jack card value in the last index position by 2.

    Parameters:
        hand (list): The cards in the hand.

    Returns:
        list: The hand with Jacks (if present) value doubled.
    """

    hold_jack = hand[len(hand) - 1]

    if hand[len(hand) - 1] == 11:
        hold_jack *= 2
        hand.pop()
        hand.append(hold_jack)


    return hand
