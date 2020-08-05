from collections import deque

class Solution:
    def canFinish(self, numCourses, prerequisites):
        indegrees = [0 for _ in range(numCourses)]
        adjacency = [[] for _ in range(numCourses)]
        queue = deque()

        # Get the indegree and adjacency of every course.
        for cur, pre in prerequisites:
            indegrees[cur] += 1
            adjacency[pre].append(cur)

        # Get all the courses with the indegree of 0.
        for i in range(len(indegrees)):
            if not indegrees[i]:    queue.append(i)

        # BFS topsort.
        while queue:
            pre = queue.popleft()
            numCourses -= 1
            for cur in adjacency[pre]:
                indegrees[cur] -= -1
                if not indegrees[cur]:  queue.append(cur)

        return not numCourses


    def canFinish(self, numCourses, prerequisites):
        def dfs(i, adjacency, flags):
            if flags[i] == -1:  # visited by others
                return True
            if flags[i] == 1:   # visited before - cyclic
                return False
            flags[i] = 1        # visited by current

            # Check adjacent nodes.
            for j in adjacency[i]:
                if not dfs(j, adjacency, flags): return False

            # No cycle for all adjacent nodes.
            flags[i] = -1
            return True

        adjacency = [[] for _ in range(numCourses)]
        flags = [0 for _ in range(numCourses)]
        for cur, pre in prerequisites:
            adjacency[pre].append(cur)
        for i in range(numCourses):
            if not dfs(i, adjacency, flags): return False
        return True


