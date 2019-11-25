
class Solution:

    def solve(self, times, score, tasks):
        self.ans = times + 1

        def dfs(t, s, i):
            if s >= score and self.ans > t:
                self.ans = t
                return
            if t > times or i >= len(tasks):
                return

            dfs(t + tasks[i][0], s + tasks[i][1], i + 1)
            dfs(t, s, i+1)

        dfs(0, 0, 0)
        return self.ans if self.ans <= times else -1


for _ in range(int(input())):
    n, times, score = map(int, input().split())
    tasks = [list(map(int, input().split())) for _ in range(n)]
    res = Solution().solve(times, score, tasks)
    if res != -1:
        print('YES', res)
    else:
        print('NO')