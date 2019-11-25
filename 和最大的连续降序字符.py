

def solve(chs):
    chs = [ord(c)-ord('A') for c in chs]
    chs = set(chs)
    ans = []
    for c in sorted(chs, reverse=True):
        for i in range(1, 25):
            cur = [c]
            while cur[-1] - i in chs:
                cur.append(cur[-1] - i)
            if len(cur) > len(ans) or (len(cur) == len(ans) and len(cur) >= 2 and cur[0]-cur[1] < ans[0] - ans[1]):
                ans = cur
    ans = [chr(c + ord('A')) for c in ans]
    return ans


for _ in range(int(input())):
    print(''.join(solve(input())))