import collections


def solve(matrix, s):
    N = len(matrix)
    graph = [[] for _ in range(N)]
    for i in range(N):
        for j in range(i):
            if matrix[i][j] == 1:
                graph[i].append(j)
                graph[j].append(i)

    s = ord(s) - ord('a')
    q = collections.deque([s])
    res = []
    seen = {s}
    while q:
        node = q.popleft()
        res.append(node)
        for nx in graph[node]:
            if nx not in seen:
                q.append(nx)
                seen.add(nx)
    return [chr(ord('a') + k) for k in res]


for _ in range(int(input())):
    lines, s = input().split()
    matrix = []
    input()
    for _ in range(int(lines)):
        matrix.append(list(map(int, input().split()[1:])))
    res = solve(matrix, s)
    print(' '.join(res))