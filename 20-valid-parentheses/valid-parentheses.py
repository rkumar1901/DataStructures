class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        dic = {"}": "{", ")": "(", "]":"["}

        temp = []

        for ch in s:

            if temp and ch in dic:
                
                if dic[ch] == temp[-1]:
                    temp.pop()
                    continue
                else: 
                    return False

            temp.append(ch)

        return True if not temp else False

        