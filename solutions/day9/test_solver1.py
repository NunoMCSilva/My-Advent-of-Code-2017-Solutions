#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pytest

import solutions.day9.solver1 as solver


@pytest.mark.parametrize('test_input_stream, test_output_stream', [
    ('<{!>}>', '<{}>'),
    ('<!!>', '<>'),
    ('<!!!>>', '<>'),
    ('{{<!>},{<!>},{<!>},{<a>}}', '{{<},{<},{<},{<a>}}'),
    ('{{<!!>},{<!!>},{<!!>},{<!!>}}', '{{<>},{<>},{<>},{<>}}'),
    ('{{<a!>},{<a!>},{<a!>},{<ab>}}', '{{<a},{<a},{<a},{<ab>}}'),
])
def test_prune_exclamations(test_input_stream, test_output_stream):
    # act
    output_stream = solver.prune_exclamations(test_input_stream)

    # assert
    assert ''.join(list(output_stream)) == test_output_stream


@pytest.mark.parametrize('test_input_stream, test_output_stream', [
    # self-contained pieces of garbage
    ('<>', ''),
    ('<random characters>', ''),
    ('<<<<>', ''),
    ('<{}>', ''),
    ('<>', ''),
    ('<{o"i!a,<{i<a>', ''),
    # whole streams
    ('{}', '{}'),
    ('{{{}}}', '{{{}}}'),
    ('{{},{}}', '{{},{}}'),
    ('{{{},{},{{}}}}', '{{{},{},{{}}}}'),
    ('{<{},{},{{}}>}', '{}'),
    ('{<a>,<a>,<a>,<a>}', '{,,,}'),
    ('{{<a>},{<a>},{<a>},{<a>}}', '{{},{},{},{}}'),
    ('{{<},{<},{<},{<a>}}', '{{}}'),
    # more
    ('{{<ab>},{<ab>},{<ab>},{<ab>}}', '{{},{},{},{}}'),
    ('{{<>},{<>},{<>},{<>}}', '{{},{},{},{}}'),
    ('{{<a},{<a},{<a},{<ab>}}', '{{}}'),
])
def test_prune_garbage(test_input_stream, test_output_stream):
    # act
    output_stream = solver.prune_garbage(test_input_stream)

    # assert
    assert ''.join(list(output_stream)) == test_output_stream


@pytest.mark.parametrize('test_input_stream, test_output_stream', [
    ('', []),
    ('{}', [1]),
    ('{{{}}}', [1, 2, 3]),
    ('{{},{}}', [1, 2, 2]),
    ('{{{},{},{{}}}}', [1, 2, 3, 3, 3, 4]),
    ('{,,,}', [1]),
    ('{{},{},{},{}}', [1, 2, 2, 2, 2]),
    ('{{}}', [1, 2]),
])
def test_score_groups(test_input_stream, test_output_stream):
    # act
    output_stream = solver.score_groups(test_input_stream)

    # assert
    assert list(output_stream) == test_output_stream
