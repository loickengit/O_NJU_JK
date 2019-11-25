from itertools import combinations


def solve(nums1, nums2):
    ans = float('inf')
    total = sum(nums1) + sum(nums2)
    for arr in combinations(nums1+nums2, len(nums1)):
        ans = min(ans, abs(total - 2*sum(arr)))
    return ans


for _ in range(int(input())):
    nums1 = list(map(int, input().split()))
    nums2 = list(map(int, input().split()))
    print(solve(nums1, nums2))
