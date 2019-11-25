

def mergeSort(nums):
    if len(nums) < 2:
        return 0, nums
    count = 0
    mid = len(nums) // 2
    cl, l = mergeSort(nums[:mid])
    cr, r = mergeSort(nums[mid:])
    for i in range(len(nums)):
        if not r or l and l[0] < r[0]:
            nums[i] = l.pop(0)
        else:
            nums[i] = r.pop(0)
            count += len(l)

    return count + cl + cr, nums


def count(nums):
    return mergeSort(nums)[0]


for _ in range(int(input())):
    input()
    print(count(list(map(int, input().split()))))