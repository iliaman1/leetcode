from heapq import *


class SeatManager:

    def __init__(self, n: int):
        self.n = [i for i in range(1, n + 1)]

    def reserve(self) -> int:
        seat_number = heappop(self.n)
        return seat_number

    def unreserve(self, seatNumber: int) -> None:
        heappush(self.n, seatNumber)
