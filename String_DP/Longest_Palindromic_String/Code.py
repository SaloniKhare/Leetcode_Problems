# ==================================================
# LONGEST PALINDROMIC SUBSTRING - ALL APPROACHES
# ==================================================

# Problem:
# Given a string s, return the longest palindromic substring in s.


# -------------------------------------------------
# 1️⃣ Brute Force
# -------------------------------------------------
class BruteForceSolution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        longest = ""

        def is_palindrome(sub):
            return sub == sub[::-1]

        for i in range(n):
            for j in range(i, n):
                substring = s[i:j+1]
                if is_palindrome(substring) and len(substring) > len(longest):
                    longest = substring

        return longest


# -------------------------------------------------
# 2️⃣ Recursion (Check All Substrings)
# -------------------------------------------------
class RecursionSolution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        longest = ""

        def is_palindrome(left, right):
            if left >= right:
                return True
            if s[left] != s[right]:
                return False
            return is_palindrome(left + 1, right - 1)

        for i in range(n):
            for j in range(i, n):
                if is_palindrome(i, j) and (j - i + 1) > len(longest):
                    longest = s[i:j+1]

        return longest


# -------------------------------------------------
# 3️⃣ DP - Memoization (Top Down)
# -------------------------------------------------
class MemoizationSolution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        memo = {}
        start = 0
        max_len = 1

        def is_palindrome(i, j):
            if i >= j:
                return True
            if (i, j) in memo:
                return memo[(i, j)]
            if s[i] == s[j]:
                memo[(i, j)] = is_palindrome(i + 1, j - 1)
            else:
                memo[(i, j)] = False
            return memo[(i, j)]

        for i in range(n):
            for j in range(i, n):
                if is_palindrome(i, j) and (j - i + 1) > max_len:
                    start = i
                    max_len = j - i + 1

        return s[start:start + max_len]


# -------------------------------------------------
# 4️⃣ DP - Tabulation (Bottom Up)
# -------------------------------------------------
class TabulationSolution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        start = 0
        max_len = 1

        for i in range(n):
            dp[i][i] = True

        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1

                if s[i] == s[j]:
                    if length == 2:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i + 1][j - 1]
                else:
                    dp[i][j] = False

                if dp[i][j] and length > max_len:
                    start = i
                    max_len = length

        return s[start:start + max_len]


# -------------------------------------------------
# 5️⃣ Two Pointer - Expand Around Center (Optimal)
# -------------------------------------------------
class TwoPointerSolution:
    def longestPalindrome(self, s: str) -> str:
        start = 0
        end = 0

        def expand(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return right - left - 1  # length

        for i in range(len(s)):
            len1 = expand(i, i)       # odd length
            len2 = expand(i, i + 1)   # even length
            max_len = max(len1, len2)

            if max_len > end - start:
                start = i - (max_len - 1) // 2
                end = i + max_len // 2

        return s[start:end + 1]

"""📊 Complexity Comparison
Approach	Time	Space
Brute Force	O(n³)	O(1)
Recursion	O(n³)	O(n) stack
Memoization	O(n²)	O(n²)
Tabulation	O(n²)	O(n²)
Two Pointer	O(n²)	O(1)"""
