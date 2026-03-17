# ======================================================
# MAXIMUM UNITS ON A TRUCK - ALL APPROACHES
# ======================================================

# Problem (LeetCode 1710):
# You are given boxTypes where:
# boxTypes[i] = [numberOfBoxes, unitsPerBox]
# and an integer truckSize (max boxes you can carry).
#
# Return the maximum total units you can put on the truck.


# ------------------------------------------------------
# 1️⃣ Brute Force (Expand All Boxes)
# ------------------------------------------------------

class BruteForceSolution:
    def maximumUnits(self, boxTypes, truckSize):

        boxes = []

        # Expand each box
        for count, units in boxTypes:
            boxes.extend([units] * count)

        boxes.sort(reverse=True)

        return sum(boxes[:truckSize])


# ------------------------------------------------------
# 2️⃣ Sorting + Greedy (Optimal)
# ------------------------------------------------------

class GreedySolution:
    def maximumUnits(self, boxTypes, truckSize):

        # Sort by units per box (descending)
        boxTypes.sort(key=lambda x: x[1], reverse=True)

        total_units = 0

        for count, units in boxTypes:

            if truckSize == 0:
                break

            take = min(count, truckSize)

            total_units += take * units
            truckSize -= take

        return total_units


# ------------------------------------------------------
# 3️⃣ Max Heap Approach
# ------------------------------------------------------

import heapq

class HeapSolution:
    def maximumUnits(self, boxTypes, truckSize):

        # Max heap based on units per box
        max_heap = [(-units, count) for count, units in boxTypes]
        heapq.heapify(max_heap)

        total_units = 0

        while max_heap and truckSize > 0:

            units, count = heapq.heappop(max_heap)
            units = -units

            take = min(count, truckSize)

            total_units += take * units
            truckSize -= take

        return total_units

