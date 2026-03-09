# ======================================================
# MINIMUM NUMBER OF ARROWS TO BURST BALLOONS
# ======================================================

# Problem:
# points[i] = [start, end] of a balloon
# An arrow shot at position x bursts all balloons
# where start <= x <= end.
# Return the minimum number of arrows needed.


# ------------------------------------------------------
# 1️⃣ Brute Force (Check all overlaps)
# ------------------------------------------------------

class BruteForceSolution:
    def findMinArrowShots(self, points):
        if not points:
            return 0

        points.sort()
        arrows = 0

        while points:
            start, end = points[0]
            arrows += 1
            new_points = []

            for s, e in points:
                if s > end or e < start:
                    new_points.append([s, e])
                else:
                    start = max(start, s)
                    end = min(end, e)

            points = new_points

        return arrows


# ------------------------------------------------------
# 2️⃣ Greedy (Sort by End) ⭐ Optimal
# ------------------------------------------------------

class GreedySolution:
    def findMinArrowShots(self, points):
        if not points:
            return 0

        points.sort(key=lambda x: x[1])

        arrows = 1
        arrow_pos = points[0][1]

        for start, end in points:
            if start > arrow_pos:
                arrows += 1
                arrow_pos = end

        return arrows


# ------------------------------------------------------
# 3️⃣ Greedy (Sort by Start + Merge)
# ------------------------------------------------------

class GreedyMergeSolution:
    def findMinArrowShots(self, points):
        if not points:
            return 0

        points.sort()
        arrows = 1
        curr_end = points[0][1]

        for start, end in points[1:]:
            if start <= curr_end:
                curr_end = min(curr_end, end)
            else:
                arrows += 1
                curr_end = end

        return arrows


# ------------------------------------------------------
# 4️⃣ Dynamic Programming (Interval Style)
# ------------------------------------------------------

class DPSolution:
    def findMinArrowShots(self, points):
        points.sort()
        n = len(points)

        dp = [1] * n

        for i in range(n):
            for j in range(i):
                if points[j][1] >= points[i][0]:
                    dp[i] = min(dp[i], dp[j])
                else:
                    dp[i] = min(dp[i], dp[j] + 1)

        return dp[-1]
