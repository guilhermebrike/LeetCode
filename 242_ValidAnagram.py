"""
242. Valid Anagram

Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?
"""


class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        sDict = dict()
        tDict = dict()

        for c in s:
            if sDict.has_key(c):
                sDict[c] +=1
            else:
                sDict[c] = 1

        for c in t:
            if tDict.has_key(c):
                tDict[c] +=1
            else:
                tDict[c] = 1

        print(sDict)
        print(tDict)

        shared_items = {k: sDict[k] for k in sDict if k in tDict and sDict[k] == tDict[k]}
        return len(shared_items) == len(sDict) == len(tDict)
