from collections import deque
from typing import List


class Solution:
    @staticmethod
    def count_students(students: List[int], sandwiches: List[int]) -> int:
        circle_student_count = 0
        square_student_count = 0

        for student in students:
            if student == 0:
                circle_student_count += 1
            else:
                square_student_count += 1

        for sandwich in sandwiches:
            if sandwich == 0 and circle_student_count == 0:
                return square_student_count

            if sandwich == 1 and square_student_count == 0:
                return circle_student_count

            if sandwich == 0:
                circle_student_count -= 1
            else:
                square_student_count -= 1

        return 0


class SolutionStack:
    @staticmethod
    def count_students(students: List[int], sandwiches: List[int]) -> int:
        length = len(students)  # Sandwiches will be the same length
        student_queue = deque()
        sandwich_stack = []

        # Add students and sandwiches to the queue and stack
        for i in range(length):
            sandwich_stack.append(sandwiches[length - i - 1])
            student_queue.append(students[i])

        # Simulate the lunch process by serving sandwiches
        # or sending students to the back of the queue.
        last_served = 0
        while len(student_queue) > 0 and last_served < len(student_queue):
            if sandwich_stack[-1] == student_queue[0]:
                sandwich_stack.pop()  # Serve sandwich
                student_queue.popleft()  # Student leaves queue
                last_served = 0
            else:
                # Student moves to back of queue
                student_queue.append(student_queue.popleft())
                last_served += 1

        # Remaining students in queue are unserved students
        return len(student_queue)
