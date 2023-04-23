EXPECTED_BAKE_TIME = 40


def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """

    return EXPECTED_BAKE_TIME - elapsed_bake_time


def preparation_time_in_minutes(number_of_layers):
    """
    The preparation_time_in_minutes function takes the number of layers as an argument and returns the preparation
    time in minutes.

    :param number_of_layers: Determine the number of layers
    :return: The number of minutes it takes to prepare a cake with the given number of layers
    """
    return number_of_layers * 2


def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """
    The elapsed_time_in_minutes function takes two arguments:
    1. number_of_layers (int) - the number of layers
    2. elapsed_bake_time (int) - how long the lasagna has been baking

    :param number_of_layers: Determine the number of layers in the lasagna
    :param elapsed_bake_time: The number of minutes the lasagna has been baking in the oven
    :return: The sum of the preparation_time_in_minutes function and the elapsed bake time
    """

    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time
