# ============================================================
# NUMBER OF LONGEST INCREASING SUBSEQUENCES
# ============================================================

# Problem:
# Given an integer array nums,
# return the number of longest increasing subsequences.


# ------------------------------------------------------------
# 1️⃣ Dynamic Programming O(n²) (Standard Interview Solution)
# ------------------------------------------------------------

class DPSolution:
    def findNumberOfLIS(self, nums):
        n = len(nums)

        # length[i] = LIS ending at i
        length = [1] * n
        
        # count[i] = number of LIS ending at i
        count = [1] * n

        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:

                    # Found longer subsequence
                    if length[j] + 1 > length[i]:
                        length[i] = length[j] + 1
                        count[i] = count[j]

                    # Found another subsequence of same length
                    elif length[j] + 1 == length[i]:
                        count[i] += count[j]

        max_len = max(length)

        result = 0
        for i in range(n):
            if length[i] == max_len:
                result += count[i]

        return result
