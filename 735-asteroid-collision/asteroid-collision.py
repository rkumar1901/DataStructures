class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        
        temp = []
        

        for r in range(len(asteroids)):
            flag = True

            while temp and temp[-1] > 0 and asteroids[r] < 0:
                
                if temp[-1] > abs(asteroids[r]):
                    flag = False
                    break

                elif temp[-1] < abs(asteroids[r]):
                    temp.pop()

                else:
                    flag = False
                    temp.pop()
                    break

            if flag:
                temp.append(asteroids[r])

        return temp
        