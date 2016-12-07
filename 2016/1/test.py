#!/usr/bin/env python3

"""
Short description

Longer description
"""

__author__ = "Mike Lane"
__copyright__ = "Copyright 2016, Michael Lane"
__license__ = "GPL"
__version__ = "3.0"
__email__ = "mikelane@gmail.com"


import re
result = re.findall(r'([R|L])(\d+)', 'R191')
inst, d = result[0]
print(inst, d)