import logging

from random import randint
from typing import List

logging.basicConfig(level=logging.INFO, format='%(asctime)s -- %(levelname)s -- %(message)s')


def play(zombies: List, plants: List, ) -> bool:

    """
    The play function takes two lists of integers as arguments.
    The first list represents the strength of each plant, and the second list represents the strength of each zombie.
    Each element in a list is an integer representing that creature's power level.
    If a plant has more power than a zombie, it will destroy that zombie (and vice versa).
    If they are equal in power, both creatures will be destroyed.
    The function should return True if all zombies are destroyed and False otherwise.

    :param zombies: List: Pass in a list of zombie strength values
    :param plants: List: Pass the list of plants to the function
    :param : Pass the list of plants and zombies to the function
    :return: A boolean value
    :doc-author: Trelent
    """
    try:
        if plants and zombies:
            diff = abs(len(plants) - len(zombies))
            if len(plants) < len(zombies):
                plants += [0] * diff
            elif len(zombies) < len(plants):
                zombies += [0] * diff

            survived_plants = sum(1 for p, z in zip(plants, zombies) if p > z)
            survived_zombies = sum(1 for p, z in zip(plants, zombies) if z > p)

            strength_plants = sum(plants)
            strength_zombies = sum(zombies)

            if survived_plants > survived_zombies:
                return True
            elif survived_plants < survived_zombies:
                return False
            else:
                if strength_plants > strength_zombies:
                    return True
                elif strength_plants < strength_zombies:
                    return False
                else:
                    return True

            # print(survived_zombies, survived_plants, strength_zombies, strength_plants)
        elif None in zombies or None in plants:
            raise TypeError(f"argument of type 'NoneType' is not iterable")

    except Exception as exp:
        logging.error(f"play(plants:{plants}, zombies:{zombies}) --> {exp.__class__.__qualname__}: {exp}!")


if __name__ == '__main__':

    plants = []
    zombies = []
    count = 1
    num_plants = randint(1, 10)
    num_zombies = randint(1, 10)
    for zombie_soldier in range(num_zombies + 1):
        new_zombie = randint(1, 10)
        zombies.append(new_zombie)
    while count < num_plants + 1:
        try:
            user_input = input(f"Please enter strength of Plant's soldier ({count} of {num_plants}): ")
            plants.append(float(user_input))
            count += 1
        except Exception as exp:
            print(f'User input: "{user_input}" --> {exp.__class__.__qualname__}: {exp}!')
            continue
    result = play(zombies=zombies, plants=plants)
    print(result)
