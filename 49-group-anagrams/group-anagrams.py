from collections import defaultdict
class Solution(object):
    
    def groupAnagrams(self, strs):
        dic = defaultdict(list)

        for s in strs:
            count = [0] * 26

            for ch in s:
                count[ord(ch) - ord('a')] += 1

            dic[tuple(count)].append(s)

        return list(dic.values())
        