"""
500. Keyboard Row

Given a List of words, return the words that can be typed using letters of alphabet on only one row's of American keyboard like the image below.


Example:

Input: ["Hello", "Alaska", "Dad", "Peace"]
Output: ["Alaska", "Dad"]
"""


class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        row1 = "QWERTYUIOP"
        row2 = "ASDFGHJLK"
        row3 = "ZXCVBNM"
        row4 = "qwertyuiop"
        row5 = "asdfghjkl"
        row6 = "zxcvbnm"

        arrayResutl = []

        for string in words:
            rows = set() # creating empty Set
            for c in string:
                if c in row1 or c in row4:
                    rows.add(1)
                elif c in row2 or c in row5:
                    rows.add(2)
                elif c in row3 or c in row6:
                    rows.add(3)
                else:
                    rows.add(4)

            if len(rows) == 1:
                arrayResutl.append(string)

        return arrayResutl

