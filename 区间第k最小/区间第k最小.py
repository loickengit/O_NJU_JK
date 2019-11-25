
def solve(nums, s, e, k):
    return sorted(nums[s-1:e])[k-1]


for _ in range(int(input())):
    nums = list(map(int, input().split()))
    s, e = map(int, input().split())
    k = int(input())
    print(solve(nums, s, e, k))