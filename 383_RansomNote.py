"""
383. Ransom Note

Given an arbitrary ransom note string and another string containing letters from all the magazines, write a function that will return true if the ransom note can be constructed from the magazines ; otherwise, it will return false.

Each letter in the magazine string can only be used once in your ransom note.

Note:
You may assume that both strings contain only lowercase letters.

canConstruct("a", "b") -> false
canConstruct("aa", "ab") -> false
canConstruct("aa", "aab") -> true
"""


class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """

        ransomDict = dict()
        magazineDict = dict()

        for c in ransomNote:
            if ransomDict.has_key(c):
                ransomDict[c] += 1
            else:
                ransomDict[c] = 1

        for c in magazine:
            if magazineDict.has_key(c):
                magazineDict[c] += 1
            else:
                magazineDict[c] = 1

        print ransomDict
        print magazineDict

        for k in ransomDict:
            if magazineDict.has_key(k):
                if magazineDict[k] < ransomDict[k]:
                    return False
                else:
                    continue
            else:
                return False

        return True