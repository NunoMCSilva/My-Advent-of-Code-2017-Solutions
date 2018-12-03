import collections

import solutions.utils as utils


def get_input(fpath):
    with open(fpath) as f:
        for line in f:
            yield line.replace('\n', '')


def is_valid(passphrase):
    for count in collections.Counter(passphrase.split(' ')).values():
        if count != 1:
            return False
    return True


def is_valid2(passphrase):
    lst = [''.join(sorted(word)) for word in passphrase.split(' ')]
    return True if len(lst) == len(set(lst)) else False


def solver(func, dpath):
    return sum(1 for valid in filter(func, get_input(utils.get_fpath(dpath))))


def part1(dpath):
    return solver(is_valid, dpath)


def part2(dpath):
    return solver(is_valid2, dpath)
