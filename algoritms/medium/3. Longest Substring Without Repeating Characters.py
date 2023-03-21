def lengthOfLongestSubstring(s: str) -> int:
    left = 0
    max_len = 0
    basket = []
    for right in range(len(s)):
        while s[right] in basket:
            basket.remove(s[left])
            left += 1

        basket.append(s[right])
        max_len = max(max_len, right - left + 1)

    return max_len


# better solution
def lengthOfLongestSubstring1(s: str) -> int:
    left = 0
    max_len = 0
    basket = {}
    for right_index, value in enumerate(s):
        if value not in basket:
            basket[value] = right_index
        elif value in basket and basket[value] < left:
            basket[value] = right_index
        else:
            left = basket[value] + 1
            basket[value] = right_index

        max_len = max(max_len, right_index - left + 1)
    return max_len
