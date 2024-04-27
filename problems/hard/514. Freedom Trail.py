from cmath import inf


class SolutionTopDown:
    def findRotateSteps(self, ring: str, key: str) -> int:
        ring_len = len(ring)
        key_len = len(key)
        best_steps = {}

        # Find the minimum steps between two indexes of ring
        def count_steps(curr, next):
            steps_between = abs(curr - next)
            steps_around = ring_len - steps_between
            return min(steps_between, steps_around)

        def try_lock(ring_index, key_index):
            # If we have already calculated this sub-problem, return result
            if (ring_index, key_index) in best_steps:
                return best_steps[(ring_index, key_index)]

            # If we reach the end of the keyword, it has been spelled
            if key_index == key_len:
                best_steps[(ring_index, key_index)] = 0
                return 0

            # For each occurrence of the character k[key_index] in ring
            # calculate the minimum steps from the ring_index of ring
            min_steps = inf
            for char_index in range(ring_len):
                if ring[char_index] == key[key_index]:
                    min_steps = min(min_steps,
                                    count_steps(ring_index, char_index)
                                    + 1
                                    + try_lock(char_index, key_index + 1))

            best_steps[(ring_index, key_index)] = min_steps
            return min_steps

        return try_lock(0, 0)


class SolutionBottomUp:
    def findRotateSteps(self, ring: str, key: str) -> int:
        ring_len = len(ring)
        key_len = len(key)
        # Initialize values of best_steps to largest integer
        best_steps = [[inf] * (key_len + 1) for _ in range(ring_len)]

        # Find the minimum steps between two indexes of ring
        def count_steps(curr, next):
            steps_between = abs(curr - next)
            steps_around = ring_len - steps_between
            return min(steps_between, steps_around)

        # Initialize last column to 0 to represent the word has been spelled
        for row in best_steps:
            row[key_len] = 0

        # For each occurrence of the character at key_index of key in ring
        # Stores minimum steps to the character from the ring_index of ring
        for key_index in range(key_len - 1, -1, -1):
            for ring_index in range(ring_len):
                for char_index in range(ring_len):
                    if ring[char_index] == key[key_index]:
                        best_steps[ring_index][key_index] = min(
                            best_steps[ring_index][key_index],
                            1 + count_steps(ring_index, char_index)
                            + best_steps[char_index][key_index + 1])

        return best_steps[0][0]
