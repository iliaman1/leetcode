from pprint import pprint
from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        flag = True

        for i in range(len(board)):
            j = 0
            while j < len(board[i]):
                if board[i][j] == word[0]:
                    used_letters = [(i, j)]
                    current_index = 1
                    while True:
                        if len(used_letters) == len(word):
                            return True

                        if i + 1 < len(board) and board[i + 1][j] == word[current_index] and (
                                i + 1, j) not in used_letters:
                            i += 1
                            used_letters.append((i, j))
                            current_index += 1
                        elif i - 1 >= 0 and board[i - 1][j] == word[current_index] and (i - 1, j) not in used_letters:
                            i -= 1
                            used_letters.append((i, j))
                            current_index += 1
                        elif j + 1 < len(board[i]) and board[i][j + 1] == word[current_index] and (
                                i, j + 1) not in used_letters:
                            j += 1
                            used_letters.append((i, j))
                            current_index += 1
                        elif j - 1 >= 0 and board[i][j - 1] == word[current_index] and (i, j - 1) not in used_letters:
                            j -= 1
                            used_letters.append((i, j))
                            current_index += 1
                        else:
                            board[used_letters[-1][0]][used_letters[-1][1]] = '#'
                            i = used_letters[0][0]
                            j = used_letters[0][1] - 1
                            for elm in board:
                                print(elm)
                            break

                else:
                    j += 1
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
