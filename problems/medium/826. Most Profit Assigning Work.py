from typing import List


def mpa(difficulty: List[int], profit: List[int], worker: List[int]) -> int:
    res, best, j, tmp = 0, 0, 0, []
    for i in range(len(difficulty)):
        tmp.append((difficulty[i], profit[i]))

    tmp.sort()
    worker.sort()

    for work in worker:
        while j < len(tmp) and work >= tmp[j][0]:
            best = max(best, tmp[j][1])
            j += 1
        res += best

    return res
