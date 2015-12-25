#!/usr/bin/env python3

"""
--- Day 4: The Ideal Stocking Stuffer ---

Santa needs help mining some AdventCoins (very similar to bitcoins) to use as
gifts for all the economically forward-thinking little girls and boys.

To do this, he needs to find MD5 hashes which, in hexadecimal, start with at
least five zeroes. The input to the MD5 hash is some secret key (your puzzle
input, given below) followed by a number in decimal. To mine AdventCoins, you
must find Santa the lowest positive number (no leading zeroes: 1, 2, 3, ...)
that produces such a hash.

For example:

If your secret key is abcdef, the answer is 609043, because the MD5 hash of
abcdef609043 starts with five zeroes (000001dbbfa...), and it is the lowest such
number to do so.
If your secret key is pqrstuv, the lowest number it combines with to make an MD5
hash starting with five zeroes is 1048970; that is, the MD5 hash of
pqrstuv1048970 looks like 000006136ef....

--- Part Two ---

Now find one that starts with six zeroes.
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

