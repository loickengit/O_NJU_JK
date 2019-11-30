
import collections
def solve(nums):
    count = collections.Counter(nums)
    res = []
    for val, c in count.most_common():
        res += [val] * c
    return res


for _ in range(int(input())):
    input()
    nums = list(map(int, input().split()))
    print(*solve(nums))