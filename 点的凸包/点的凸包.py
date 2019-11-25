class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Solution:
    def outerTrees(self, points):
        points = sorted(points, key=lambda p: (p.x, p.y))
        if len(points) <= 2:
            return points

        def cross(o, a, b):
            return (a.x - o.x) * (b.y - o.y) - (a.y - o.y) * (b.x - o.x)

        lower = []
        for p in points:
            while len(lower) >= 2 and cross(lower[-2], lower[-1], p) < 0:
                lower.pop()
            lower.append(p)

        upper = []
        for p in reversed(points):
            while len(upper) >= 2 and cross(upper[-2], upper[-1], p) < 0:
                upper.pop()
            upper.append(p)

        return list(set(lower[:-1] + upper[:-1]))


for _ in range(int(input())):
    input()
    nums = input().split()
    nums = [int(num) if float(num).is_integer() else float(num) for num in nums]
    points = [Point(*nums[i:i+2]) for i in range(0, len(nums), 2)]
    points = list(set(points))
    res = Solution().outerTrees(points)
    res.sort(key=lambda p: (p.x, p.y))
    if len(res) < 3:
        print(-1)
        continue
    out = ', '.join(' '.join(map(str, [p.x, p.y])) for p in res)
    print(out)