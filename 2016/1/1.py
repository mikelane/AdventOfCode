#!/usr/bin/env python3
import functools
import operator

import re

with open('input.txt', 'r') as f:
    input = f.read().strip().split(', ')

start = ((0, 0), 0)
current = ((0, 0), 0)
hdg_update = {'R': 90, 'L': -90}


def manhattan_dist(x, y):
    return sum(abs(functools.reduce(operator.sub, t)) for t in zip(x, y))


def update(curr, inst):
    position, heading = curr
    turn_inst, dist_inst = re.findall(r'([R|L])(\d+)', inst)[0]
    new_heading = (heading + hdg_update[turn_inst]) % 360
    if new_heading == 0:
        new_position = tuple(functools.reduce(operator.add, t) for t in zip(position, (0, int(dist_inst))))
    elif new_heading == 90:
        new_position = tuple(functools.reduce(operator.add, t) for t in zip(position, (int(dist_inst), 0)))
    elif new_heading == 180:
        new_position = tuple(functools.reduce(operator.sub, t) for t in zip(position, (0, int(dist_inst))))
    else:
        new_position = tuple(functools.reduce(operator.sub, t) for t in zip(position, (int(dist_inst), 0)))
    return (new_position, new_heading), manhattan_dist(start[0], new_position)


for inst in input:
    updated_current, updated_curr_dist = update(current, inst)
    print('current loc: {}\t'
          'current hdg: {}\n'
          'instruction: {}\n'
          'updated loc: {}\t'
          'updated hdg: {}\n'
          'dist update: {}\n'
          '-------------------------'.format(current[0],
                                             current[1],
                                             inst,
                                             updated_current[0],
                                             updated_current[1],
                                             updated_curr_dist))
    current = updated_current
