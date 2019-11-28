import heapq, collections
def solve(tasks):
    times = max([job[1] for job in tasks])

    t_tasks = collections.defaultdict(list)
    for task in tasks:
        t_tasks[task[1]].append(task)

    count, profit, q = 0, 0, []
    for t in range(1, times+1)[::-1]:
        for task in t_tasks[t]:
            heapq.heappush(q, -task[2])
        if q:
            count += 1
            profit += -heapq.heappop(q)

    return count, profit


for _ in range(int(input())):
    input()
    nums = list(map(int, input().split()))
    jobs = [tuple(nums[i:i+3]) for i in range(0, len(nums), 3)]
    print(*solve(jobs))