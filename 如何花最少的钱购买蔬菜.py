
def solve(sellers):
    last = [0]*3
    for seller in sellers:
        nx = [0]*3
        nx[0] = seller[0] + min(last[1], last[2])
        nx[1] = seller[1] + min(last[0], last[2])
        nx[2] = seller[2] + min(last[0], last[1])
        last = nx
    return min(last)


for _ in range(int(input())):
    n = int(input())
    sellers = [list(map(int, input().split())) for _ in range(n)]
    print(solve(sellers))