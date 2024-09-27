class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        pass

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        mapping = {")": "(", "}": "{", "]": "["}

        for char in s:
            if char in mapping.values():  # opening bracket
                stack.append(char)
            elif char in mapping:  # closing bracket
                if not stack or mapping[char] != stack.pop():
                    return False

        return not stack






    



  

