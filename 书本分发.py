from functools import lru_cache

def solve(p, tasks):
    @lru_cache(None)
    def dfs(rp, it):
        if rp == 1:
            return sum(tasks[it:])
        if it == len(tasks) - 1:
            return tasks[-1]
        rp -= 1

        ans, cursum = float('inf'), 0
        for j in range(it, len(tasks)):
            cursum += tasks[j]
            ans = min(ans, max(cursum, dfs(rp, j+1)))
        return ans

    return dfs(p, 0)


for _ in range(int(input())):
    input()
    tasks = list(map(int, input().split()))
    p = int(input())
    print(solve(p, tasks))

