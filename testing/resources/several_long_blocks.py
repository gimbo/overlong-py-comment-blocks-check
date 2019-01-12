import os
import re
import sys

# First block
# which is just
# three lines long

THING = 5

    # Next block
    #
    # is quite a bit longer
    #
    # and it happens to be indented
    #
    # but that's fine, we'll still find it
    # because we really should be able to :-)

def moo(x):
    if x > 1:
        return x + 2

# In fact
    # we even consider mixed indentation
        # to be part of the same comment block
# so this
# will be considered
# to be
    # one block


if __name__ == '__main__':
    exit(0)
