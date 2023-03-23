class Obj:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None


class MyStack:
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
            buf = self.last.val
            self.last = self.root = None
            return buf
        else:
            buf = self.last.val
            self.last.prev.next = None
            self.last = self.last.prev
            return buf

    def top(self) -> int:
        return self.last.val

    def empty(self) -> bool:
        return self.last == None and self.root == None

    def show(self):
        return self.last, self.root


# good solution?
# import queue
# class MyStack:
#     def __init__(self):
#         self.q_primary = queue.Queue()
#         self.q_helper = queue.Queue()
#
#     def push(self, x: int) -> None:
#         self.q_primary.put(x)
#     def pop(self) -> int:
#         while self.q_primary.qsize() != 1:
#             self.q_helper.put(self.q_primary.get())
#         top = self.q_primary.get()
#         while not self.q_helper.empty():
#             self.q_primary.put(self.q_helper.get())
#         return top
#     def top(self) -> int:
#         while self.q_primary.qsize() != 1:
#             self.q_helper.put(self.q_primary.get())
#         top = self.q_primary.get()
#         while not self.q_helper.empty():
#             self.q_primary.put(self.q_helper.get())
#         self.q_primary.put(top)
#         return top
#     def empty(self) -> bool:
#         return self.q_primary.qsize() == 0


# what?
# class MyStack:
#
#     def __init__(self):
#         self.container = []
#
#     def push(self, x: int) -> None:
#         self.container.append(x)
#
#     def pop(self) -> int:
#         return self.container.pop()
#
#     def top(self) -> int:
#         return self.container[-1]
#
#     def empty(self) -> bool:
#         return len(self.container) == 0
