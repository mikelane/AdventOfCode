#!/usr/bin/env python3

"""
--- Day 3: Perfectly Spherical Houses in a Vacuum ---

Santa is delivering presents to an infinite two-dimensional grid of houses.

He begins by delivering a present to the house at his starting location, and
then an elf at the North Pole calls him via radio and tells him where to move
next. Moves are always exactly one house to the north (^), south (v), east (>),
or west (<). After each move, he delivers another present to the house at his
new location.

However, the elf back at the north pole has had a little too much eggnog, and so
his directions are a little off, and Santa ends up visiting some houses more
than once. How many houses receive at least one present?

For example:

> delivers presents to 2 houses: one at the starting location, and one to the
east.
^>v< delivers presents to 4 houses in a square, including twice to the house at
his starting/ending location.
^v^v^v^v^v delivers a bunch of presents to some very lucky children at only 2
houses.


--- Part Two ---

The next year, to speed up the process, Santa creates a robot version of
himself, Robo-Santa, to deliver presents with him.

Santa and Robo-Santa start at the same location (delivering two presents to the
same starting house), then take turns moving based on instructions from the elf,
who is eggnoggedly reading from the same script as the previous year.

This year, how many houses receive at least one present?

For example:

^v delivers presents to 3 houses, because Santa goes north, and then Robo-Santa
goes south.
^>v< now delivers presents to 3 houses, and Santa and Robo-Santa end up back
where they started.
^v^v^v^v^v now delivers presents to 11 houses, with Santa going one direction
and Robo-Santa going the other.
"""

__author__ = "Mike Lane"
__copyright__ = "Copyright 2015, Michael Lane"
__license__ = "GPL"
__version__ = "3.0"
__email__ = "mikelane@gmail.com"

visited_houses = {(0, 0)}
santa_current = [0, 0]
robo_current = [0, 0]
whose_turn = 0


def left():
    global whose_turn
    if whose_turn == 0:
        santa_current[0] -= 1
        visited_houses.add(tuple(santa_current))
    else:
        robo_current[0] -= 1
        visited_houses.add(tuple(robo_current))
    print('santa: {}\trobo santa: {}'.format(santa_current, robo_current))
    whose_turn = (whose_turn + 1) % 2


def right():
    global whose_turn
    if whose_turn == 0:
        santa_current[0] += 1
        visited_houses.add(tuple(santa_current))
    else:
        robo_current[0] += 1
        visited_houses.add(tuple(robo_current))
    print('santa: {}\trobo santa: {}'.format(santa_current, robo_current))
    whose_turn = (whose_turn + 1) % 2


def up():
    global whose_turn
    if whose_turn == 0:
        santa_current[1] += 1
        visited_houses.add(tuple(santa_current))
    else:
        robo_current[1] += 1
        visited_houses.add(tuple(robo_current))
    print('santa: {}\trobo santa: {}'.format(santa_current, robo_current))
    whose_turn = (whose_turn + 1) % 2


def down():
    global whose_turn
    if whose_turn == 0:
        santa_current[1] -= 1
        visited_houses.add(tuple(santa_current))
    else:
        robo_current[1] -= 1
        visited_houses.add(tuple(robo_current))
    print('santa: {}\trobo santa: {}'.format(santa_current, robo_current))
    whose_turn = (whose_turn + 1) % 2


moves = {'<': left,
         '^': up,
         '>': right,
         'v': down}

with open('input2.txt', 'r') as f:
    data = f.read()

print('santa: {}\trobo santa: {}'.format(santa_current, robo_current))

for c in data:
    moves[c]()

print('visited_houses: {}\n'
      '  total unique: {}'.format(visited_houses, len(visited_houses)))
