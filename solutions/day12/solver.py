#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import solutions.utils as utils


def get_input(fpath):
    with open(fpath) as f:
        for line in f:
            yield line.replace('\n', '')


def parse_lines(lines):
    for line in lines:
        f, t = line.split(' <-> ')
        yield [int(f), [int(n) for n in t.split(', ')]]


def build_graph(lines):
    graph = {}
    for k, v in lines:
        graph[k] = tuple(v)
    return graph


# TODO: not very efficient, but...
def is_connected(k, graph, visited, objective=0):
    visited[k] = True

    if k == objective:
        return True
    else:
        for v in graph[k]:
            if not visited.get(v, False) and is_connected(v, graph, visited):
                return True
        return False


def check_connections(graph, objective=0):
    connected = {k: False for k in graph}   # connected to 0?

    for k, v in graph.items():
        connected[k] = is_connected(k, graph, {}, objective)

    return connected


# TODO: REDO, not working...
def count_groups(graph):
    groups = 0
    import copy
    g = copy.deepcopy(graph)

    for k in graph:
        conns = check_connections(g, k)
        if len([True for k2, v2 in conns.items() if v2]) != 0:
            groups += 1
        g = {k1: v1 for k1, v1 in g.items() if not conns[k1]}

    return groups


def part1(dpath):
    graph = build_graph(parse_lines(utils.get_input_by_line(utils.get_fpath(dpath))))
    connected = check_connections(graph)

    return sum(True for k, v in connected.items() if v)
    #print(count_groups(graph))


def part2(dpath):
    raise NotImplementedError
