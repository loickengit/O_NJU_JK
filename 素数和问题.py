

def solve(n):
    primes = [False]*2 + [True] * n
    for i in range(2, n):
        if not primes[i]: continue
        for j in range(i*2, n+1, i):
            primes[j] = False

    primes = [i for i in range(n+1) if primes[i]]

    lo, hi = 0, len(primes)-1
    while lo <= hi:
        cur = primes[lo] + primes[hi]
        if cur == n:
            return [primes[lo], primes[hi]]
        elif cur > n:
            hi -= 1
        else:
            lo += 1


for _ in range(int(input())):
    print(*(solve(int(input()))))