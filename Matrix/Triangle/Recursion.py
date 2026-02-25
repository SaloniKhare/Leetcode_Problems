``` python
class RecursionSolution:
    def minimumTotal(self, triangle):
        n = len(triangle)
        def helper(i, j):
            # Base case: last row
            if i == n - 1:
                return triangle[i][j]
            down = helper(i + 1, j)
            diagonal = helper(i + 1, j + 1)
            return triangle[i][j] + min(down, diagonal)
        return helper(0, 0)
```
