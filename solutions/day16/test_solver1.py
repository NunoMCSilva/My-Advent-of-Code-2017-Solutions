#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pytest

import solutions.day16.solver1 as solver


@pytest.mark.parametrize('test_programs, test_move, test_output', [
    ('abcde', 's3', 'cdeab'),
    ('abcde', 's1', 'eabcd'),
])
def test_spin(test_programs, test_move, test_output):
    assert solver.spin(test_programs, test_move) == test_output


@pytest.mark.parametrize('test_programs, test_move, test_output', [
    ('abcde', 'x3/1', 'adcbe'),
    ('eabcd', 'x3/4', 'eabdc'),
])
def test_exchange(test_programs, test_move, test_output):
    assert solver.exchange(test_programs, test_move) == test_output


@pytest.mark.parametrize('test_programs, test_move, test_output', [
    ('abcde', 'pc/d', 'abdce'),
    ('eabdc', 'pe/b', 'baedc')
])
def test_partner(test_programs, test_move, test_output):
    assert solver.partner(test_programs, test_move) == test_output


@pytest.mark.parametrize('test_programs, test_moves, test_output', [
    ('abcde', ('s1', 'x3/4', 'pe/b'), 'baedc'),
])
def test_solve(test_programs, test_moves, test_output):
    assert solver.solve(test_programs, test_moves) == test_output
