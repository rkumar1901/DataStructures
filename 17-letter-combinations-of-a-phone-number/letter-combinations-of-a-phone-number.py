class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        if not digits:
            return []

        res, temp = [], []

        phone = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        def tenta(index, temp):

            if len(temp) == len(digits):
                res.append("".join(temp))
                return

            letters = phone[digits[index]]

            for letter in letters:

                temp.append(letter)
                tenta(index + 1, temp)
                temp.pop()

        tenta(0, temp)

        return res
        