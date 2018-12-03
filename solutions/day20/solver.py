#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import collections

import solutions.utils as utils


def parse_value(value):
    a = value.index('<')
    b = value.index('>')
    return [int(i) for i in value[a+1:b].split(',')]


def parse_file(lines):
    for line in lines:
        yield tuple([parse_value(value) for value in line.split(', ')])


def update(particle):
    position, velocity, acceleration = particle
    position_, velocity_, acceleration_ = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

    for i in range(3):
        acceleration_[i] = acceleration[i]

    for i in range(3):
        velocity_[i] = velocity[i] + acceleration_[i]

    for i in range(3):
        position_[i] = position[i] + velocity_[i]

    return position_, velocity_, acceleration_


def distance(particle):
    position = particle[0]
    x, y, z = position
    return abs(x) + abs(y) + abs(z)


def part1(dpath, fname='input.txt'):
    d = dict()
    fpath = utils.get_fpath(dpath, fname)
    #print(fpath)
    for particle in parse_file(utils.get_input_by_line(fpath)):
        #print(particle, distance(particle))

        particle_ = particle
        for i in range(1000):
            particle_ = update(particle_)
        #print(particle_, distance(particle_))
        d[tuple([tuple(l) for l in particle])] = distance(particle_)

    l = [k for k, v in d.items() if min(d.values()) == v]

    if len(l) == 1:
        p, v, a = l[0]
        #print('p=< {},{},{}>, v=< {},{},{}>, a=< {},{},{}>'.format(*p, *v, *a))
        # p=< 642,-2979,-1903>, v=< 90,-425,-270>, a=< -11,34,23>
        # p=< 642,-2979,-1903>, v=< 90,-425,-270>, a=<-11,34,23>
        # p=<642,-2979,-1903>, v=<90,-425,-270>, a=<-11,34,23>
        return [p for p in parse_file(
            utils.get_input_by_line(fpath))].index((list(p), list(v), list(a)))
        # p=< 226,-1933,96>, v=< 0,99,-3>, a=< -1,0,0>
        # 150

    # TODO: yes, I don't plot the evolution to check if all were clear, I just run enough ranges (1000)


def part2(dpath, fname='input.txt'):
    particles = [particle for particle in parse_file(utils.get_input_by_line(utils.get_fpath(dpath, fname)))]

    for i in range(1000):
        #for p in particles:
            #print(p)
        #print()

        particles = [(tuple(p), tuple(v), tuple(c)) for p, v, c in map(update, particles)]
        #for p in particles:
            #print(p)
        #print()

        counter = collections.Counter([p for p, v, a in particles])
        counter_not_1 = {k: v for k, v in counter.items() if v != 1}
        if counter_not_1:
            for remove_p in counter_not_1.keys():
                particles = [(p, v, c) for p, v, c in particles if p != remove_p]
                #print('removed')

    return len(particles)

    # TODO: yes, I don't plot the evolution to check if all were clear, I just run enought ranges (1000)
