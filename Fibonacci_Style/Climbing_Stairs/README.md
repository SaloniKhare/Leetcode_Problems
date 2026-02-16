# 🧩 Climbing Stairs

## 🔹 Platform
LeetCode

## 🔹 Problem Summary
Given `n` stairs, you can climb either 1 or 2 steps at a time.
Return the total number of distinct ways to reach the top.

---

# 🔎 Key Observation

To reach step `n`, you must have:
- Come from step `n-1` (1 step jump)
- Come from step `n-2` (2 step jump)

This forms a Fibonacci-like recurrence.

---

# 🧠 APPROACH 1: Pure Recursion (Brute Force)

## 💡 Idea
Try all possible ways:
- From step `n`, go to `n-1`
- From step `n`, go to `n-2`

## 🔁 Recurrence
ways(n) = ways(n-1) + ways(n-2)

## ❗ Problem
Many overlapping subproblems → exponential time.

## ⏱ Time Complexity
O(2^n)

## 🗂 Space Complexity
O(n) (recursion stack)

---

# 🧠 APPROACH 2: Recursion + Memoization (Top-Down DP)

## 💡 Idea
Store previously computed results to avoid recomputation.

## 🔹 State Definition
dp[n] = number of ways to reach step n

## 🔁 Recurrence
dp[n] = dp[n-1] + dp[n-2]

## ✅ Why It Works
Eliminates overlapping subproblems.

## ⏱ Time Complexity
O(n)

## 🗂 Space Complexity
O(n)

---

# 🧠 APPROACH 3: Bottom-Up DP (Tabulation)

## 💡 Idea
Build solution iteratively from base cases.

## 🔹 Base Cases
dp[1] = 1  
dp[2] = 2  

## 🔁 Transition
dp[i] = dp[i-1] + dp[i-2]

## ⏱ Time Complexity
O(n)

## 🗂 Space Complexity
O(n)

---

# 🧠 APPROACH 4: Space Optimized DP

## 💡 Idea
We only need last two values.

Use two variables:
prev1 → dp[i-1]  
prev2 → dp[i-2]

## ⏱ Time Complexity
O(n)

## 🗂 Space Complexity
O(1)

---

# 📊 Comparison Table

| Approach | Time | Space | Recommended? |
|----------|------|-------|--------------|
| Recursion | O(2^n) | O(n) | ❌ No |
| Memoization | O(n) | O(n) | ✅ Good |
| Tabulation | O(n) | O(n) | ✅ Better |
| Space Optimized | O(n) | O(1) | ⭐ Best for interviews |

---

# 🎯 Pattern Identified
1D DP  
Fibonacci Pattern  

---

# 🤖 Real World / ML Connection
- Sequence modeling
- Dynamic programming in Reinforcement Learning
- State transition modeling

---

# 📌 What I Learned
- How overlapping subproblems create exponential complexity
- Importance of state definition in DP
- Space optimization techniques
