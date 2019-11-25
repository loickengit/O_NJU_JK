import itertools


def solve(s):
    ans = -1
    if s == '0':
        return ans
    for ss in itertools.permutations(s):
        num = int(''.join(ss))
        if num % 17 == 0 and num > ans:
            ans = num
    return ans


for _ in range(int(input())):
    res = solve(input())
    out = res if res != -1 else 'Not Possible'
    print(out)
