class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        pass

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_map = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        result = 0

        for i in range(len(s) - 1):
            if roman_map[s[i]] < roman_map[s[i + 1]]:
                result -= roman_map[s[i]]
            else:
                result += roman_map[s[i]]

        result += roman_map[s[-1]]  # add the last numeral

        return result

