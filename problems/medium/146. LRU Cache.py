class LRUCache:

    def __init__(self, capacity: int):
        self.basket = {}
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self.basket:
            val = self.basket.pop(key)
            self.basket[key] = val
            return self.basket.get(key)
        return -1

    def put(self, key: int, value: int) -> None:
        if key not in self.basket.keys():
            if len(self.basket.keys()) == self.capacity:
                del self.basket[next(iter(self.basket))]
        else:
            self.basket.pop(key)
        self.basket[key] = value
