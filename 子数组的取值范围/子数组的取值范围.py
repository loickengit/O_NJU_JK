
def solve(nums, k):
    minStack, maxStack = [nums[0]], [nums[0]]
    lo, hi = 0, 1
    ans, n = 0, len(nums)
    while hi < n:
        while minStack and nums[hi] < minStack[-1]:
            minStack.pop()
        minStack.append(nums[hi])

        while maxStack and nums[hi] > maxStack[-1]:
            maxStack.pop()
        maxStack.append(nums[hi])

        while minStack and maxStack and maxStack[0] - minStack[0] > k:
            ans += n - hi
            if minStack[0] == nums[lo]:
                minStack.pop(0)
            if maxStack[0] == nums[lo]:
                maxStack.pop(0)
            lo += 1
        hi += 1
    return ans


for _ in range(int(input())):
    nums = list(map(int, input().split()))
    k = int(input())
    print(solve(nums, k))
