from game import play


def test_play():
    # successful test: Plants won with a score of 0:4
    assert play(zombies=[1, 3, 5, 7], plants=[2, 4, 6, 8]) is True

    # successful test: Zombies won with a score of strength 16:6 because of score 2:2
    assert play(zombies=[1, 3, 5, 7], plants=[2, 4]) is False

    # successful test: Plants won with a score of 1:3
    assert play(zombies=[1, 3, 5, 7], plants=[2, 4, 0, 8]) is True

    # successful test: Plants won because the score of strength is equal 5:5 and the score is equal 1:1
    assert play(zombies=[2, 1, 1, 1], plants=[1, 2, 1, 1]) is True

    # failed test: One of list element is None
    assert play(zombies=[1, 2, 1, 1], plants=[2, 1, None, 1]) is None

    # failed test: One of list element is None and the attribute is None
    assert play(zombies=None, plants=[2, 1, None, 1]) is None

    # failed test: Both attributes is None
    assert play(zombies=None, plants=None) is None

    # failed test: One of attribute is 'str' type, not List[int]
    assert play(zombies="Abc", plants=[2, 1, 1]) is None

    # failed test: One of attribute is 'int' type, not List[int]
    assert play(zombies=12, plants=[2, 1, 1]) is None

    # failed test: One of attribute is 'dict' type, not List[int]
    assert play(zombies={1: 'qwerty'}, plants=[2, 1, 1]) is None


if __name__ == '__main__':
    test_play()
