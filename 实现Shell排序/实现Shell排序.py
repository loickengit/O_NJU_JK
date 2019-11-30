def shellSort(nums, dis):
    for d in dis:
        for i in range(d, len(nums)):
            j = i
            back = nums[i]
            while j >= d and nums[j-d] > back:
                nums[j] = nums[j-d]
                j -= d
            nums[j] = back
    return nums


N = int(input())
for _ in range(N):
    nums = list(map(int, input().split()))
    dis = list(map(int, input().split()))
    res = shellSort(nums, dis)
    print(' '.join(map(str, res)))