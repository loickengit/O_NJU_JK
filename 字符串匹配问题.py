def solve(txt, pat):
    ans = [-1]
    while txt.find(pat, ans[-1]+1) != -1:
        ans.append(txt.find(pat, ans[-1]+1))
    return ans[1:]


for _ in range(int(input())):
    txt, pat = input().split(',')
    res = solve(txt, pat)
    print(*solve(txt, pat))
