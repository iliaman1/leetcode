from collections import defaultdict


class MyHashMap:

    def __init__(self):
        self.mp = defaultdict(lambda: -1)

    def put(self, key: int, value: int) -> None:
        self.mp[key] = value

    def get(self, key: int) -> int:
        return self.mp[key]

    def remove(self, key: int) -> None:
        if key in self.mp:
            del self.mp[key]
