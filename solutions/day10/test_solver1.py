import pytest

import solutions.day10.solver1 as solver

STATE1 = {'list': [0, 1, 2, 3, 4], 'position': 0, 'skip size': 0}
STATE2 = {'list': [2, 1, 0, 3, 4], 'position': 3, 'skip size': 1}
STATE3 = {'list': [4, 3, 0, 1, 2], 'position': 3, 'skip size': 2}
STATE4 = {'list': [4, 3, 0, 1, 2], 'position': 1, 'skip size': 3}
STATE5 = {'list': [3, 4, 2, 1, 0], 'position': 4, 'skip size': 4}


@pytest.mark.parametrize('test_lst, test_position, test_length, test_output', [
    ([0, 1, 2, 3, 4], 0, 3, [2, 1, 0, 3, 4]),
    ([2, 1, 0, 3, 4], 3, 4, [4, 3, 0, 1, 2]),
    ([4, 3, 0, 1, 2], 3, 1, [4, 3, 0, 1, 2]),
    ([4, 3, 0, 1, 2], 1, 5, [3, 4, 2, 1, 0]),
    ([1, 2, 3], 2, 3, [1, 3, 2]),
])
def test_change_list(test_lst, test_position, test_length, test_output):
    # act
    output = solver.change_list(test_lst, test_position, test_length)

    # assert
    assert test_output == output


@pytest.mark.parametrize('test_state, test_length, test_output', [
    (STATE1, 3, STATE2), (STATE2, 4, STATE3), (STATE3, 1, STATE4), (STATE4, 5, STATE5)
])
def test_change(test_state, test_length, test_output):
    # act
    output = solver.change(test_state, test_length)

    # assert
    assert test_output == output


def test_solver():
    # arrange
    test_state = {'list': list(range(0, 5)), 'position': 0, 'skip size': 0}
    test_length = [3, 4, 1, 5]

    # act
    output = solver.solver(test_state, test_length)

    # assert
    assert test_state['list'] == [3, 4, 2, 1, 0]
    assert test_state['position'] == 4
    assert test_state['skip size'] == 4
    assert output == 12


def test_part1():
    assert solver.part1('solutions/day10') == 48705
