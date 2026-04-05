# ======================================================
# COUNT AND SAY - ALL APPROACHES
# ======================================================

# Problem (LeetCode 38):
# The count-and-say sequence is a sequence of digit strings:
#
# 1
# 11       ("one 1")
# 21       ("two 1s")
# 1211     ("one 2, one 1")
# 111221   ("one 1, one 2, two 1s")
#
# Given n, return the nth term.
#
# Example:
# Input: n = 4
# Output: "1211"


# ------------------------------------------------------
# 1️⃣ Brute Force (Build Step by Step)
# ------------------------------------------------------

class BruteForceSolution:
    def countAndSay(self, n):

        result = "1"

        for _ in range(n - 1):

            temp = ""
            i = 0

            while i < len(result):

                count = 1

                while i + 1 < len(result) and result[i] == result[i + 1]:
                    i += 1
                    count += 1

                temp += str(count) + result[i]
                i += 1

            result = temp

        return result


# ------------------------------------------------------
# 2️⃣ Two Pointer Approach ⭐ MOST IMPORTANT
# ------------------------------------------------------

class OptimalSolution:
    def countAndSay(self, n):

        s = "1"

        for _ in range(n - 1):

            i = 0
            new_s = ""

            while i < len(s):

                j = i

                while j < len(s) and s[j] == s[i]:
                    j += 1

                new_s += str(j - i) + s[i]
                i = j

            s = new_s

        return s


# ------------------------------------------------------
# 3️⃣ Recursive Approach
# ------------------------------------------------------

class RecursiveSolution:
    def countAndSay(self, n):

        if n == 1:
            return "1"

        prev = self.countAndSay(n - 1)

        i = 0
        result = ""

        while i < len(prev):

            count = 1

            while i + 1 < len(prev) and prev[i] == prev[i + 1]:
                i += 1
                count += 1

            result += str(count) + prev[i]
            i += 1

        return result


# ------------------------------------------------------
# 4️⃣ Using GroupBy (Pythonic)
# ------------------------------------------------------

from itertools import groupby

class GroupBySolution:
    def countAndSay(self, n):

        s = "1"

        for _ in range(n - 1):
            s = ''.join(str(len(list(group))) + digit for digit, group in groupby(s))

        return s


# ------------------------------------------------------
# 5️⃣ Queue-Based Approach
# ------------------------------------------------------

from collections import deque

class QueueSolution:
    def countAndSay(self, n):

        queue = deque(["1"])

        for _ in range(n - 1):

            curr = queue.popleft()
            i = 0
            result = ""

            while i < len(curr):

                count = 1

                while i + 1 < len(curr) and curr[i] == curr[i + 1]:
                    i += 1
                    count += 1

                result += str(count) + curr[i]
                i += 1

            queue.append(result)

        return queue[0]


# ------------------------------------------------------
# Example
# ------------------------------------------------------

n = 5

print("BruteForce:", BruteForceSolution().countAndSay(n))
print("Optimal:", OptimalSolution().countAndSay(n))
print("Recursive:", RecursiveSolution().countAndSay(n))
print("GroupBy:", GroupBySolution().countAndSay(n))
print("Queue:", QueueSolution().countAndSay(n))
