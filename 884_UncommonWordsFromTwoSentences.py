"""
884. Uncommon Words from Two Sentences

We are given two sentences A and B.  (A sentence is a string of space separated words.  Each word consists only of lowercase letters.)

A word is uncommon if it appears exactly once in one of the sentences, and does not appear in the other sentence.

Return a list of all uncommon words.

You may return the list in any order.



Example 1:

Input: A = "this apple is sweet", B = "this apple is sour"
Output: ["sweet","sour"]
Example 2:

Input: A = "apple apple", B = "banana"
Output: ["banana"]
"""


class Solution(object):
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """

        bigString = A + " " + B

        bigStringSplit = bigString.split()

        # print(bigStringSplit)

        mySet = set()
        myArray = []

        for s in bigStringSplit:
            if s in mySet:
                myArray.append(s)
            else:
                mySet.add(s)


        return list(set(bigStringSplit) - set(myArray))

