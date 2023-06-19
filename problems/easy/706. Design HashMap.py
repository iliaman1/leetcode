class MyHashMap:

    def __init__(self):
        self.my_map = []

    def put(self, key: int, value: int) -> None:
        for index, element in enumerate(self.my_map):
            if element[0] == key:
                element[1] = value
                return

        self.my_map.append([key, value])

    def get(self, key: int) -> int:
        for m_key, value in self.my_map:
            if m_key == key:
                return value
        return -1

    def remove(self, key: int) -> None:
        for index, element in enumerate(self.my_map):
            if element[0] == key:
                del self.my_map[index]
                break
