class Solution:
    def isValid(self, s: str) -> bool:

        dic = {')':'(', '}':'{', ']':'['}

        st = []

        for i in s:

            if i in dic:
                if not st or dic[i] != st.pop():
                    return False
            else:
                st.append(i)

        return len(st) == 0
        