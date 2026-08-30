import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        dic = {}
        task = []
        time = 0

        for i in tasks:
            dic[i] = 1 + dic.get(i, 0)

        max_heap = [-freq for freq in dic.values()]
        heapq.heapify(max_heap)

        while max_heap:

            temp = []

            for _ in range(n+1):

                if max_heap:
                    freq = heapq.heappop(max_heap)
                    freq += 1

                    if freq < 0:
                        temp.append(freq)
                
                time += 1 

                if not max_heap and not temp:
                    break

            for freq in temp:
                heapq.heappush(max_heap, freq)

        return time





        