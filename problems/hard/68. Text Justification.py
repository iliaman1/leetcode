from typing import List


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        pointer_word = 0
        line_lst = []

        while pointer_word < len(words):
            line = []





if __name__ == '__main__':
    solution = Solution()
    assert solution.fullJustify(
        ["This", "is", "an", "example", "of", "text", "justification."],
        16
    ) == [
        "This    is    an",
        "example  of text",
        "justification.  "
    ], 'test 1'

    assert solution.fullJustify(
        ["What", "must", "be", "acknowledgment", "shall", "be"],
        16
    ) == [
        "What   must   be",
        "acknowledgment  ",
        "shall be        "
    ], 'test 2'

    assert solution.fullJustify(
        [
            "Science", "is", "what", "we", "understand", "well", "enough", "to", "explain", "to", "a", "computer.",
            "Art", "is", "everything", "else", "we", "do"
        ],
        20
    ) == [
        "Science  is  what we",
        "understand      well",
        "enough to explain to",
        "a  computer.  Art is",
        "everything  else  we",
        "do                  "
    ], 'test 3'
