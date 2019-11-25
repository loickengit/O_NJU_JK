
def solve(nums, k):
    stack = []
    ans = 0
    for i, num in enumerate(nums):
        while stack and stack[-1] < num:
            stack.pop()
        stack.append(num)
        if i >= k-1:
            ans += stack[0]
            if stack[0] == nums[i-k+1]:
                stack.pop(0)
    return ans


for _ in range(int(input())):
    nums = list(map(int, input().split()))
    k = int(input())
    print(solve(nums, k))