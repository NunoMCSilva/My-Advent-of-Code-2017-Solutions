#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import solutions.utils as utils


def execute_instruction(registers, instruction):
    register, op, num, condition = instruction
    condition_register, condition_op, condition_num = condition

    # condition
    if condition_register not in registers:
        registers[condition_register] = 0

    condition_bool = False
    if condition_op == '>':
        condition_bool = registers[condition_register] > condition_num
    elif condition_op == '<':
        condition_bool = registers[condition_register] < condition_num
    elif condition_op == '>=':
        condition_bool = registers[condition_register] >= condition_num
    elif condition_op == '==':
        condition_bool = registers[condition_register] == condition_num
    elif condition_op == '<=':
        condition_bool = registers[condition_register] <= condition_num
    elif condition_op == '!=':
        condition_bool = registers[condition_register] != condition_num
    else:
        raise Exception('missing condition op:', condition_op)

    # result
    if condition_bool:
        register_value = registers.get(register, 0)
        if op == 'inc':
            registers[register] = register_value + num
        elif op == 'dec':
            registers[register] = register_value - num
        else:
            raise Exception('missing op:', op)
    else:
        if register not in registers:
            registers[register] = 0


def parse_instruction(instruction):
    register, op, num, _, if_register, if_op, if_num = instruction.split(' ')
    return (register, op, int(num), (if_register, if_op, int(if_num)))


def solver1(iterable):
    registers = {}

    for instruction in iterable:
        execute_instruction(registers, parse_instruction(instruction))

    return max(registers.values())


def solver2(iterable):
    registers = {}
    max_value = 0

    for instruction in iterable:
        execute_instruction(registers, parse_instruction(instruction))
        max_value = max((max(registers.values()), max_value))

    return max_value


def part1(dpath):
    return solver1(utils.get_input_by_line(utils.get_fpath(dpath)))


def part2(dpath):
    return solver2(utils.get_input_by_line(utils.get_fpath(dpath)))
