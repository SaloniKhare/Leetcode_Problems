# ======================================================
# NON-OVERLAPPING INTERVALS - ALL APPROACHES
# ======================================================

# Problem (LeetCode 435):
# Given an array of intervals, return the minimum number of
# intervals you need to remove to make the rest non-overlapping.


# ------------------------------------------------------
# 1️⃣ Brute Force (Try all removals)
# ------------------------------------------------------

class BruteForceSolution:
    def eraseOverlapIntervals(self, intervals):

        intervals.sort()
        n = len(intervals)

        def is_non_overlapping(arr):
            for i in range(1, len(arr)):
                if arr[i][0] < arr[i-1][1]:
                    return False
            return True

        def backtrack(idx, curr):
            if idx == n:
                if is_non_overlapping(curr):
                    return len(curr)
                return 0

            # include
            include = backtrack(idx + 1, curr + [intervals[idx]])

            # exclude
            exclude = backtrack(idx + 1, curr)

            return max(include, exclude)

        max_keep = backtrack(0, [])
        return n - max_keep


# ------------------------------------------------------
# 2️⃣ Dynamic Programming (LIS Style)
# ------------------------------------------------------

class DPSolution:
    def eraseOverlapIntervals(self, intervals):

        intervals.sort()
        n = len(intervals)

        dp = [1] * n

        for i in range(n):
            for j in range(i):
                if intervals[j][1] <= intervals[i][0]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return n - max(dp)


# ------------------------------------------------------
# 3️⃣ Greedy (Optimal - Sort by End Time)
# ------------------------------------------------------

class GreedySolution:
    def eraseOverlapIntervals(self, intervals):

        intervals.sort(key=lambda x: x[1])

        end = float('-inf')
        count = 0

        for start, finish in intervals:

            if start >= end:
                end = finish
            else:
                count += 1

        return count


# ------------------------------------------------------
# 4️⃣ Greedy (Sort by Start Time)
# ------------------------------------------------------

class GreedyAltSolution:
    def eraseOverlapIntervals(self, intervals):

        intervals.sort()

        prev_end = intervals[0][1]
        count = 0

        for i in range(1, len(intervals)):

            if intervals[i][0] < prev_end:
                count += 1
                prev_end = min(prev_end, intervals[i][1])
            else:
                prev_end = intervals[i][1]

        return count
