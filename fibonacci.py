#!/usr/bin/env python3

from collections import defaultdict
from datetime import datetime
from typing import Tuple

__author__ = "Mike Lane"
__copyright__ = "Copyright 2015, Michael Lane"
__license__ = "GPL"
__version__ = "3.0"
__email__ = "mikelane@gmail.com"


class Fibonacci:
    """Object that implements various methods of calculating the nth fibonacci
    value. This is a good introduction to algorithms, time & space efficiency,
    and why we must take these factors into consideration as programmers."""

    def __init__(self):
        self.memo = defaultdict(int)
        self.number_of_operations = 0

    def recursive(self, n):
        """The basic recursive solution.
        """
        if n < 1:
            raise ValueError("Invalid value for n!")

        # Let's raise an error if n > 40 since it starts taking way too long
        if n > 40:
            raise ValueError("TOO BIG")

        self.number_of_operations = 0

        start = datetime.now()
        value = self._recursive(n)
        self.number_of_operations += 2
        duration = (datetime.now() - start).total_seconds()

        return value, self.number_of_operations, duration

    def _recursive(self, n: int) -> int:
        """The basic recursive solution's helper function
        """
        if n == 1 or n == 2:
            self.number_of_operations += 1
            return 1

        value = self._recursive(n - 2) + self._recursive(n - 1)
        self.number_of_operations += 7

        return value

    def memoization(self, n: int) -> Tuple[int, int, float]:
        """The first optimization we can try is called memoization. The problem
         with the recursive solution is that, for sufficiently large values of
         n, it will calculate the same thing many times. So instead of
         calculating something more than once, we calculate it once and then
         store the result into a dict.
        """
        if n < 1:
            raise ValueError("Invalid value for n!")

        # Through trial and error on my machine, it appears n = 1995 is the
        # limit for the recursive depth of this function. So raise an error
        if n > 1995:
            raise ValueError("ERROR")

        # Reset the class's memoization in case some other example has
        #  been called
        self.memo = defaultdict(int)
        self.number_of_operations = 0

        start = datetime.now()
        value = self._memoization(n)
        self.number_of_operations += 2
        duration = (datetime.now() - start).total_seconds()

        return value, self.number_of_operations, duration

    def _memoization(self, n: int) -> int:
        """The helper function for memoization
        """
        # Populate the memo with the base case
        self.memo[1] += 1
        self.memo[2] += 1
        self.number_of_operations += 4

        if n not in self.memo:
            self.memo[n] = self._memoization(n - 2) + self._memoization(n - 1)
            self.number_of_operations += 7

        self.number_of_operations += 1
        return self.memo[n]

    def dynamic_programming(self, n: int) -> Tuple[int, int, float]:
        """What's wrong with memoization? It was a DRASTIC improvement over
         basic recursion. But at what cost? Space efficiency. That memo is a
         dictionary that takes up O(n) space. Additionally, our recursion is
         worse case O(n) stack frames. Bear in mind also, that the assignment
         operations and pushing and popping frames off the stack are now coming
         into play in our efficiency calculation. Python will also limit the
         depth of recursion so at large values of n, we will get an error.

         Enter Dynamic Programming. What do we need to keep track of? For n > 3,
         we only need the previous 2 values, right? So why bother storing
         anything more than that? And while we're at it, let's get rid of the
         recursion to further improve our space efficiency and reduce the
         overhead of calling functions.
        """
        if n < 1:
            raise ValueError("invalid value for n!")

        # This is MUCH faster than recursion and we don't have to worry about
        # the depth of recursion. However, the time grows as the number of
        # entries grows. Let's limit it to 20,000,000 which takes about a
        # minute on a decent machine.
        if n > 20_000_000:
            raise ValueError("TOO BIG")

        start = datetime.now()
        # Define some local variables to keep track of where we are.
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
            self.number_of_operations += 4

        duration = (datetime.now() - start).total_seconds()

        return b, self.number_of_operations, duration

    def closed_form(self, n: int) -> Tuple[int, int, float]:
        """But wait! There's more! Sometimes we get lucky and a sequence like
         this can be calculated directly. If this is the case, the formula for
         calculating a value is called the closed form. The fibonacci sequence
         is an example of a sequence that has a closed form (google it). There
         are some sequences that cannot possibly have a closed form, however
         (e.g. there is no closed form that can calculate the nth digit of pi).

         The upside is that we do not have to calculate every value in the
         sequence prior to our target number. There is a downside, though.
         Because of the limits of floating point precision, we are forced to
         accept an approximate value for the nth fibonacci number which could
         lead to slight errors when the numbers get extremely large.
         Furthermore, the intermediate steps in the calculation (for example
         2^n) will overflow before n gets to be an interesting size. To overcome
         this python has algorithms that work in the background to calculate and
         stitch numbers together. These algorithms take time and, therefore,
         hide some operations from us.
        """
        if n < 1:
            raise ValueError("invalid value for n!")

        # Trial and error says that 604 is as large as I can do.
        if n > 604:
            raise ValueError("TOO BIG")

        self.number_of_operations = 0

        start = datetime.now()
        value = round(
            (((1 + (5 ** 0.5)) ** n) - ((1 - (5 ** 0.5)) ** n))
            / ((2 ** n) * (5 ** 0.5))
        )
        duration = (datetime.now() - start).total_seconds()
        self.number_of_operations += 13

        return value, self.number_of_operations, duration


if __name__ == "__main__":
    fib = Fibonacci()

    print(f'\n\n\t{"Time to calculate fibonacci(2^n) in microseconds":^62}\n')
    print("\t==============================================================")
    print("\t|  n: | Recursive | Memoization | Dynamic Prog | Closed Form |")
    print("\t==============================================================")

    for i in range(0, 22):
        try:
            r = fib.recursive(2 ** i)
            r = r[2]
        except ValueError as e:
            r = e
        try:
            m = fib.memoization(2 ** i)
            m = m[2]
        except ValueError as e:
            m = e
        try:
            d = fib.dynamic_programming(2 ** i)
            d = d[2]
        except ValueError as e:
            d = e
        try:
            c = fib.closed_form(2 ** i)
            c = c[2]
        except ValueError as e:
            c = e

        print(f"\t| {i:>2}: | {r:>9} | {m:>11} | {d:>12} | {c:>11} |")
    print("\t==============================================================")
