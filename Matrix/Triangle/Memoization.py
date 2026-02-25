``` python
class MemoizationSolution:
    def minimumTotal(self, triangle):
        n = len(triangle)
        memo = {}
        def helper(i, j):
            if i == n - 1:
                return triangle[i][j]            
            if (i, j) in memo:
                return memo[(i, j)]
            down = helper(i + 1, j)
            diagonal = helper(i + 1, j + 1)
            memo[(i, j)] = triangle[i][j] + min(down, diagonal)
            return memo[(i, j)]
        return helper(0, 0)
```
