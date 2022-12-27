def canJump(nums: list[int]) -> bool:
    pass


if __name__ == '__main__':
    assert canJump([2,3,1,1,4]) == True, 'test 1 failed'
    assert canJump([3,2,1,0,4]) == False, 'test 2 failed'
    assert canJump([3,2,3,0,4]) == True, 'test 3 failed'