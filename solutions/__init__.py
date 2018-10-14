#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# a bit hackish, but...

import importlib

import pytest


def run(day, part):
    try:
        solver = importlib.import_module('solutions.day{}.solver'.format(day))
        func = solver.part1 if part == 1 else solver.part2
        result = func('solutions/day{}'.format(day))
        print(result)
    except ImportError:
        raise NotImplementedError('day {} not implemented'.format(day))
    except AttributeError:
        raise NotImplementedError('part {} not implemented'.format(part))


def test(day):
    pytest.main(['solutions/day{}'.format(day)])
