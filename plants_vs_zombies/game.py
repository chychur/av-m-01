import logging
from pprint import pprint
from typing import List
from xmlrpc.client import boolean

logging.basicConfig(level=logging.INFO, format='%(asctime)s -- %(levelname)s -- %(message)s')


def play(zombies: List, plants: List, ) -> boolean:
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

    while True:
        user_input = input('Please enter plants (1-9): ')
    play()
