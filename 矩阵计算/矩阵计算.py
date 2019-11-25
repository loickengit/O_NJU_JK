
def solve(n):
    arr = [0, 0, 1, 1, 1, 0, 1]
    return sum(arr[(i*j)**3 % 7] for i in range(1, n+1) for j in range(1, n+1))


for _ in range(int(input())):
    print(solve(int(input())))