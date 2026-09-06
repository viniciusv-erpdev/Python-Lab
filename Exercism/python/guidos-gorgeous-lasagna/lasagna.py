"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""


EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2

#TODO (student): Remove 'pass' and complete the 'bake_time_remaining()' function below.
def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    Parameters:
        elapsed_bake_time (int): The baking time already elapsed.

    Returns:
        int: The remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """

    return EXPECTED_BAKE_TIME - elapsed_bake_time


def preparation_time_in_minutes(number_of_layers):
    """Calculate the time to add each new lasagna layer.

    Parameters:
        number_of_layers (int): the number of layers the lasagna will have.

    returns:
        int: the total time for adding the number of layers

    Function that takes the amount of layers added to the lasagna as an argument and returns 
    how much total time it takes to make all the layers.
    
    """


    return number_of_layers * PREPARATION_TIME


#TODO (student): define the 'elapsed_time_in_minutes()' function below.
def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the elapsed time since the start of the lasagna preparation.

    Parameters:
        number_of_layers (int): the amount of layers the lasagna have
        elapsed_bake_time (int): the time alredy speended into the preparation
        of the lasanga

    returns:
        int: the total amount of time spend into cooking the lasagna

    Function that takes the amount of layers and the total baking time of the lasagna
    and returns the amount of time alredy spent in cooking the lasagna 
    """


    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time

