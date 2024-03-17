from typing import List


def insert(intervals: List[List[int]], new_interval: List[int]) -> List[List[int]]:
    res = []
    i = 0
    n = len(intervals)

    while i < n and intervals[i][1] < new_interval[0]:
        res.append(intervals[i])
        i += 1

    while i < n and new_interval[1] >= intervals[i][0]:
        new_interval[0] = min(new_interval[0], intervals[i][0])
        new_interval[1] = max(new_interval[1], intervals[i][1])
        i += 1

    res.append(new_interval)

    while i < n:
        res.append(intervals[i])
        i += 1

    return res


def binary_search_insert(intervals: List[List[int]], new_interval: List[int]) -> List[List[int]]:
    if not intervals:
        return [new_interval]

    n = len(intervals)
    target = new_interval[0]
    l, r, res = 0, n - 1, []

    while l <= r:
        mid = (l + r) // 2
        if intervals[mid][0] < target:
            l = mid + 1
        else:
            r = mid - 1

    intervals.insert(l, new_interval)

    for i in intervals:
        if not res or res[-1][1] < i[0]:
            res.append(i)
        else:
            res[-1][1] = max(res[-1][1], i[1])

    return res

def best_beat_insert(intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
    res = []

    for i, n in enumerate(intervals):
        if newInterval[1] < n[0]:
            res.append(newInterval)
            return res + intervals[i:]

        elif newInterval[0] > n[1]:
            res.append(n)

        else:
            newInterval = [min(newInterval[0], n[0]), max(newInterval[1], n[1])]

    res.append(newInterval)

    return res
