

def solve(nums):
    if max(nums) <= 0:
        return max(nums)
    n = len(nums)
    left = [0] * n
    for i in range(len(nums)-1):
        left[i+1] = max(nums[i]+left[i], 0)

    right = [0] * n
    for i in range(1, len(nums))[::-1]:
        right[i-1] = max(nums[i]+right[i], 0)

    ans = float('-inf')
    for i in range(n):
        ans = max(ans, left[i]+right[i], left[i] + nums[i] + right[i])
    return ans


def solve2(nums):
    def maxsub(nums):
        ans = float('-inf')
        cur = 0
        for num in nums:
            cur += num
            ans = max(cur, ans)
            cur = max(cur, 0)
        return ans

    ans = maxsub(nums)
    for i, num in enumerate(nums):
        if num < 0:
            ans = max(ans, maxsub(nums[:i]+nums[i+1:]))
    return ans


for _ in range(int(input())):
    input()
    nums = list(map(int, input().split()))
    print(solve(nums))