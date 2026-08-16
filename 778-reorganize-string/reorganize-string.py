class Solution(object):
    def reorganizeString(self, s):

        res = [""] * len(s)
        dic = {}
        for i in s:
            dic[i] = 1 + dic.get(i, 0)

        if max(dic.values()) > (len(s) + 1) // 2:
            return ""
 
        sorted_chars = sorted(dic.keys(), key=lambda x: dic[x], reverse=True)

        i = 0
        for ch in sorted_chars:

            while dic[ch] > 0:
                if i >= len(s):
                    i = 1
                
                res[i] = ch
                dic[ch] -= 1
                i += 2

        return "".join(res)
                






        