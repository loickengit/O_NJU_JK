import collections


def solve(points):
    def count(items):
        c = collections.Counter(items)
        return sum(n*(n-1)//2 for n in c.values())

    xs, ys = list(zip(*points))
    tpoints = [tuple(p) for p in points]
    return count(xs) + count(ys) - count(tpoints)


for _ in range(int(input())):
    n = int(input())
    points = [list(map(int, input().split())) for _ in range(n)]
    print(solve(points))