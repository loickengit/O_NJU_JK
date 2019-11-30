

def solve(matrix, s):
    N = len(matrix)
    graph = [[] for _ in range(N)]
    for i in range(N):
        for j in range(i):
            if matrix[i][j] == 1:
                graph[i].append(j)
                graph[j].append(i)

    dis = [-1] * N
    s = ord(s) - ord('a')
    dis[s] = 1

    def dfs(path):
        for nx in graph[path[-1]]:
            if nx not in path and len(path)+1 > dis[nx]:
                dis[nx] = len(path) + 1
                dfs(path + [nx])

    dfs([s])
    return max(dis)

for _ in range(int(input())):
    lines, s = input().split()
    matrix = []
    input()
    for _ in range(int(lines)):
        matrix.append(list(map(int, input().split()[1:])))
    print(solve(matrix, s))