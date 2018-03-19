

def getBiggestRegion(grid):
    maxRegion = 0

    def dfs(i, j):
        if i < 0 or j < 0 or i + 1 > len(grid) or j +1 > len(grid[i]) or grid[i][j] == 0:
            return 0
        grid[i][j] = 0
        return (dfs(i-1, j-1) + dfs(i-1, j) + dfs(i-1, j+1)
                + dfs(i, j-1) + dfs(i, j+1)
                + dfs(i + 1, j - 1) + dfs(i + 1, j) + dfs(i + 1, j + 1)) + 1

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                maxRegion = max(dfs(i, j), maxRegion)
    return maxRegion


n = int(input().strip())
m = int(input().strip())
grid = []
for grid_i in range(n):
    grid_t = list(map(int, input().strip().split(' ')))
    grid.append(grid_t)
print(getBiggestRegion(grid))
