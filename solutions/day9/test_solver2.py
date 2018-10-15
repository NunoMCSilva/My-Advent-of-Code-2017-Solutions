#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pytest

import solutions.day9.solver2 as solver2


@pytest.mark.parametrize('test_input_stream, test_output_stream', [
    ('<>', [0]),
    ('<random characters>', [17]),
    ('<<<<>', [3]),
    ('<{}>', [2]),
    ('<>', [0]),
    ('<{o"i,<{i<a>', [10]),
    ('{}', [0]),
    ('<{}>{}<{}>', [2, 2]),
    ('{{<a},{<a},{<a},{<ab>}}', [17]),
])
def test_count_garbage_size(test_input_stream, test_output_stream):
    # act
    output_stream = solver2.count_garbage_size(test_input_stream)

    # assert
    assert list(output_stream) == test_output_stream
