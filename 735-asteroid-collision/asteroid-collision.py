class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        
        res = []
        for r in range(len(asteroids)):
            append = True

            while res and res[-1] > 0 and asteroids[r] < 0:

                if abs(res[-1]) < abs(asteroids[r]):
                    res.pop()

                elif  abs(res[-1]) == abs(asteroids[r]):
                    res.pop()
                    append=False
                    break

                else:
                    append = False
                    break

            if append:
                res.append(asteroids[r])

        return res
        