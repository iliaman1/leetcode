from collections import Counter

def hammingWeight(n: int) -> int:
    return Counter(str(n))['1']


print(hammingWeight(11111111111111111111111111111101))