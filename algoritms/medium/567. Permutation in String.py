from collections import Counter


def checkInclusion(s1: str, s2: str) -> bool:
    if len(s1) > len(s2):
        return False

    basket = []
    for right_index, value in enumerate(s2):
        if value in s1:
            left = right_index
            while left < right_index + len(s1) <= len(s2):
                basket.append(s2[left])
                left += 1
            if Counter(basket) == Counter(s1):
                return True
            else:
                basket.clear()

    return False


print(checkInclusion('adc', 'dcda'))
