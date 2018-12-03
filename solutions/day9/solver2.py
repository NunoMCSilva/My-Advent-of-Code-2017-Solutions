#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Now, you're ready to remove the garbage.

To prove you've removed it, you need to count all of the characters within the
garbage. The leading and trailing < and > don't count, nor do any
canceled characters or the ! doing the canceling.

<>, 0 characters.
<random characters>, 17 characters.
<<<<>, 3 characters.
<{!>}>, 2 characters.
<!!>, 0 characters.
<!!!>>, 0 characters.
<{o"i!a,<{i<a>, 10 characters.
How many non-canceled characters are within the garbage in your puzzle input?
"""

import solutions.day9.solver1 as solver
import solutions.utils as utils


def count_garbage_size(stream):
    garbage_counter = 0
    yielded_flag = False
    ignore_flag = False
    for char in stream:
        if ignore_flag:
            if char == '>':
                ignore_flag = False
                yield garbage_counter
                yielded_flag = True
                garbage_counter = 0
                continue
            else:
                garbage_counter += 1
        else:
            if char == '<':
                ignore_flag = True
                continue
            else:
                pass
    if not yielded_flag:
        yield 0


def part2(dpath):
    pruned = solver.prune_exclamations(solver.get_stream(utils.get_fpath(dpath)))
    return sum(count_garbage_size(pruned))
