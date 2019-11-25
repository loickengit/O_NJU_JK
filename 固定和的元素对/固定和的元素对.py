

def solve(nums, tar):
    nums.sort()
    lo, hi = 0, len(nums)-1
    ans = 0
    while lo < hi:
        cur = nums[lo] + nums[hi]
        if cur > tar:
            hi -= 1
        elif cur < tar:
            lo += 1
        else:
            cl = cr = 1
            while nums[lo] == nums[lo+cl]:
                cl += 1
            while nums[hi] == nums[hi-cr]:
                cr += 1
            if nums[lo] == nums[hi]:
                ans += cl*(cl-1)//2
            else:
                ans += cl*cr
            lo += cl
    return ans


for _ in range(int(input())):
    nums = list(map(int, input().split()))
    k = int(input())
    print(solve(nums, k))