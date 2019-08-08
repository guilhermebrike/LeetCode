"""
7. Reverse Integer


Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21


"""


class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        if x >= 0:
            reversed = int(str(x)[::-1])
            if reversed >= 2147483651:
                return 0
            else:
                return reversed
        else:
            reversed = (-1 *int(str(x)[::-1][:-1]))
            if reversed <= -2147483651:
                return 0
            else:
                return reversed