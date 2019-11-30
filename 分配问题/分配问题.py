import itertools

def solve(matrix):
    n = len(matrix)
    ans = float('inf')
    res = []
    for combi in itertools.permutations(range(n), n):
        cur = sum(matrix[i][j] for i, j in zip(range(n), combi))
        if cur < ans:
            res = [combi]
            ans = cur
        elif cur == ans:
            res.append(combi)
    return res


for _ in range(int(input())):
    n = int(input())
    matrix = [[0]*n for _ in range(n)]
    for r, c, val in (map(int, entry.split()) for entry in input().split(',')):
        matrix[r-1][c-1] = val
    res = solve(matrix)
    res = [[val+1 for val in ans] for ans in res]
    out = [' '.join(map(str, ans)) for ans in res]
    out = ','.join(sorted(out, reverse=True))
    print(out)
