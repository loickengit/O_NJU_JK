

def solve(mags):
    res = []
    for i in range(len(mags)-1):
        l, r = mags[i], mags[i+1]
        while True:
            mid = (l+r) / 2
            f = sum(1/(mid-m) for m in mags)
            if round(f, 5) == 0:
                res.append(mid)
                break
            elif f > 0:
                l = mid
            else:
                r = mid
    return res


for _ in range(int(input())):
    input()
    M = list(map(float, input().strip().split()))
    res = solve(M)
    out = ['{:.2f}'.format(loc) for loc in res]
    print(*out)