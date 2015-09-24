#!/usr/bin/env python3

"""
This class handles various methods of calculating the nth fibonacci value.
"""

__author__ = "Mike Lane"
__copyright__ = "Copyright 2015, Michael Lane"
__license__ = "GPL"
__version__ = "3.0"
__email__ = "mikelane@gmail.com"

import time
from pprint import pprint as pp

class Fibonacci:
    """Object that implements various methods of calculating the nth fibonacci
    value. This is a good introduction to algorithms, time & space efficiency,
    and why we must take these factors into consideration as programmers."""

    def recursive(self, n):
        """The basic recursive solution.
        :param n: Which fibonacci number to calculate, ValueError raised if less
         than 1.
        :return: Tuple (value, numOps, duration) where value is the nth fibonacci
         value, numOps is the number of operations (adds) it took to calculate the
         value, and duration is the time required to calculate the value rounded to
         the nearest microsecond.
        """
        if n < 1:
            raise ValueError('Invalid value for n!')

        # Start the timer and call the helper function
        start = time.clock()
        value, numOps = self._recursive(n, 0)
        duration = time.clock() - start

        # return the results in a dict.
        return value, numOps, round(duration*1000000)

    def _recursive(self, n, numOps):
        """The basic recursive solution's helper function
        :param n: Which fibonacci number to calculate. Guaranteed to be greater
         than 0.
        :param numOps: The number of operations used so far in the calculation
        :return: A tuple (value, numOps) where value is the nth fibonacci value and
         numOps is the number of operations (adds) used.
        """
        # Base case
        if n == 1 or n ==2:
            numOps += 1
            return 1, numOps

        # Since we're working with tuples, we need to be a bit more verbose here.
        aVal, aNumOps = self._recursive(n-2, numOps)
        bVal, bNumOps = self._recursive(n-1, numOps)
        value = aVal + bVal
        numOps = aNumOps + bNumOps + 1
        return value, numOps

# Testing
fib = Fibonacci()
for i in range(1, 20):
    result = fib.recursive(i)
    print("         n: {}\n"
          "     value: {}\n"
          "operations: {}\n"
          "      time: {} microseconds\n"
          "===========================================".format(i, result[0], result[1], result[2]))
