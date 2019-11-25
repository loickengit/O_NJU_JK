
import collections
def solve(nums):
    count = collections.Counter(nums)
    ans = 0
    for num in sorted(count.keys(), reverse=True):
        if count[num] > 0:
            ans += num * count[num]
            count[num-1] -= count[num]
    return ans


for _ in range(int(input())):
    input()
    nums = list(map(int, input().split()))
    print(solve(nums))