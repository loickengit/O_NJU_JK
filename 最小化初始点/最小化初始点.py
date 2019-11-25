
def solve(grid):
    m, n = len(grid), len(grid[0])
    dp = [[float('inf')]*(n+1) for _ in range(m+1)]
    dp[m-1][n-1] = max(-grid[-1][-1], 0) + 1

    for i in range(m)[::-1]:
        for j in range(n)[::-1]:
            if i == m-1 and j == n-1:
                continue
            best_exit = min(dp[i+1][j], dp[i][j+1])
            dp[i][j] = max(best_exit-grid[i][j], 1)
    return dp[0][0]


for _ in range(int(input())):
    r, c = map(int, input().split())
    ins = list(map(int, input().split()))
    nums = [ins[i:i+r] for i in range(0, r*c, r)]
    print(solve(nums))