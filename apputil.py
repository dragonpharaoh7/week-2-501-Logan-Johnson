import numpy as np

# update/add code below ...


def ways(cents, coin_types=[1, 5]):
    """
    Returns the number of ways to make change for a given amount of
    cents using specified coin types.

    Parameters:
    cents (int): The amount of cents to make change for.
    coin_types (list): A list of coin denominations to use for making
        change. Default is [1, 5].

    Returns:
    int: The number of ways to make change for the given amount of
        cents using the specified coin types.
    """
    # Initialize a list to store the number of ways to make change for
    # each amount from 0 up to 'cents'. There is exactly 1 way to make
    # 0 cents (use no coins at all), so we start there.
    ways_to_make_change = [1] + [0] * cents

    # Go through one coin type at a time (instead of one amount at a
    # time). Handling a whole coin type before moving to the next is
    # what keeps us from counting the same combination twice in a
    # different order.
    for coin in coin_types:
        # For every amount that this coin can actually be used toward...
        for amount in range(coin, cents + 1):
            # ...add in the ways to make the remainder after using one
            # of this coin. This accumulates onto
            # ways_to_make_change[amount - coin], which was already
            # updated earlier in this same loop, so it naturally
            # accounts for using the coin more than once.
            ways_to_make_change[amount] += ways_to_make_change[amount - coin]

    return ways_to_make_change[cents]


def lowest_score(names, scores):
    """
    Returns the name of the student with the lowest score.

    Parameters:
    names (numpy.ndarray): An array of student names.
    scores (numpy.ndarray): An array of student scores.

    Returns:
    str: The name of the student with the lowest score.
    """
    # Combine the names and scores into a dictionary.
    student_scores = dict(zip(names, scores))

    return min(student_scores, key=student_scores.get)


def sort_names(names, scores):
    """
    Returns student names sorted by score, from highest to lowest.

    Parameters:
    names (numpy.ndarray): An array of student names.
    scores (numpy.ndarray): An array of student scores.

    Returns:
    list: The names in descending order of score.
    """
    # Sort the score indices ascending, then reverse for descending
    # order. Sorting by position (instead of building a name-keyed
    # dict) also means students who tie on score never overwrite one
    # another.
    order = np.argsort(scores)[::-1]

    return list(names[order])
