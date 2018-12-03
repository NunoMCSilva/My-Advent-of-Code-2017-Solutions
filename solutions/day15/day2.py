#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# using generators

FACTOR_A = 16807
FACTOR_B = 48271
DIV = 2147483647


def generator(initial_value, factor, div):
    value = initial_value
    while True:
        value = (value * factor) % DIV
        if value % div == 0:
            yield value


def judge(generator_a, generator_b, rounds):
    counter = 0
    for value_a, value_b in zip(generator_a, generator_b):
        if value_a & 0xFFFF == value_b & 0xFFFF:
            yield 1
        else:
            yield 0

        counter += 1
        if counter == rounds:
            break


# TODO: yup, also takes a bit to run... profile and optimize
def run(initial_value_a, initial_value_b, rounds=5*10**6):
    generator_a = generator(initial_value_a, FACTOR_A, 4)
    generator_b = generator(initial_value_b, FACTOR_B, 8)
    return sum(judge(generator_a, generator_b, rounds))


def part2(dpath):
    return run(116, 299)    # result: 298
