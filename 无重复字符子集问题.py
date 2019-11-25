
def solve(snums):
    def dfs(i, seen):
        if i >= len(snums):
            return 0

        ans = dfs(i+1, seen)
        if not (seen & set(snums[i])):
            seen |= set(snums[i])
            ans = max(ans, int(snums[i]) + dfs(i+1, seen))
            seen -= set(snums[i])
        return ans
    return dfs(0, set())


for _ in range(int(input())):
    input()
    nums = input().split()
    print(solve(nums))