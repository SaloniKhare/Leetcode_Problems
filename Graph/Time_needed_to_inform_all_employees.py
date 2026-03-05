# ============================================================
# TIME NEEDED TO INFORM ALL EMPLOYEES - ALL APPROACHES
# ============================================================

# Problem:
# n employees numbered 0 to n-1
# headID = company head
# manager[i] = direct manager of employee i
# informTime[i] = time taken by employee i to inform subordinates
#
# Return total time needed to inform all employees.


# ------------------------------------------------------------
# 1️⃣ DFS Recursion (Build Tree First)
# ------------------------------------------------------------

from collections import defaultdict

class DFSRecursionSolution:
    def numOfMinutes(self, n, headID, manager, informTime):
        tree = defaultdict(list)

        for emp in range(n):
            if manager[emp] != -1:
                tree[manager[emp]].append(emp)

        def dfs(node):
            max_time = 0
            for child in tree[node]:
                max_time = max(max_time, dfs(child))
            return informTime[node] + max_time

        return dfs(headID)


# ------------------------------------------------------------
# 2️⃣ DFS + Memoization
# ------------------------------------------------------------

class DFSMemoSolution:
    def numOfMinutes(self, n, headID, manager, informTime):
        memo = {}

        def dfs(emp):
            if manager[emp] == -1:
                return 0

            if emp in memo:
                return memo[emp]

            memo[emp] = informTime[manager[emp]] + dfs(manager[emp])
            return memo[emp]

        return max(dfs(i) for i in range(n))


# ------------------------------------------------------------
# 3️⃣ BFS (Level Order Traversal)
# ------------------------------------------------------------

from collections import deque

class BFSSolution:
    def numOfMinutes(self, n, headID, manager, informTime):
        tree = defaultdict(list)

        for i in range(n):
            if manager[i] != -1:
                tree[manager[i]].append(i)

        queue = deque([(headID, 0)])
        max_time = 0

        while queue:
            node, time = queue.popleft()
            max_time = max(max_time, time)

            for child in tree[node]:
                queue.append((child, time + informTime[node]))

        return max_time


# ------------------------------------------------------------
# 4️⃣ DFS Iterative (Stack Based)
# ------------------------------------------------------------

class DFSIterativeSolution:
    def numOfMinutes(self, n, headID, manager, informTime):
        tree = defaultdict(list)

        for i in range(n):
            if manager[i] != -1:
                tree[manager[i]].append(i)

        stack = [(headID, 0)]
        max_time = 0

        while stack:
            node, time = stack.pop()
            max_time = max(max_time, time)

            for child in tree[node]:
                stack.append((child, time + informTime[node]))

        return max_time


# ------------------------------------------------------------
# 5️⃣ Bottom-Up Approach (Follow Manager Chain)
# ------------------------------------------------------------

class BottomUpSolution:
    def numOfMinutes(self, n, headID, manager, informTime):
        memo = [0] * n

        def dfs(i):
            if manager[i] == -1:
                return 0

            if memo[i] != 0:
                return memo[i]

            memo[i] = informTime[manager[i]] + dfs(manager[i])
            return memo[i]

        ans = 0
        for i in range(n):
            ans = max(ans, dfs(i))

        return ans
