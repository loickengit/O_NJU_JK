n = 10 ** 6 // 2
isPrimes = [False] * 2 + [True] * (n - 1)
for p in range(2, n):
    if not isPrimes[p]: continue
    for i in range(p * 2, n, p):
        isPrimes[i] = False
primes = [i for i in range(n) if isPrimes[i]]


import bisect
def solve(N):
    index = bisect.bisect_left(primes, int(N ** 0.5))
    lo, hi = 0, index
    ans = 0
    while lo < hi:
        while lo < hi and (primes[lo] * primes[hi]) ** 2 <= N:
            lo += 1
        if lo == hi: break
        ans += lo
        hi -= 1
    ans += lo * (lo + 1) // 2
    import math
    ans += bisect.bisect_right(primes, int(math.pow(N, 1 / 8)))
    return ans


N = int(input())
for _ in range(N):
    K = int(input())
    print(solve(K))


