class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        x = ''.join(c for c in s if c.isalnum()).lower()
        if x[::-1] == x:
            return True
        else:
            return False
        