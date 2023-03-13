def reverseString(s: list[str]) -> None:
    s.reverse()


# with pointers
def reverseString1(s: list[str]) -> None:
    left = 0
    right = len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
