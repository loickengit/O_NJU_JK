
def solve(n):

    def f(k):
        if k == 1:
            return 1
        return 3*f(k-1) + 1
    return 2*f(n)


for _ in range(int(input())):
    print(solve(int(input())))