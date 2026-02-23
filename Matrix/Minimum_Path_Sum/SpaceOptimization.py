```python
class SpaceOptimizedSolution:
    def minPathSum(self, grid):
        m = len(grid)
        n = len(grid[0])
        prev_row = [0] * n
        prev_row[0] = grid[0][0]
        # First row
        for j in range(1, n):
            prev_row[j] = prev_row[j - 1] + grid[0][j]
        for i in range(1, m):
            current_row = [0] * n
            current_row[0] = prev_row[0] + grid[i][0]
            for j in range(1, n):
                current_row[j] = grid[i][j] + min(
                    prev_row[j],        # from top
                    current_row[j - 1]  # from left
                )
            prev_row = current_row
        return prev_row[n - 1]
```
