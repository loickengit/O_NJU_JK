
import collections
def solve(points):

    def dis2(p1, p2):
        return (float(p2[0]) - float(p[0])) ** 2 + (float(p2[1]) - float(p[1])) ** 2

    ans = collections.defaultdict(list)
    for i in range(len(points)-1):
        p = points[i]
        cur, d = [(p, points[i+1])], dis2(p, points[i+1])
        for j in range(i+2, len(points)):
            dj = dis2(p, points[j])
            if dj < d:
                cur = [(p, points[j])]
                d = dj
            elif dj == d:
                cur.append((p, points[j]))
        ans[d] += cur

    return ans[min(ans.keys())]


for _ in range(int(input())):
    points = [p.split() for p in input().split(',')]
    res = solve(points)
    res = [','.join(' '.join(p) for p in sorted(pair)) for pair in res]
    print(','.join(sorted(res)))