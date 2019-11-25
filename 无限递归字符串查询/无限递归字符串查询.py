s = list('12345$54321')


def solve(n):
    if n <= 11:
        return s[n-1]

    count, times = 5, 1
    while count < n:
        count = count*2 + times
        times += 1

    lastc = (count - times + 1) // 2
    if lastc < n < lastc+times:
        return '$'
    return solve(n-lastc-times+1)


for _ in range(int(input())):
    print(solve(int(input())))