class Solution(object):
    def carFleet(self, target, position, speed):

        res = []
        for r in range(len(position)):

            time = float(target - position[r]) / speed[r]
            res.append((position[r], time))

        res.sort(reverse=True)

        prev_time = 0
        car_fleet = 0
        for pos, time in res:

            if time > prev_time:
                car_fleet += 1
                prev_time = time

        return car_fleet



 