import collections

def solve(nums1, nums2):
    count = collections.Counter(nums1)
    res = []
    for num in nums2:
        res += [num]*count[num]
        del count[num]

    for num in sorted(count.keys()):
        res += [num] * count[num]
    return res


for _ in range(int(input())):
    input()
    nums1 = list(map(int, input().split()))
    nums2 = list(map(int, input().split()))
    print(*solve(nums1, nums2))