import pytest

# would be better not to need this long, but...
import solutions.day2.solver as solver


@pytest.mark.parametrize('test_input, test_output', [
    ([[5, 1, 9, 5], [7, 5, 3], [2, 4, 6, 8]], 18)
])
def test_solver(test_input, test_output):
    # act
    output = solver.solver1(test_input)

    # assert
    assert output == test_output


@pytest.mark.parametrize('test_row, test_output', [
    ([5, 9, 2, 8], (8, 2)),
    ([9, 4, 7, 3], (9, 3)),
    ([3, 8, 6, 5], (6, 3)),
    #([7, 5, 3], None),
])
def test_evenly_divisible(test_row, test_output):
    output = solver._evenly_divisible(test_row)
    assert output == test_output


@pytest.mark.parametrize('test_input, test_output', [
    ((8, 2), 4),
    ((9, 3), 3),
    ((6, 3), 2)
])
def test_evenly_divisible_division(test_input, test_output):
    output = solver._evenly_divisible_division(test_input)
    assert output == test_output


@pytest.mark.parametrize('test_input, test_output', [
    ([[5, 9, 2, 8], [9, 4, 7, 3], [3, 8, 6, 5]], 9),
])
def test_solver2(test_input, test_output):
    output = solver.solver2(test_input)
    assert output == test_output


# added after solutions were found
def test_part1():
    output = solver.part1('solutions/day2')
    assert output == 34581


def test_part2():
    output = solver.part2('solutions/day2')
    assert output == 214
