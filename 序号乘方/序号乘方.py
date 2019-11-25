
def solve(n):
    cur = 1
    while n >= cur**2:
        n -= cur**2
        cur += 1
    return cur - 1


for _ in range(int(input())):
    print(solve(int(input())))