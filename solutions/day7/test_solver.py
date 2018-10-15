#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pytest

import solutions.day7.solver as solver

IN = """pbga (66)
xhth (57)
ebii (61)
havc (66)
ktlj (57)
fwft (72) -> ktlj, cntj, xhth
qoyq (66)
padx (45) -> pbga, havc, qoyq
tknk (41) -> ugml, padx, fwft
jptl (61)
ugml (68) -> gyxo, ebii, jptl
gyxo (61)
cntj (57)"""


def test_solver1():
    # arrange
    in_ = IN.split('\n')
    # print(in_)

    # act & assert
    assert solver.solver1(in_) == 'tknk'


@pytest.mark.parametrize('in_, out', [
    ('pbga (66)', ('pbga', 66, [])),
    ('xhth (57)', ('xhth', 57, [])),
    ('ebii (61)', ('ebii', 61, [])),
    ('havc (66)', ('havc', 66, [])),
    ('ktlj (57)', ('ktlj', 57, [])),
    ('fwft (72) -> ktlj, cntj, xhth', ('fwft', 72, ['ktlj', 'cntj', 'xhth'])),
    ('qoyq (66)', ('qoyq', 66, [])),
    ('padx (45) -> pbga, havc, qoyq', ('padx', 45, ['pbga', 'havc', 'qoyq'])),
    ('tknk (41) -> ugml, padx, fwft', ('tknk', 41, ['ugml', 'padx', 'fwft'])),
    ('jptl (61)', ('jptl', 61, [])),
    ('ugml (68) -> gyxo, ebii, jptl', ('ugml', 68, ['gyxo', 'ebii', 'jptl'])),
    ('gyxo (61)', ('gyxo', 61, [])),
    ('cntj (57)', ('cntj', 57, [])),

    ('qmvebxb (43) -> hjuzxv, nxrlaw, pdewbw, hqlni', ('qmvebxb', 43, ['hjuzxv', 'nxrlaw', 'pdewbw', 'hqlni'])),
    ('gvaie (153) -> cpwdhw', ('gvaie', 153, ['cpwdhw'])),  # UNEXISTENT EXAMPLE
    
])
def test_parse_line(in_, out):
    # act & assert
    assert solver.parse_line(in_) == out


def test_tree_init():
    # act
    stree = solver.SolverTree()

    # assert
    assert stree.weights == {}
    assert stree.connections == {}


@pytest.mark.parametrize('bottom, weight, top, weights, connections', [
    ('pbga', 66, [], {'pbga': 66}, {'pbga': []}),
    ('fwft', 72, ['ktlj', 'cntj', 'xhth'], {'fwft': 72}, {'fwft': ['ktlj', 'cntj', 'xhth']}),
])
def test_tree_add__first_add(bottom, weight, top, weights, connections):
    # arrange
    stree = solver.SolverTree()

    # act
    stree.add(bottom, weight, top)

    # assert
    assert stree.weights == weights
    assert stree.connections == connections


def test_tree_add__first_and_second_add_1():
    # arrange
    stree = solver.SolverTree()

    # act
    stree.add('fwft', 72, ['ktlj', 'cntj', 'xhth'])
    stree.add('tknk', 41, ['ugml', 'padx', 'fwft'])

    # assert
    assert stree.weights == {'tknk': 41, 'fwft': 72}
    assert stree.connections == {'tknk': ['ugml', 'padx', {'fwft': ['ktlj', 'cntj', 'xhth']}]}


def test_tree_add__first_and_second_add_2():
    # arrange
    stree = solver.SolverTree()

    # act
    stree.add('tknk', 41, ['ugml', 'padx', 'fwft'])
    stree.add('fwft', 72, ['ktlj', 'cntj', 'xhth'])

    # assert
    assert stree.weights == {'tknk': 41, 'fwft': 72}
    assert stree.connections == {'tknk': ['ugml', 'padx', {'fwft': ['ktlj', 'cntj', 'xhth']}]}


def test_tree_add__other_adds():
    # arrange
    stree = solver.SolverTree()

    # act
    stree.add('a', 1, ['b', 'c'])
    stree.add('b', 2, ['d', 'e'])
    stree.add('d', 3, ['f', 'g'])

    # assert
    assert stree.weights == {'a': 1, 'b': 2, 'd': 3}
    assert stree.connections == {'a': [{'b': [{'d': ['f', 'g']}, 'e']}, 'c']}


def test_tree_add__full():
    # arrange
    stree = solver.SolverTree()

    # act
    for bottom, weight, top in [('pbga', 66, []),
                                ('xhth', 57, []),
                                ('ebii', 61, []),
                                ('havc', 66, []),
                                ('ktlj', 57, []),
                                ('fwft', 72, ['ktlj', 'cntj', 'xhth']),
                                ('qoyq', 66, []),
                                ('padx', 45, ['pbga', 'havc', 'qoyq']),
                                ('tknk', 41, ['ugml', 'padx', 'fwft']),
                                ('jptl', 61, []),
                                ('ugml', 68, ['gyxo', 'ebii', 'jptl']),
                                ('gyxo', 61, []),
                                ('cntj', 57, [])]:
        stree.add(bottom, weight, top)

    # assert
    assert stree.weights == {'pbga': 66, 'xhth': 57, 'ebii': 61, 'havc': 66,
                             'ktlj': 57, 'fwft': 72, 'qoyq': 66, 'padx': 45,
                             'tknk': 41, 'jptl': 61, 'ugml': 68, 'gyxo': 61,
                             'cntj': 57}
    assert stree.connections == {'tknk': [{'ugml': [{'gyxo': []}, {'ebii': []}, {'jptl': []}]},
                                          {'padx': [{'pbga': []}, {'havc': []}, {'qoyq': []}]},
                                          {'fwft': [{'ktlj': []}, {'cntj': []}, {'xhth': []}]}]}
    assert stree.is_tree_connected() is True
    assert stree.get_root() == 'tknk'


def test_tree_not_connected():
    # arrange
    stree = solver.SolverTree()

    # act
    stree.add('a', 1, [])
    stree.add('b', 1, [])

    # assert
    assert stree.is_tree_connected() is False
    assert stree.get_root() is None


def arrange_stree_in():
    stree = solver.SolverTree()

    for line in IN.split('\n'):
        stree.add(*solver.parse_line(line))

    return stree


@pytest.mark.parametrize('test_name, test_weight', [
    ('gyxo', 61),
    ('ebii', 61),
    ('jptl', 61),

    ('pbga', 66),
    ('havc', 66),
    ('qoyq', 66),

    ('ktlj', 57),
    ('cntj', 57),
    ('xhth', 57),

    ('ugml', 68 + 3 * 61),
    ('padx', 45 + 3 * 66),
    ('fwft', 72 + 3 * 57),

    ('tknk', 41 + 251 + 243 * 2),
])
def test_get_tower_weight(test_name, test_weight):
    # arrange
    stree = arrange_stree_in()

    # act
    weight = stree.get_tower_weight(test_name)

    # assert
    assert weight == test_weight


@pytest.mark.parametrize('test_name, test_bool', [
    ('gyxo', True),
    ('ebii', True),
    ('jptl', True),

    ('pbga', True),
    ('havc', True),
    ('qoyq', True),

    ('ktlj', True),
    ('cntj', True),
    ('xhth', True),

    ('ugml', True),
    ('padx', True),
    ('fwft', True),

    ('tknk', False),
])
def test_is_disc_balanced(test_name, test_bool):
    # arrange
    stree = arrange_stree_in()

    # act
    bool_ = stree.is_disc_balanced(test_name)

    # assert
    assert bool_ == test_bool


def test_find_unbalanced_disc():
    # arrange
    stree = arrange_stree_in()

    # act & assert
    assert stree.find_unbalanced_disc() == 'tknk'


def test_determinate_weight_correction():
    # arrange
    stree = arrange_stree_in()

    # act & assert
    assert stree.determinate_weight_correction() == ('ugml', 60)


@pytest.mark.parametrize('test_name1, test_name2, test_bool', [
    ('ugml', 'ugml', True),
    ('ugml', 'gyxo', True),
    ('gyxo', 'ugml', False),
    ('tknk', 'gyxo', True),
    ('gyxo', 'tknk', False),
    ('pbga', 'havc', False),
])
def test_le(test_name1, test_name2, test_bool):
    # arrange
    stree = arrange_stree_in()

    # act & assert
    assert stree.le(test_name1, test_name2) == test_bool


#@pytest.mark.skip
def test_solver2():
    # arrange
    in_ = IN.split('\n')

    # act & assert
    assert solver.solver2(in_) == 60


# added after solutions found
def test_part1():
    assert solver.part1('solutions/day7') == 'rqwgj'


def test_part2():
    assert solver.part2('solutions/day7') == 333
