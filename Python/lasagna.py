# Guido's Gorgeous Lasagna


EXPECTED_BAKE_TIME = 40

PREPARATION_TIME = 2


def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int baking time already elapsed.
    :return int remaining bake time derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time


def preparation_time_in_minutes(number_of_layers):
    """Takes the number of layers you want to add to the lasagna.
    Returns how many minutes you would spend making them

     :param number_of_layers: int take the number of layers
     :return int preparation time based on 'PREPARATION_TIME'
     """
    return PREPARATION_TIME * number_of_layers


def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """This function should return the total number of minutes you've been cooking,
     or the sum of your preparation time and the time the lasagna has already spent baking in the oven.

     :param number_of_layers: int take the number of layers
     :param elapsed_bake_time: int elapsed_bake_time: int baking time already elapsed.
     :return int the sum of your preparation time and the time the lasagna has already spent baking in the oven.
     """
    total_time = preparation_time_in_minutes(number_of_layers) + bake_time_remaining(elapsed_bake_time)
    return total_time


if __name__ == "__main__":
    print("The total time needed to prepare lasagna will be " + str(elapsed_time_in_minutes(2, 6)))
