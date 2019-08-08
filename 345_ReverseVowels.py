class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """

        charArray = []
        charVowels = []

        for i in s:
            if i == "a" or i == "e" or i == "i" or i == "o" or i == "u" or i == "A" or i == "E" or i == "I" or i == "O" or i == "U":
                charArray.append("/")
                charVowels.append(i)
            else:
                charArray.append(i)

        print(charArray)
        print(charVowels)

        charVowels.reverse()

        aux = 0
        for pos, value in enumerate(charArray):
            if charArray[pos] == "/":
                charArray[pos] = charVowels[aux]
                aux += 1

        return ''.join(charArray) # converting string list to string


