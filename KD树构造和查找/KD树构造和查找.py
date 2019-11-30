

def solve(points, tar, k):
    points.sort(key=lambda p: (p[0]-tar[0])**2 + (p[1]-tar[1])**2)
    return points[:k]


for _ in range(int(input())):
    points = []
    for p in input().split(','):
        x, y = map(float, p.split())
        x = int(x) if x.is_integer() else x
        y = int(y) if y.is_integer() else y
        points.append((x, y))

    tar = tuple(map(float, input().split()))
    k = int(input())
    res = solve(points, tar, k)

    out = ','.join(' '.join(map(str, point)) for point in res)
    print(out)