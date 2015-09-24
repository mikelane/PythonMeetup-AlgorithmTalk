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
        duration = round((time.clock() - start) * 1000000)

        # return the results in a dict.
        return value, numOps, duration

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

    def memoization(self, n):
        """The first optimization we can try is called memoization. The problem with
        the recursive solution is that, for sufficiently large values of n, it will
        calculate the same thing many times. So instead of calculating something
        more than once, we calculate it once and then store the result into a dict.
        :param n: Which fibonacci number to calculate.
        :return: A tuple (value, numOps, duration) where value is the value of the nth
        fibonacci number, numOps is the number of operations (adds) required, and
        duration is the number of microseconds required.
        """

        # Guarantee that we only try valid values of n.
        if n < 1:
            raise ValueError('Invalid value for n!')

        # Create an empty dictionary to store our results
        memo = {}

        # Start a timer and calculate our value.
        start = time.clock()
        value, numOps = self._memoization(n, memo)
        duration = round((time.clock() - start) * 1000000)

        return value, numOps, duration

    def _memoization(self, n, m):
        """The helper function for memoization
        :param n: Which fibonacci number we are calculating.
        :param m: The memo of previously recorded values.
        :return: A tuple (value, numOps) where the value is the nth fibonacci number
         and numOps is the required number of operations (adds) to get that value.
        """
        # Populate the memo with the base case
        m[1] = (1, 1)
        m[2] = (1, 1)

        # For a given n, if that value is not stored in the memo, calculate it
        # by calling the function recursively.
        if n not in m:
            a = self._memoization(n-2, m)
            b = self._memoization(n-1, m)
            # And then store the calculated value in the memo for future use
            m[n] = (a[0] + b[0], a[1] + b[1] + 1)

        # Now we know that the nth fibonacci number is stored in the memo, so
        # return it to the caller.
        return m[n]

# Testing
fib = Fibonacci()
# for i in range(0, 20):
#     try:
#         result = fib.recursive(i)
#     except ValueError as e:
#         print("\n\033[91mValueError: {0}\033[0m\n\n"
#               "===========================================".format(e))
#     else:
#         print("         n: {}\n"
#               "     value: {}\n"
#               "operations: {}\n"
#               "      time: {} microseconds\n"
#               "===========================================".format(i, result[0], result[1], result[2]))
for i in range(0, 20):
    try:
        result = fib.memoization(i)
    except ValueError as e:
        print("\n\033[91mValueError: {0}\033[0m\n\n"
              "===========================================".format(e))
    else:
        print("         n: {}\n"
              "     value: {}\n"
              "operations: {}\n"
              "      time: {} microseconds\n"
              "===========================================".format(i, result[0], result[1], result[2]))
