"""
507. Perfect Number

We define the Perfect Number is a positive integer that is equal to the sum of all its positive divisors except itself.

Now, given an integer n, write a function that returns true when it is a perfect number and false when it is not.
Example:
Input: 28
Output: True
Explanation: 28 = 1 + 2 + 4 + 7 + 14
Note: The input number n will not exceed 100,000,000. (1e8)
"""

import math


class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0:
            return False

        divisors = []

        i = 1
        while i <= math.sqrt(num):

            if (num % i == 0):

                # If divisors are equal, print only one
                if (num / i == i):
                    divisors.append(i)
                else:
                    # Otherwise print both
                    divisors.append(i)
                    divisors.append(num / i)
            i = i + 1

        divisors.sort()
        del divisors[-1]
        sumOfAllDivisors = sum(divisors)

        if sumOfAllDivisors == num:
            return True
        else:
            return False