

def solve(items, k):
    e = len(items) // k * k
    res = []
    for i in range(0, e, k):
        res += items[i:i+k][::-1]
    res += items[e:]
    return res


for _ in range(int(input())):
    line = input().split()
    items, k = line[1:-1], int(line[-1])
    print(*solve(items, k))