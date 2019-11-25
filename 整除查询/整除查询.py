
def solve(nums, query):
    return [sum(int(num % q == 0) for num in nums) for q in query]


for _ in range(int(input())):
    input()
    nums = list(map(int, input().split()))
    query = list(map(int, input().split()))
    print(' '.join(map(str, solve(nums, query))))