class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        if len(colors) < 3:
            return False

        alice = bob = 0

        for i in range(1, len(colors) - 1):
            if colors[i - 1] == colors[i] == colors[i + 1]:
                if colors[i] == "A":
                    alice += 1
                else:
                    bob += 1

        return alice > bob


if __name__ == '__main__':
    solution = Solution()
    assert solution.winnerOfGame('AAABABB') is True, 'test 1 failed'
    assert solution.winnerOfGame('AA') is False, 'test 2 failed'
    assert solution.winnerOfGame('ABBBBBBBAAA') is False, 'test 3 failed'
    assert solution.winnerOfGame('AAAABBBB') is False, 'test 4 failed'
