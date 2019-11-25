

def solve(nums):
    return nums == nums[::-1]


for _ in range(int(input())):
    ans = solve(input().split()[1:])
    out = 'true' if ans else 'false'
    print(out)
