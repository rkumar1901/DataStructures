from collections import defaultdict, deque
class Solution:

    def canFinish(self, numCourses, prerequisites):
        
        graph = [[] for i in range(numCourses)]
        preq_count = [0] * numCourses
        completed = 0
        queue = deque()

        for crs, preq in prerequisites:
            graph[preq].append(crs)
            preq_count[crs] += 1

        for i in range(len(preq_count)):
            if preq_count[i] == 0:
                queue.append(i)

        while queue:

            crs = queue.popleft()
            completed += 1

            for next_crs in graph[crs]:
                preq_count[next_crs] -= 1

                if preq_count[next_crs] == 0:
                    queue.append(next_crs)


        return completed == numCourses

        

     


# BFS SOLUTION:
# class Solution(object):
#     def canFinish(self, numCourses, prerequisites):

#         graph = [[] for _ in range(numCourses)]
#         prereq_count = [0] * numCourses

#         # Build graph
#         for course, prerequisite in prerequisites:
#             graph[prerequisite].append(course)
#             prereq_count[course] += 1

#         # Courses with no prerequisites
#         queue = deque()

#         for course in range(numCourses):
#             if prereq_count[course] == 0:
#                 queue.append(course)

#         completed = 0

#         # BFS
#         while queue:
#             course = queue.popleft()
#             completed += 1

#             # Remove this course as a prerequisite
#             for next_course in graph[course]:
#                 prereq_count[next_course] -= 1

#                 if prereq_count[next_course] == 0:
#                     queue.append(next_course)

#         return completed == numCourses


        