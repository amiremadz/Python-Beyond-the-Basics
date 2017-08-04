"""
    Usages:
    ./test.py                       (reads out the entire config dict)
    ./test.py thiskey thisvalue	    (sets 'thiskey' and 'thisvalue' in the dict)
"""

import sys
from assigment3 import ConfigDict

cd = ConfigDict('config_file.txt')

if len(sys.argv) == 3:
    key = sys.argv[1]
    value

