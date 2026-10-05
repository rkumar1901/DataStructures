class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:

        res = [0,0,0]

        for triplet in triplets:

            if (triplet[0] > target[0] or
                triplet[1] > target[1] or
                triplet[2] > target[2]):
                continue

            res[0] = max(triplet[0], res[0])
            res[1] = max(triplet[1], res[1])
            res[2] = max(triplet[2], res[2])

        return res == target