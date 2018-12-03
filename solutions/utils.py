#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os


def get_fpath(dpath, fname='input.txt'):
    return os.path.join(dpath, fname)


def get_input_by_line(fpath):
    with open(fpath) as f:
        for line in f:
            yield line.replace('\n', '')
