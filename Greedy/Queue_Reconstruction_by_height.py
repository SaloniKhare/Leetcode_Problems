# ============================================================
# QUEUE RECONSTRUCTION BY HEIGHT - ALL APPROACHES
# ============================================================

# Problem:
# people[i] = [height, k]
#
# height = person's height
# k = number of people in front who have height >= height
#
# Reconstruct the queue.


# ------------------------------------------------------------
# 1️⃣ Greedy + Sorting + Insert (Optimal & Most Expected)
# ------------------------------------------------------------

class GreedySolution:
    def reconstructQueue(self, people):
        # Step 1: Sort
        people.sort(key=lambda x: (-x[0], x[1]))

        queue = []

        # Step 2: Insert at index k
        for h, k in people:
            queue.insert(k, [h, k])

        return queue


# ------------------------------------------------------------
# 2️⃣ Greedy + List Insertion (Same Idea Explicit)
# ------------------------------------------------------------

class GreedySimpleSolution:
    def reconstructQueue(self, people):
        people = sorted(people, key=lambda x: (-x[0], x[1]))

        result = []

        for person in people:
            result.insert(person[1], person)

        return result


# ------------------------------------------------------------
# 3️⃣ Simulation Approach (Slower)
# ------------------------------------------------------------

class SimulationSolution:
    def reconstructQueue(self, people):
        n = len(people)
        result = [None] * n

        # Sort by height ascending
        people.sort(key=lambda x: (x[0], -x[1]))

        for h, k in people:
            spaces = k + 1

            for i in range(n):
                if result[i] is None:
                    spaces -= 1

                    if spaces == 0:
                        result[i] = [h, k]
                        break

        return result


# ------------------------------------------------------------
# 4️⃣ Fenwick Tree / BIT (Advanced Approach)
# ------------------------------------------------------------

class FenwickSolution:
    def reconstructQueue(self, people):
        n = len(people)

        people.sort(key=lambda x: (x[0], -x[1]))

        tree = [0]*(n+1)

        def update(i, val):
            while i <= n:
                tree[i] += val
                i += i & -i

        def query(i):
            s = 0
            while i > 0:
                s += tree[i]
                i -= i & -i
            return s

        for i in range(1, n+1):
            update(i, 1)

        result = [None]*n

        for h, k in people:
            left, right = 1, n
            target = k + 1

            while left < right:
                mid = (left + right)//2
                if query(mid) >= target:
                    right = mid
                else:
                    left = mid + 1

            result[left-1] = [h,k]
            update(left, -1)

        return result
