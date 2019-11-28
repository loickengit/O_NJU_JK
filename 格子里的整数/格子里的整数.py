

def solve(grid):
    m, n = len(grid), len(grid[0])
    mindis = [[float('inf')]*n for _ in range(m)]
    def dfs(i, j, cur):
        for x, y in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
            if 0 <= x < m and 0 <= y < n and mindis[x][y] > cur + grid[x][y]:
                mindis[x][y] = cur + grid[x][y]
                dfs(x, y, cur + grid[x][y])
    dfs(0, 0, grid[0][0])
    return mindis[-1][-1]

        


for _ in range(int(input())):
    n = int(input())
    nums = list(map(int, input().split()))
    grid = [nums[i:i+n] for i in range(0, len(nums), n)]
    print()
    print(solve(grid))


    
    
            