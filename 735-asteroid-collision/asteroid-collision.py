class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:

        res = []

        for r in asteroids:
            append = True

            while res and res[-1] > 0 and r < 0:

                if res[-1] < abs(r):
                    res.pop()

                elif res[-1] == abs(r):
                    res.pop()
                    append = False
                    break

                else:
                    append = False
                    break
            
            if append:
                res.append(r)

        return res



        