import collections

def solve(links):
    graph = collections.defaultdict(list)
    starts = set()
    follow = set()
    for s, e in links:
        graph[s].append(e)
        starts.add(s)
        follow.add(e)
    starts -= follow

    def dfs(node):
        if not graph[node]:
            return 1

        ans = 0
        for nx in graph[node]:
            ans += dfs(nx)
        return ans
    return sum(dfs(node) for node in starts)


for _ in range(int(input())):
    links = [pair.split() for pair in input().split(',')]
    print(solve(links))
