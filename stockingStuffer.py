#!/usr/bin/env python

"""
Short description

Longer description
"""

__author__ = "Mike Lane"
__copyright__ = "Copyright 2015, Michael Lane"
__license__ = "GPL"
__version__ = "3.0"
__email__ = "mikelane@gmail.com"

from hashlib import md5
from itertools import count

puzzle_input = 'yzbqklnj'

for i in count(1):
    test = puzzle_input + str(i)
    if md5(test.encode()).hexdigest()[:6] == '000000':
        print(i)
        break

