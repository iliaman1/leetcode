from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def backtrack(i, j, k):
            if k == len(word):
                return True

            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] != word[k]:
                return False

            temp = board[i][j]
            board[i][j] = ''

            if (
                    backtrack(i + 1, j, k + 1) or
                    backtrack(i - 1, j, k + 1) or
                    backtrack(i, j + 1, k + 1) or
                    backtrack(i, j - 1, k + 1)
            ):
                return True

            board[i][j] = temp
            return False

        for i in range(len(board)):
            for j in range(len(board[0])):
                if backtrack(i, j, 0):
                    return True

        return False


if __name__ == '__main__':
    solution = Solution()
    assert solution.exist(
        board=[
            ["A", "B", "C", "E"],
            ["S", "F", "C", "S"],
            ["A", "D", "E", "E"]],
        word="ABCCED") is True
    assert solution.exist(
        board=[
            ["A", "B", "C", "E"],
            ["S", "F", "C", "S"],
            ["A", "D", "E", "E"]],
        word="SEE") is True
    assert solution.exist(
        board=[
            ["A", "B", "C", "E"],
            ["S", "F", "C", "S"],
            ["A", "D", "E", "E"]],
        word="ABCB") is False
    assert solution.exist(
        board=[
            ["D", "D", "D"],
            ["A", "A", "D"],
            ["B", "C", "D"]],
        word="AAB") is True
    assert solution.exist(
        board=[
            ["C", "A", "A"],
            ["A", "A", "A"],
            ["B", "C", "D"]],
        word="AAB") is True
