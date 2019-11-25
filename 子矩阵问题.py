
def solve(matrix):
    m, n = len(matrix), len(matrix[0])

    def count(r, c):
        ans = 0
        for j in range(c, n):
            if matrix[r][j] == 0:
                break
            i = r
            while i < m and all(matrix[i][c:j+1]):
                i += 1
            ans = max(ans, (i-r)*(j-c+1))
        return ans

    ans = 0
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 1:
                ans = max(ans, count(i, j))
    return ans


for _ in range(int(input())):
    rows, cols = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(rows)]
    print(solve(matrix))
