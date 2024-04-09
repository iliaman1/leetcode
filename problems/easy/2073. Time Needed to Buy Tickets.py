from collections import deque
from typing import List


class SolutionWithQueue:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        que = deque()

        for i in range(len(tickets)):
            que.append(i)

        time = 0

        while que:
            time += 1
            front = que.popleft()
            tickets[front] -= 1

            if k == front and tickets[front] == 0:
                return time

            if tickets[front] != 0:
                que.append(front)

        return time


class SolutionWithoutQueue:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        n = len(tickets)
        time = 0

        # If person k only needs one ticket, return the time to buy it
        if tickets[k] == 1:
            return k + 1

        # Continue buying tickets until person k buys all their tickets
        while tickets[k] > 0:
            for i in range(n):
                # Buy a ticket at index 'i' if available
                if tickets[i] != 0:
                    tickets[i] -= 1
                    time += 1

                # If person k bought all their tickets, return the time
                if tickets[k] == 0:
                    return time

        return time


class OnePassSolution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        time = 0

        for i in range(len(tickets)):
            # If the current person is before or at the desired person 'k'
            if i <= k:
                # Buy the minimum of tickets available at person 'k' and the current person
                time += min(tickets[k], tickets[i])
            else:
                # If the current person is after 'k', buy the minimum of
                # (tickets available at person 'k' - 1) and the current person
                time += min(tickets[k] - 1, tickets[i])

        return time
