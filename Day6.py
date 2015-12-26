#!/usr/bin/env python3

"""
--- Day 6: Probably a Fire Hazard ---

Because your neighbors keep defeating you in the holiday house decorating
contest year after year, you've decided to deploy one million lights in a
1000x1000 grid.

Furthermore, because you've been especially nice this year, Santa has mailed you
instructions on how to display the ideal lighting configuration.

Lights in your grid are numbered from 0 to 999 in each direction; the lights at
each corner are at 0,0, 0,999, 999,999, and 999,0. The instructions include
whether to turn on, turn off, or toggle various inclusive ranges given as
coordinate pairs. Each coordinate pair represents opposite corners of a
rectangle, inclusive; a coordinate pair like 0,0 through 2,2 therefore refers
to 9 lights in a 3x3 square. The lights all start turned off.

To defeat your neighbors this year, all you have to do is set up your lights by
doing the instructions Santa sent you in order.

For example:

turn on 0,0 through 999,999 would turn on (or leave on) every light.
toggle 0,0 through 999,0 would toggle the first line of 1000 lights, turning off
the ones that were on, and turning on the ones that were off.
turn off 499,499 through 500,500 would turn off (or leave off) the middle four
lights.

After following the instructions, how many lights are lit?


--- Part Two ---

You just finish implementing your winning light pattern when you realize you
mistranslated Santa's message from Ancient Nordic Elvish.

The light grid you bought actually has individual brightness controls; each
light can have a brightness of zero or more. The lights all start at zero.

The phrase turn on actually means that you should increase the brightness of
those lights by 1.

The phrase turn off actually means that you should decrease the brightness of
those lights by 1, to a minimum of zero.

The phrase toggle actually means that you should increase the brightness of
those lights by 2.

What is the total brightness of all lights combined after following Santa's
instructions?

For example:

turn on 0,0 through 0,0 would increase the total brightness by 1.
toggle 0,0 through 999,999 would increase the total brightness by 2000000.
"""

__author__ = "Mike Lane"
__copyright__ = "Copyright 2015, Michael Lane"
__license__ = "GPL"
__version__ = "3.0"
__email__ = "mikelane@gmail.com"

import re

n = 1000
# grid = [list('0' * n) for _ in range(n)]
grid = [[0 for _ in range(n)] for _ in range(n)]


def turn_on(top_left, bottom_right):
    for i in range(top_left[0], bottom_right[0] + 1):
        for j in range(top_left[1], bottom_right[1] + 1):
            grid[i][j] += 1
            # grid[i][j] = '1'


def turn_off(top_left, bottom_right):
    for i in range(top_left[0], bottom_right[0] + 1):
        for j in range(top_left[1], bottom_right[1] + 1):
            grid[i][j] = max(0, grid[i][j] - 1)
            # grid[i][j] = '0'


def toggle(top_left, bottom_right):
    for i in range(top_left[0], bottom_right[0] + 1):
        for j in range(top_left[1], bottom_right[1] + 1):
            grid[i][j] += 2
            # grid[i][j] = str((int(grid[i][j]) + 1) % 2)


def on_count():
    # return sum(_.count('1') for _ in grid)
    return sum(sum(grid, []))

with open('input4.txt', 'r') as f:
    instructions = f.read().split('\n')

for line in instructions:
    r = re.findall(r'\d+', line)
    top_left = [int(r[0]), int(r[1])]
    bottom_right = [int(r[2]), int(r[3])]
    if 'turn on' in line:
        turn_on(top_left, bottom_right)
    elif 'turn off' in line:
        turn_off(top_left, bottom_right)
    else:
        toggle(top_left, bottom_right)

print(on_count())
