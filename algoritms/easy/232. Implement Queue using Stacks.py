class Obj:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None


class MyQueue:

    def __init__(self):
        self.root = None
        self.last = None

    def push(self, x: int) -> None:
        obj = Obj(x)
        if self.root is None and self.last is None:
            self.root = self.last = obj
        else:
            buf = self.last
            self.last.next = obj
            self.last = obj
            self.last.prev = buf

    def pop(self) -> int:
        if self.last == self.root:
            buf = self.root.val
            self.last = self.root = None
            return buf
        else:
            buf = self.root.val
            self.root = self.root.next
            return buf

    def peek(self) -> int:
        return self.root.val

    def empty(self) -> bool:
        return self.last is None and self.root is None


# good solution
class MyQueue1:

    def __init__(self):
        self.queue = []

    def push(self, x: int) -> None:
        self.queue.append(x)

    def pop(self) -> int:
        t = self.queue[0]
        self.queue.remove(self.queue[0])
        return t

    def peek(self) -> int:
        return self.queue[0]

    def empty(self) -> bool:
        if len(self.queue) > 0:
            return False
        else:
            return True
