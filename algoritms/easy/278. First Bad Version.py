def isBadVersion(version: int) -> bool:
    return version >= 4


# binary
def firstBadVersion(n: int) -> int:
    left = 1
    right = n
    mid = -1
    while left <= right:
        mid = (left + right) // 2
        if mid == 1 and isBadVersion(mid):
            return mid
        elif isBadVersion(mid) and not isBadVersion(mid - 1):
            return mid
        elif not isBadVersion(mid):
            left = mid + 1
        elif isBadVersion(mid):
            right = mid - 1

    return mid + 1
