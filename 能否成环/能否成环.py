import collections

def solve(nodes):
    N = len(nodes)
    follow = collections.defaultdict(list)
    for node in nodes:
        for f in nodes:
            if node[-1] == f[0]:
                follow[node].append(f)

    def dfs(path):
        if len(path) == N:
            return path[-1][-1] == path[0][0]

        for node in follow[path[-1]]:
            if node not in path and dfs(path+[node]):
                return True
        return False

    return any(dfs([node]) for node in nodes)


for _ in range(int(input())):
    input()
    nodes = input().split()
    print(int(solve(nodes)))