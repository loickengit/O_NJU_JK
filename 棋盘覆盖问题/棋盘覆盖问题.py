def isSame(n1, n2, n3):
    return ((n1[0]-n3[0] >= 0) == (n2[0] - n3[0] >= 0)) and ((n1[1]-n3[1] >= 0) == (n2[1]-n3[1] >= 0))


def solve(tl, br, node, tar):
    if br[0] - tl[0] == 1:
        s = {tl, br, (tl[0]+1, tl[1]), (tl[0], tl[1]+1)}
        s.remove(node)
        s.remove(tar)
        return list(s)

    p4 = (tl[0] + (br[0]-tl[0]+1)//2, tl[1] + (br[1] - tl[1]+1)//2)
    nx = None
    if tar[0] >= p4[0]:
        if tar[1] >= p4[1]:
            nx = p4
            tl, br = p4, br
        else:
            nx = (p4[0], p4[1]-1)
            tl, br = (p4[0], tl[1]), (br[0], p4[1]-1)
    else:
        if tar[1] >= p4[1]:
            nx = (p4[0]-1, p4[1])
            tl, br = (tl[0], p4[1]), (p4[0]-1, br[1])
        else:
            nx = (p4[0]-1, p4[1]-1)
            tl, br = tl, (p4[0]-1, p4[1]-1)
    if isSame(node, tar, p4):
        nx = node
    elif nx == tar:
        res = [(p4[0]-1, p4[1]-1), (p4[0]-1, p4[1]), (p4[0], p4[1]-1), p4]

        if isSame(node, res[0], p4):
            res.remove(res[0])
        elif isSame(node, res[1], p4):
            res.remove(res[1])
        elif isSame(node, res[2], p4):
            res.remove(res[2])
        else:
            res.remove(res[3])
        res.remove(nx)
        return res
    return solve(tl, br, nx, tar)


for _ in range(int(input())):
    n, i, j = map(int, input().split())
    tar = tuple(map(int, input().split()))
    res = solve((0, 0), (2**n, 2**n), (i, j), tar)
    out = ','.join(sorted([' '.join(map(str, r)) for r in res]))
    print(out)