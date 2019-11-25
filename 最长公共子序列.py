

def solve(s1, s2):

    import functools
    @functools.lru_cache(None)
    def dp(i, j):
        if i >= len(s1) or j >= len(s2):
            return ['']

        if s1[i] == s2[j]:
            res = [s1[i] + r for r in dp(i+1, j+1)]
        else:
            r1, r2 = dp(i+1, j), dp(i, j+1)
            res = r1 if len(r1[0]) > len(r2[0]) else r2 if len(r1[0]) != len(r2[0]) else list(set(r1+r2))
        return res

    return sorted(dp(0, 0))


for _ in range(int(input())):
    for ans in solve(input(), input()):
        print(ans)
