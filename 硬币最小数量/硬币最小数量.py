import functools
def solve(coins, amount):
    @functools.lru_cache(None)
    def dp(i, amount):
        if amount == 0:
            return 0
        if i == 0:
            return [float('inf'), amount // coins[0]][amount % coins[0] == 0]

        ans = float('inf')
        for j in range(amount//coins[i] + 1):
            ans = min(ans, j + dp(i-1, amount-coins[i]*j))
        return ans

    res = dp(len(coins)-1, amount)
    return [res, -1][res == float('inf')]


for _ in range(int(input())):
    _, amount = map(int, input().split())
    coins = list(map(int, input().split()))
    print(solve(coins, amount))