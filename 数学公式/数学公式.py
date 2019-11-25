from functools import lru_cache
@lru_cache(None)
def solve(a, b, c):
    a %= c
    if b == 1:
        return a
    return (solve(a, (b+1)//2, c) * solve(a, b//2, c)) % c


for _ in range(int(input())):
    a, b, c = map(int, input().split())
    print(solve(a, b, c))