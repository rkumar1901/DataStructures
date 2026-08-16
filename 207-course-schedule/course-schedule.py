from collections import defaultdict
class Solution:
    def canFinish(self, numCourses, prerequisites):
        
        preMap = defaultdict(list)
        visited = set()
        for i in prerequisites:
            crs, preq = i
            preMap[preq].append(crs)

        def dfs(crs):
            if crs in visited:
                return False
            if not preMap[crs]:
                return True         

            visited.add(crs)
            for adj_crs in preMap[crs]:
                if not dfs(adj_crs):
                    return False

            visited.remove(crs)
            preMap[crs] = []
            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True


        