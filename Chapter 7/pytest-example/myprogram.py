#!/usr/bin/python
import sys

def doubleit(x):
    if not isinstance(x, (int, float)):
        raise TypeError
    var = x*2
    return var

def doublelines(filename):
    with open(filename) as fh:
        num_list = [ str(doubleit(int(val))) for val in fh]
    with open(filename, 'w') as fh:
        fh.write('\n'.join(num_list))

if __name__ == "__main__":
    input_val = sys.argv[1]
    doubled_val = doubleit(input_val)

    print "the value of {0} is {1}".format(input_val, doubled_val)
