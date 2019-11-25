
from functools import lru_cache
def solve(X, Y, tx, ty):
    @lru_cache(None)
    def dfs(x, y, i):
        if i == len(tx):
            return 0

        if x == 0:
            return sum(ty[i:])
        elif y == 0:
            return sum(tx[i:])

        return max(tx[i]+dfs(x-1, y, i+1), ty[i] + dfs(x, y-1, i+1))

    return dfs(X, Y, 0)


for _ in range(int(input())):
    _, X, Y = map(int, input().split())
    tx = list(map(int, input().split()))
    ty = list(map(int, input().split()))
    print(solve(X, Y, tx, ty))
