def find_pivot_index(nums: list) -> int:
    total = sum(nums)
    temp = 0
    for i in range(len(nums)):
        if (nums[i] == total - 2 * temp):
            return i
        temp += nums[i]
    return -1


if __name__ == '__main__':
    assert find_pivot_index([1, 7, 3, 6, 5, 6]) == 3, 'failed test 1'
    assert find_pivot_index([1, 2, 3]) == -1, 'failed test 2'
    assert find_pivot_index([2, 1, -1]) == 0, 'failed test 3'
