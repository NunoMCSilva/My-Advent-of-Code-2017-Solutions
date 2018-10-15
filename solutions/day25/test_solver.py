#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pytest

import solutions.day25.solver as solver
import solutions.utils as utils


@pytest.mark.parametrize('test_input, test_output', [
    (
        utils.get_input_by_line(utils.get_fpath('solutions/day25', 'test_input.txt')),
        {
            'tape': {},
            'cursor': 0,
            'states': {
                'A': {0: (1, 1, 'B'), 1: (0, -1, 'B')},
                'B': {0: (1, -1, 'A'), 1: (1, 1, 'A')},
            },
            'steps': 6,
            'current state': 'A',
        }
    ),
])
def test_parse_blueprint(test_input, test_output):
    assert solver.parse_blueprint(test_input) == test_output


@pytest.mark.parametrize('test_input, test_output', [
    (
        {
            'tape': {},
            'cursor': 0,
            'states': {
                'A': {0: (1, 1, 'B'), 1: (0, -1, 'B')},
                'B': {0: (1, -1, 'A'), 1: (1, 1, 'A')},
            },
            'steps': 6,
            'current state': 'A',
        },
        {
            'tape': {0: 1},
            'cursor': 1,
            'states': {
                'A': {0: (1, 1, 'B'), 1: (0, -1, 'B')},
                'B': {0: (1, -1, 'A'), 1: (1, 1, 'A')},
            },
            'steps': 5,
            'current state': 'B',
        }
    ),
    (
        {
            'tape': {0: 1},
            'cursor': 1,
            'states': {
                'A': {0: (1, 1, 'B'), 1: (0, -1, 'B')},
                'B': {0: (1, -1, 'A'), 1: (1, 1, 'A')},
            },
            'steps': 5,
            'current state': 'B',
        },
        {
            'tape': {0: 1, 1: 1},
            'cursor': 0,
            'states': {
                'A': {0: (1, 1, 'B'), 1: (0, -1, 'B')},
                'B': {0: (1, -1, 'A'), 1: (1, 1, 'A')},
            },
            'steps': 4,
            'current state': 'A',
        }
    ),
    (
        {
            'tape': {0: 1, 1: 1},
            'cursor': 0,
            'states': {
                'A': {0: (1, 1, 'B'), 1: (0, -1, 'B')},
                'B': {0: (1, -1, 'A'), 1: (1, 1, 'A')},
            },
            'steps': 4,
            'current state': 'A',
        },
        {
            'tape': {0: 0, 1: 1},
            'cursor': -1,
            'states': {
                'A': {0: (1, 1, 'B'), 1: (0, -1, 'B')},
                'B': {0: (1, -1, 'A'), 1: (1, 1, 'A')},
            },
            'steps': 3,
            'current state': 'B',
        }
    ),
    # yes, I could put more tests...
])
def test_execute_step(test_input, test_output):
    assert solver.execute_step(test_input) == test_output


@pytest.mark.parametrize('test_input, test_output', [
    (
        {
            'tape': {},
            'cursor': 0,
            'states': {
                'A': {0: (1, 1, 'B'), 1: (0, -1, 'B')},
                'B': {0: (1, -1, 'A'), 1: (1, 1, 'A')},
            },
            'steps': 6,
            'current state': 'A',
        },
        0
    ),
    (
        {
            'tape': {0: 1, 1: 1},
            'cursor': 0,
            'states': {
                'A': {0: (1, 1, 'B'), 1: (0, -1, 'B')},
                'B': {0: (1, -1, 'A'), 1: (1, 1, 'A')},
            },
            'steps': 4,
            'current state': 'A',
        },
        2
    ),
    (
        {
            'tape': {0: 0, 1: 1},
            'cursor': -1,
            'states': {
                'A': {0: (1, 1, 'B'), 1: (0, -1, 'B')},
                'B': {0: (1, -1, 'A'), 1: (1, 1, 'A')},
            },
            'steps': 3,
            'current state': 'B',
        },
        1
    ),
])
def test_diagnostic_checksum(test_input, test_output):
    assert solver.diagnostic_checksum(test_input) == test_output


# added after solutions were found
def test_part1():
    assert solver.part1('solutions/day25') == 2474
