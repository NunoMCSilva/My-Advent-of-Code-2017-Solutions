import pytest

import solutions.day4.solver as solver


@pytest.mark.parametrize('test_input, test_output', [
    ('aa bb cc dd ee', True),
    ('aa bb cc dd aa', False),
    ('aa bb cc dd aaa', True),
])
def test_is_valid(test_input, test_output):
    # act
    output = solver.is_valid(test_input)

    # assert
    assert output == test_output


@pytest.mark.parametrize('test_input, test_output', [
    ('abcde fghij', True),
    ('abcde xyz ecdab', False),
    ('a ab abc abd abf abj', True),
    ('iiii oiii ooii oooi oooo', True),
    ('oiii ioii iioi iiio', False),
])
def test_is_valid2(test_input, test_output):
    # act
    output = solver.is_valid2(test_input)

    # assert
    assert output == test_output


# added after solution found
def test_part1():
    assert solver.part1('solutions/day4') == 383


def test_part2():
    assert solver.part2('solutions/day4') == 265
