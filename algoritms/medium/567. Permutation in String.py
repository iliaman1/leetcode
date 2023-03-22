from collections import Counter, defaultdict


def checkInclusion(s1: str, s2: str) -> bool:
    if len(s1) > len(s2):
        return False

    basket = Counter(s1)

    for right_index, value in enumerate(s2):
        if value in basket:
            basket[value] -= 1

        if right_index >= len(s1) and s2[right_index - len(s1)] in basket:
            basket[s2[right_index - len(s1)]] += 1

        if all(basket[i] == 0 for i in basket):
            return True

    return False


# good solution
def checkInclusion1(s1: str, s2: str) -> bool:
    length = len(s1) - 1
    window = defaultdict(int)
    counter = Counter(s1)

    for index, value in enumerate(s2):
        window[value] += 1

        if window == counter:
            return True

        if index >= length:
            key = s2[index - length]
            window[key] -= 1

            if window[key] == 0:
                del window[key]

    return False

print(checkInclusion1('adc', 'dcda'))
print(checkInclusion1('ab', 'eidboaoo'))
print(checkInclusion1('ab', 'eidbaooo'))
