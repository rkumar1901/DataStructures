from collections import defaultdict
class Solution:

    def canFinish(self, numCourses, prerequisites):
        preMap = defaultdict(list)
        visited = set()
        completed = set()

        for crs, preq in prerequisites:
            preMap[crs].append(preq)

        def dfs(crs):
            if crs in visited:
                return False 
            if crs in completed:
                return True

            visited.add(crs)

            for adj_crs in preMap[crs]:
                if not dfs(adj_crs):
                    return False

            visited.remove(crs)
            completed.add(crs)
            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return False

        return True 


        