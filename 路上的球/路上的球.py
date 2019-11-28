
def solve(balls1, balls2):
    common = set(balls1) & set(balls2)
    arr1, arr2 = [], []
    for num in sorted(common):
        idx1 = balls1.index(num)
        idx2 = balls2.index(num)
        arr1.append(sum(balls1[:idx1+1]))
        arr2.append(sum(balls2[:idx2+1]))
        balls1 = balls1[idx1+1:]
        balls2 = balls2[idx2+1:]
    ans = max(sum(balls1), sum(balls2))
    for val1, val2 in zip(arr1, arr2):
        ans += max(val1, val2)
    return ans
    

# balls1 = [1, 4, 5, 6, 8]
# balls2 = [2, 3, 4, 6, 9]
# print(solve(balls1, balls2))
for _ in range(int(input())):
    input()
    balls1 = list(map(int, input().split()))
    balls2 = list(map(int, input().split()))
    print(solve(balls1, balls2))