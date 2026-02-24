``` python
class SpaceOptimizedSolution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        if obstacleGrid[0][0] == 1:
            return 0
        prev_row = [0] * n
        prev_row[0] = 1
        for i in range(m):
            current_row = [0] * n
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    current_row[j] = 0
                else:
                    if i == 0 and j == 0:
                        current_row[j] = 1
                    else:
                        from_top = prev_row[j] if i > 0 else 0
                        from_left = current_row[j - 1] if j > 0 else 0
                        current_row[j] = from_top + from_left
            prev_row = current_row
        return prev_row[n - 1]
```
