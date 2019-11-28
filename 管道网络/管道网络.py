def solve(p, pairs):
    link, vals = {}, {}
    for pair in pairs:
        link[pair[0]] = pair[1]
        vals[(pair[0], pair[1])] = pair[2]
    starts = set(link.keys()) - set(link.values())

    ans = []
    for s in starts:
        e = link[s]
        val = vals[(s, e)]
        while e in link:
            val = min(val, vals[e, link[e]])
            e = link[e]
        ans.append((s, e, val))

    return sorted(ans)


for _ in range(int(input())):
    p, t = map(int, input().strip().split())
    pairs = [tuple(map(int, input().strip().split())) for _ in range(t)]
    res = solve(p, pairs)
    print(len(res))
    for ans in res:
        print(*ans)
