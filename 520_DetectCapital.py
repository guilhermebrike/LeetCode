"""
520. Detect Capital

Given a word, you need to judge whether the usage of capitals in it is right or not.

We define the usage of capitals in a word to be right when one of the following cases holds:

All letters in this word are capitals, like "USA".
All letters in this word are not capitals, like "leetcode".
Only the first letter in this word is capital, like "Google".
Otherwise, we define that this word doesn't use capitals in a right way.


Example 1:

Input: "USA"
Output: True


Example 2:

Input: "FlaG"
Output: False


Note: The input will be a non-empty word consisting of uppercase and lowercase latin letters.
"""


class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """

        if len(word) == 1:
            return True
        else:
            if ord(word[0]) >= 65 and ord(word[0]) <= 90 and ord(word[1]) >= 65 and ord(word[1]) <= 90 :
                # first and second words are Capital
                for i in range(2,len(word)):
                    if ord(word[i]) >= 95 and ord(word[i]) <= 122:
                        return False
            elif ord(word[0]) >= 65 and ord(word[0]) <= 90 and ord(word[1]) >= 97 and ord(word[1]) <= 122 :
                # first letter capital, second letter lowercase
                for i in range(2,len(word)):
                    if ord(word[i]) >= 65 and ord(word[i]) <= 90:
                        return False
            elif ord(word[0]) >= 97 and ord(word[0]) <= 122 and ord(word[1]) >= 65 and ord(word[1]) <= 90 :
                # first letter lower, second letter Capital
                return False
            else:
                #both letters lowercase
                for i in range(2,len(word)):
                    if ord(word[i]) >= 65 and ord(word[i]) <= 90:
                        return False
            return True




    print(detectCapitalUse("a","mL"))


