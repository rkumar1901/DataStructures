class Solution:
    def isValid(self, s: str) -> bool:

        dic = {')':'(', '}':'{', ']':'['}
        res = []

        for r in s:

            if r in dic and res:
                ans = res.pop()
                if dic[r] != ans:
                    return False
                else:
                    continue
            elif r in dic and not res:
                return False

            res.append(r)

        return False if res else True






        