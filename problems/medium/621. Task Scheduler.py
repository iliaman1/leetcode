from collections import Counter
from typing import List


class Solution:
    @staticmethod
    def least_interval(tasks: List[str], n: int) -> int:
        freq = [0] * 26
        for task in tasks:
            freq[ord(task) - ord('A')] += 1

        freq.sort()
        max_freq = freq[25] - 1
        idle_slots = max_freq * n
        for i in range(24, -1, -1):
            idle_slots -= min(max_freq, freq[i])

        return idle_slots + len(tasks) if idle_slots > 0 else len(tasks)


class GoodSolution:
    @staticmethod
    def least_interval(tasks: List[str], n: int) -> int:
        l = Counter(tasks)
        return max((n + 1) * (max(l.values()) - 1) + len([x for x in l.values() if x == max(l.values())]), len(tasks))
