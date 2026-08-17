from collections import defaultdict


class Solution:

  def findOrder(self, numCourses, prerequisites):
    preMap = defaultdict(list)
    visited = set()  # Active DFS path (cycle detection)
    completed = set()  # Fully processed nodes
    result = []

    # Map course -> list of its prerequisites
    for crs, preq in prerequisites:
      preMap[crs].append(preq)

    def dfs(crs):
      if crs in visited:
        return False  # Cycle detected
      if crs in completed:
        return True  # Already added to result

      visited.add(crs)

      for adj_crs in preMap[crs]:
        if not dfs(adj_crs):
          return False

      visited.remove(crs)
      completed.add(crs)

      result.append(crs)  # Added AFTER all prerequisites are added
      return True

    for crs in range(numCourses):
      if not dfs(crs):
        return []

    return result  # Already in correct order (no reversal needed)