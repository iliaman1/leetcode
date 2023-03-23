def runningSum(nums: list) -> list:
    return [sum(nums[:i + 1]) for i in range(len(nums))]


if __name__ == '__main__':
    assert runningSum([1, 2, 3, 4]) == [1, 3, 6, 10], 'test 1 failed'
    assert runningSum([1, 1, 1, 1, 1]) == [1, 2, 3, 4, 5], 'test 2 failed'
    assert runningSum([3, 1, 2, 10, 1]) == [3, 4, 6, 16, 17], 'test 3 failed'