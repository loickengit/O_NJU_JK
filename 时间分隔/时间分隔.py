def solve(starts, ends):
    events = [(s, 1) for s in starts] + [(e, -1) for e in ends]
    events.sort()
    ans = cur = 0
    for e in events:
        cur += e[1]
        ans = max(ans, cur)
    return ans


for _ in range(int(input())):
    input()
    starts = list(map(int, input().split()))
    ends = list(map(int, input().split()))
    print(solve(starts, ends))