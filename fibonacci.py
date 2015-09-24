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

class Fibonacci:
    """Object that implements various methods of calculating the nth fibonacci
    value. This is a good introduction to algorithms, time & space efficiency,
    and why we must take these factors into consideration as programmers."""

    def __init__(self):
        self.COLOR_RED = '\033[91m'
        self.COLOR_NONE = '\033[0m'
        self.memo = {}
        self.numOps = 0

    def recursive(self, n):
        """The basic recursive solution.
        :param n: Which fibonacci number to calculate, ValueError raised if less
         than 1.
        :return: Tuple (value, numOps, duration) where value is the nth fibonacci
         value, numOps is the number of operations it took to calculate the value,
         and duration is the time required to calculate the value rounded to the
         nearest microsecond.
        """
        if n < 1:
            raise ValueError('Invalid value for n!')

        # Reset the operations counter
        self.numOps = 0

        # Start the timer and call the helper function
        start = time.clock()
        value = self._recursive(n)
        self.numOps += 2
        duration = round((time.clock() - start) * 1000000)

        # return the results in a dict.
        return value, self.numOps, duration

    def _recursive(self, n):
        """The basic recursive solution's helper function
        :param n: Which fibonacci number to calculate. Guaranteed to be greater
         than 0.
        :param numOps: The number of operations used so far in the calculation
        :return: A tuple (value, numOps) where value is the nth fibonacci value and
         numOps is the number of operations used.
        """
        # Base case
        if n == 1 or n == 2:
            self.numOps +=1
            return 1

        # Call the function recursively
        value = self._recursive(n-2) + self._recursive(n-1)
        self.numOps += 7

        return value

    def memoization(self, n):
        """The first optimization we can try is called memoization. The problem with
         the recursive solution is that, for sufficiently large values of n, it will
         calculate the same thing many times. So instead of calculating something
         more than once, we calculate it once and then store the result into a dict.
        :param n: Which fibonacci number to calculate.
        :return: A tuple (value, numOps, duration) where value is the value of the nth
         fibonacci number, numOps is the number of operations required, and duration is
         the number of microseconds required.
        """

        # Guarantee that we only try valid values of n.
        if n < 1:
            raise ValueError('Invalid value for n!')

        # Reset the class's memo and numOps values
        self.memo = {}
        self.numOps = 0

        # Start a timer and calculate our value.
        start = time.clock()
        value = self._memoization(n)
        self.numOps += 2
        duration = round((time.clock() - start) * 1000000)

        return value, self.numOps, duration

    def _memoization(self, n):
        """The helper function for memoization
        :param n: Which fibonacci number we are calculating.
        :param m: The memo of previously recorded values.
        :return: An int value: the value is the nth fibonacci number
        """
        # Populate the memo with the base case
        if 1 not in self.memo:
            self.memo[1] = 1
            self.numOps += 2
        if 2 not in self.memo:
            self.memo[2] = 1
            self.numOps += 2
        else:
            self.numOps += 2

        # For a given n, if that value is not stored in the memo, calculate it
        # by calling the function recursively.
        if n not in self.memo:
            # And then store the calculated value in the memo for future use
            self.memo[n] = self._memoization(n-2) + self._memoization(n-1)
            self.numOps += 7

        # Now we know that the nth fibonacci number is stored in the memo, so
        # return it to the caller.
        self.numOps += 1
        return self.memo[n]

    def dynamicProgramming(self, n):
        """What's wrong with memoization? It was a DRASTIC improvement over basic
         recursion. But at what cost? Space efficiency. That memo is a dictionary that
         takes up O(n) space. Additionally, our recursion is worse case O(n) stack
         frames. Bear in mind also, that the assignment operations and pushing and
         popping frames off the stack are now coming into play in our efficiency
         calculation. Python will also limit the depth of recursion so at large values
         of n, we will get an error.

         Enter Dynamic Programming. What do we need to keep track of? For n > 3, we
         only need the previous 2 values, right? So why bother storing anything more
         than that? And while we're at it, let's get rid of the recursion to further
         improve our space efficiency and reduce the overhead of calling functions.
        :param n: Which fibonacci number we are calculating.
        :return: A tuple (value, numOps, duration) where value is the calcuated value
         of the nth fibonacci number, numOps is the required number of operations
         it took to get there, and duration is the duration of the function in
         microseconds.
        """

        # Guarantee that n is a valid value.
        if n < 1:
            raise ValueError('Invalid value for n!')

        # Start the clock and get to calculating
        start = time.clock()
        # Define some local variables to keep track of where we are.
        a = 1
        b = 1
        value = 1
        self.numOps = 3

        # Return the base case values and stop the clock if required.
        if n == 1 or n == 2:
            duration = round((time.clock() - start) * 1000000)
            self.numOps += 2
            return value, self.numOps, duration

        # Starting at 3 and going to n (range's max value is not inclusive), calculate
        # each successive fibonacci number while storing only the values we need to
        # keep track of for the next step.
        for m in range(3, n+1):
            value = a + b
            a = b
            b = value
            self.numOps += 4

        # Stop the timer.
        duration = round((time.clock() - start) * 1000000)

        return value, self.numOps, duration

# Testing
fib = Fibonacci()
for i in range(0, 20):
    try:
        result = fib.recursive(i)
    except ValueError as e:
        print("\n\033[91mValueError: {0}\033[0m\n\n"
              "===========================================".format(e))
    else:
        print("         n: {}\n"
              "     value: {}\n"
              "operations: {}\n"
              "      time: {} microseconds\n"
              "===========================================".format(i, result[0], result[1], result[2]))
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
for i in range(0, 20):
    try:
        result = fib.dynamicProgramming(i)
    except ValueError as e:
        print("\n\033[91mValueError: {0}\033[0m\n\n"
              "===========================================".format(e))
    else:
        print("         n: {}\n"
              "     value: {}\n"
              "operations: {}\n"
              "      time: {} microseconds\n"
              "===========================================".format(i, result[0], result[1], result[2]))
