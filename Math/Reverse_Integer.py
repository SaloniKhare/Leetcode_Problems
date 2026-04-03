# ======================================================
# REVERSE INTEGER - ALL APPROACHES
# ======================================================

# Problem (LeetCode 7):
# Given a signed 32-bit integer x, return x with its digits reversed.
# If reversing x causes it to go outside the 32-bit signed integer range
# [-2^31, 2^31 - 1], return 0.
#
# Example:
# Input: x = 123
# Output: 321
#
# Input: x = -123
# Output: -321
#
# Input: x = 120
# Output: 21


# ------------------------------------------------------
# 1️⃣ Brute Force (String Reverse)
# ------------------------------------------------------

class BruteForceSolution:
    def reverse(self, x):

        sign = -1 if x < 0 else 1
        x = abs(x)

        rev = int(str(x)[::-1])

        rev *= sign

        # check 32-bit overflow
        if rev < -2**31 or rev > 2**31 - 1:
            return 0

        return rev


# ------------------------------------------------------
# 2️⃣ Math Approach (Most Important)
# ------------------------------------------------------

class OptimalSolution:
    def reverse(self, x):

        rev = 0

        while x != 0:

            digit = int(x % 10)

            # handle negative numbers correctly
            if x < 0 and digit > 0:
                digit -= 10

            x = (x - digit) // 10

            # overflow check BEFORE adding digit
            if rev > (2**31 - 1) // 10 or rev < (-2**31) // 10:
                return 0

            rev = rev * 10 + digit

        return rev


# ------------------------------------------------------
# 3️⃣ Clean Math Version
# ------------------------------------------------------

class CleanSolution:
    def reverse(self, x):

        sign = -1 if x < 0 else 1
        x = abs(x)

        rev = 0

        while x:

            digit = x % 10
            x //= 10

            if rev > (2**31 - 1) // 10:
                return 0

            rev = rev * 10 + digit

        return sign * rev


# ------------------------------------------------------
# 4️⃣ Using Stack
# ------------------------------------------------------

class StackSolution:
    def reverse(self, x):

        sign = -1 if x < 0 else 1
        x = abs(x)

        stack = []

        while x:
            stack.append(x % 10)
            x //= 10

        rev = 0
        place = 1

        for digit in stack[::-1]:
            rev += digit * place
            place *= 10

        rev *= sign

        if rev < -2**31 or rev > 2**31 - 1:
            return 0

        return rev


# ------------------------------------------------------
# 5️⃣ Pythonic One-Liner
# ------------------------------------------------------

class PythonicSolution:
    def reverse(self, x):

        sign = -1 if x < 0 else 1
        rev = int(str(abs(x))[::-1])

        return sign * rev if -2**31 <= sign * rev <= 2**31 - 1 else 0
