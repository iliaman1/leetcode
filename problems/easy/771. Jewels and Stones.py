class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        basket = {}
        for jawel in jewels:
            basket[jawel] = stones.count(jawel)
        return sum(basket.values())


if __name__ == '__main__':
    soluton = Solution()
    assert soluton.numJewelsInStones("aA", "aAAbbbb") == 3
    assert soluton.numJewelsInStones("z", "ZZ") == 0
