import bisect


def get_mid(nums):
    def long_sub(nums):
        stack = []
        lenarr = [0] * len(nums)
        for i, num in enumerate(nums):
            index = bisect.bisect_left(stack, num)
            lenarr[i] = index + 1
            if index >= len(stack):
                stack.append(num)
            else:
                stack[index] = num
        return lenarr

    lenl, lenr = long_sub(nums), long_sub(nums[::-1])[::-1]
    maxlen = max(lenl[i]+lenr[i] for i in range(len(nums)))
    return [i for i in range(len(nums)) if lenl[i]+lenr[i] == maxlen]


def solve(nums):
    def get_all(path, arr, i, res_path):
        if i >= len(arr):
            if not res_path or len(path) > len(res_path[0]):
                res_path.clear()
                res_path.append(path)
            elif len(path) == len(res_path[0]):
                res_path.append(path[::])
            return

        get_all(path, arr, i + 1, res_path)
        if i >= len(arr) or path and path[-1] >= arr[i]:
            return
        get_all(path+[arr[i]], arr, i + 1, res_path)

    ans = set()
    for mid in get_mid(nums):
        subl, subr = nums[:mid+1], nums[mid:][::-1]
        ansl, ansr = [], []
        get_all([], subl, 0, ansl)
        get_all([], subr, 0, ansr)
        ans |= set(' '.join(map(str, l + r[::-1][1:])) for l in ansl for r in ansr)
    return sorted(ans)


for _ in range(int(input())):
    nums = list(map(int, input().split()))
    for ans in solve(nums):
        print(ans)

