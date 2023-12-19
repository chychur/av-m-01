import logging
from typing import List

logging.basicConfig(level=logging.INFO, format='%(asctime)s -- %(levelname)s -- %(message)s')


def is_pythagorean(triangle: List) -> bool:
    """
    The `is_pythagorean` function checks if the given triangle(a list of its legs' length) is a pythagorean triplet.

    :param triangle: List: Pass the list of 3 numbers that represent a triangle. Could be `int` or|and `float` types.
    :return: `True` if the given list of 3 numbers is a pythagorean triplet, `False` otherwise.
    :doc-author: Trelent
    """

    try:
        if len(triangle) == 3:
            for leg in triangle:

                try:
                    float(leg)
                    if leg == 0:
                        raise ValueError(f"the length of triangle leg couldn't be 0")
                except (ValueError, TypeError) as exp:
                    logging.error(f"is_pythagorean_triplet({triangle}) --> {exp.__class__.__qualname__}: {exp}!")
                    return False

            triangle.sort()
            leg_a, leg_b, hypotenuse = triangle[0], triangle[1], triangle[2]

            if leg_b != hypotenuse:
                return leg_a ** 2 + leg_b ** 2 == hypotenuse ** 2
            else:
                raise ValueError(f"the length of hypotenuse ({hypotenuse}) and the triangle leg ({leg_b}) couldn't be equal")
        else:
            raise AttributeError(f'Expected the list of 3 numbers, but got {len(triangle)}')

    except Exception as exp:
        logging.error(f"is_pythagorean_triplet({triangle}) --> {exp.__class__.__qualname__}: {exp}!")
        return False


if __name__ == '__main__':
    is_pythagorean()