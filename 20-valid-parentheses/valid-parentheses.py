class Solution:
    def isValid(self, s: str) -> bool:

        dic = {')':'(', '}':'{', ']':'['}
        res = []

        for r in s:

            if r in dic:

                if not res or dic[r] != res.pop():
                    return False
            else:
                res.append(r)

        return False if res else True






        