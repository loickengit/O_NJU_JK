

def solve(nums):
    sindex = {num: i for i, num in enumerate(sorted(nums))}
    ans = 0
    for i, num in enumerate(nums):
        while i != sindex[nums[i]]:
            ans += 1
            nums[sindex[nums[i]]], nums[i] = nums[i], nums[sindex[nums[i]]]
    return ans


for _ in range(int(input())):
    input()
    nums = list(map(int, input().split()))
    print(solve(nums))
