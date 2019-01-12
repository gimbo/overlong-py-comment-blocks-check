"""A python file containing no comments"""

import os
import re


# Just some fibonacci generator I found somewhere.
#
# The point is there's a comment block here

def fib(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

print(list(fib(10)))
