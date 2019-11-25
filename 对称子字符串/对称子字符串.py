

def solve(s):
    nums = list(map(int, s))
    ans, n = 0, len(nums)
    for i in range(len(nums)-1):
        l, r = i, i+1
        suml = sumr = 0
        while l >= 0 and r < n:
            suml += nums[l]
            sumr += nums[r]
            if suml == sumr and i-l+1 > ans:
                ans = i-l+1
            l -= 1
            r += 1
    return ans*2


for _ in range(int(input())):
    s = input()
    print(solve(s))
