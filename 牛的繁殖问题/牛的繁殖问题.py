memo = {}
mod = 10**9+7


def getMatrix(k):
    if k in memo:
        return memo[k]
    if k == 1:
        return [[0, 1], [1, 1]]
    h1, h2 = getMatrix((k + 1) // 2), getMatrix(k // 2)
    x1, y1 = h1[0][0] * h2[0][0] + h1[0][1] * h2[1][0], h1[0][0] * h2[0][1] + h1[0][1] * h2[1][1]
    x2, y2 = h1[1][0] * h2[0][0] + h1[1][1] * h2[1][0], h1[1][0] * h2[0][1] + h1[1][1] * h2[1][1]
    res = [[x1 % mod, y1 % mod], [x2 % mod, y2 % mod]]
    memo[k] = res
    return res


def solve(n):
    if n == 1:
        return 1
    matrix = getMatrix(n-1)
    return (matrix[0][1] + matrix[1][1]) % (10**9 + 7)


for _ in range(int(input())):
    print(solve(int(input())))