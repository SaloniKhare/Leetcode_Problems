# ======================================================
# PARTITION LABELS - ALL APPROACHES
# ======================================================

# Problem:
# Given a string s, partition it into as many parts as possible
# so that each letter appears in at most one part.
# Return a list of the sizes of these parts.


# ------------------------------------------------------
# 1️⃣ Brute Force
# ------------------------------------------------------

class BruteForceSolution:
    def partitionLabels(self, s: str):
        n = len(s)
        result = []

        start = 0
        while start < n:
            end = start
            for i in range(start, n):
                for j in range(i + 1, n):
                    if s[i] == s[j]:
                        end = max(end, j)
            result.append(end - start + 1)
            start = end + 1

        return result


# ------------------------------------------------------
# 2️⃣ Using Character Last Occurrence Map
# ------------------------------------------------------

class MapSolution:
    def partitionLabels(self, s: str):
        last = {}

        # store last occurrence
        for i, ch in enumerate(s):
            last[ch] = i

        result = []
        start = 0
        end = 0

        for i, ch in enumerate(s):
            end = max(end, last[ch])

            if i == end:
                result.append(end - start + 1)
                start = i + 1

        return result


# ------------------------------------------------------
# 3️⃣ Greedy (Optimal Solution) ⭐
# ------------------------------------------------------

class GreedySolution:
    def partitionLabels(self, s: str):
        last = {c: i for i, c in enumerate(s)}

        res = []
        start = 0
        end = 0

        for i in range(len(s)):
            end = max(end, last[s[i]])

            if i == end:
                res.append(end - start + 1)
                start = i + 1

        return res


# ------------------------------------------------------
# 4️⃣ Stack Approach
# ------------------------------------------------------

class StackSolution:
    def partitionLabels(self, s: str):
        last = {c: i for i, c in enumerate(s)}

        stack = []
        start = 0
        end = 0

        for i, ch in enumerate(s):
            end = max(end, last[ch])

            if not stack:
                stack.append(i)

            if i == end:
                stack.pop()
                stack.append(end - start + 1)
                start = i + 1

        return stack
