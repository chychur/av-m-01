import math

from pythagorean_pants import is_pythagorean


def test_is_pythagorean_pans():
    # successful test: correct Pythagorean triangle
    assert is_pythagorean([5, 3, 4]) == True

    # successful test: correct Pythagorean triangle
    assert is_pythagorean([12.5, 7.5, 10]) == True

    # successful test: correct Pythagorean triangle
    assert is_pythagorean([6, 8, 10]) == True

    # successful test: correct Pythagorean triangle - isosceles right triangle
    assert is_pythagorean([7, 7, math.sqrt((7 ** 2) * 2)]) == True

    # failed test: non-Pythagorean triangle
    assert is_pythagorean([100, 3, 65]) == False

    # failed test: wrong number of elements
    assert is_pythagorean([3, 4]) == False

    # failed test: wrong number of elements
    assert is_pythagorean([3, 4, 5, 6]) == False

    # failed test: elements are not numbers, but string
    assert is_pythagorean([5, 'test', 13]) == False

    # failed test: elements are not numbers, but dictionary
    assert is_pythagorean([5, 16, {'a': 3}]) == False

    # failed test: elements are not numbers, but list
    assert is_pythagorean([5, [4], 2]) == False

    # failed test: elements are not numbers, but one is None
    assert is_pythagorean([None, 4, 3]) == False

    # failed test: parameter is None
    assert is_pythagorean(None) == False

    # failed test: one of list elements - 0
    assert is_pythagorean([3, 0, 5]) == False

    # failed test: all elements - 0
    assert is_pythagorean([0, 0, 0]) == False

    # failed test: the leg of triangle equal its hypotenuse
    assert is_pythagorean([4, 5, 5]) == False

    print("All tests passed successfully!")


if __name__ == '__main__':
    test_is_pythagorean_pans()