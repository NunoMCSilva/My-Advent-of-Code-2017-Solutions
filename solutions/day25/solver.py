#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re

import solutions.utils as utils


def parse_and_set(phrase, line, machine, key, func):
    mo = re.search(phrase, line)
    if mo is not None:
        machine[key] = func(mo)


def if_parse(phrase, line):
    mo = re.search(phrase, line)
    return mo is not None, mo


# TODO: this needs a lot of work to be more generic...
def parse_blueprint(lines):
    machine = {'tape': {},
               'cursor': 0,
               'states': {},
               'steps': None,
               'current state': None}

    state = [None, None, None, None, None]
    state_ = {}
    for line in lines:
        # initial state
        parse_and_set(r'Begin in state ([A-Z]).', line, machine, 'current state', lambda mo: mo.group(1))

        # checksum
        parse_and_set(r'Perform a diagnostic checksum after (\d+) steps.', line, machine, 'steps', lambda mo: int(mo.groups(1)[0]))

        # in state
        flag, mo = if_parse('In state ([A-Z])', line)
        if flag:
            state[0] = mo.group(1)

        if state[0] is not None:
            # if current value
            flag, mo = if_parse(r'If the current value is (\d+):', line)
            if flag:
                state[1] = int(mo.group(1)[0])

            if state[1] is not None:
                # write
                flag, mo = if_parse(r'- Write the value (\d+).', line)
                if flag:
                    state[2] = int(mo.group(1)[0])

                # move
                flag, mo = if_parse(r'- Move one slot to the (right|left).', line)
                if flag:
                    state[3] = 1 if mo.group(1) == 'right' else -1

                # continue
                flag, mo = if_parse(r'- Continue with state ([A-Z]).', line)
                if flag:
                    state[4] = mo.group(1)
                    state_[state[1]] = (state[2], state[3], state[4])
                    for i in (2, 3, 4):
                        state[i] = None

        # empty
        if line == '':
            if state_ != {}:
                machine['states'][state[0]] = state_
                state_ = {}
                #print(states)

    if state_ != {}:
        machine['states'][state[0]] = state_
        state_ = {}

    return machine


def execute_step(machine):
    state = machine['states'][machine['current state']]
    value = machine['tape'].get(machine['cursor'], 0)
    op = state[value]
    w, m, g = op

    machine['tape'][machine['cursor']] = w
    machine['cursor'] += m
    machine['current state'] = g
    machine['steps'] -= 1

    # yes, it alters machine, but...
    return machine


def diagnostic_checksum(machine):
    return sum(filter(lambda n: n == 1, machine['tape'].values()))


def execute(machine):
    while True:
        machine = execute_step(machine)
        if machine['steps'] == 0:
            return diagnostic_checksum(machine)


# TODO: this takes a bit to execute, profile and optimize
def part1(dpath):
    lines = utils.get_input_by_line(utils.get_fpath(dpath))
    machine = parse_blueprint(lines)
    return execute(machine)


def part2(dpath):
    raise NotImplementedError
