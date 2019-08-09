"""
766. Toeplitz Matrix

A matrix is Toeplitz if every diagonal from top-left to bottom-right has the same element.

Now given an M x N matrix, return True if and only if the matrix is Toeplitz.


Example 1:

Input:
matrix = [
  [1,2,3,4],
  [5,1,2,3],
  [9,5,1,2]
]
Output: True
Explanation:
In the above grid, the diagonals are:
"[9]", "[5, 5]", "[1, 1, 1]", "[2, 2, 2]", "[3, 3]", "[4]".
In each diagonal all elements are the same, so the answer is True.
Example 2:

Input:
matrix = [
  [1,2],
  [2,2]
]
Output: False
Explanation:
The diagonal "[1, 2]" has different elements.
"""

import numpy as np


class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        npMatrix = np.matrix(matrix)

        n = len(matrix[0])
        m = len(matrix)
        print(n)

        #numer of diagonals is (m + n) - 1

        lower = m * -1 + 1
        higher = n - 1

        for i in range(lower,higher):
            print(np.diag(npMatrix,i))
            s = set(np.diag(npMatrix,i))
            if len(s) > 1:
                return False

        return True


