class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:

        if len(hand) % groupSize != 0:
            return False
        
        dic = {}

        for i in hand:
            dic[i] = 1 + dic.get(i, 0)

        sorted_nums = sorted(hand)

        for num in sorted_nums:

            if dic[num] == 0:
                continue

            for i in range(groupSize):
                if dic.get(num + i, 0) == 0:
                    return False

                dic[num + i] -= 1

        return True


        