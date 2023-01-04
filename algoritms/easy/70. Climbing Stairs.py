def climbStairs(n: int) -> int:
    if n == 0:
        return 0
    counter = 0
    start = 0
    start_next = 1
    while counter < n:
        start, start_next = start_next, start + start_next
        counter += 1
    return start_next


#recursion method
# def climbStairs(n: int) -> int:
#     if n == 1:
#         return 1
#     elif n == 2:
#         return 2
#     else:
#         return climbStairs(n-1) + climbStairs(n-2)


if __name__ == '__main__':
    assert climbStairs(2) == 2, 'failed test 1'
    assert climbStairs(3) == 3, 'failed test 2'
    assert climbStairs(4) == 5, 'failed test 3'
    assert climbStairs(5) == 8, 'failed test 4'
    assert climbStairs(6) == 13, 'failed test 5'
    assert climbStairs(7) == 21, 'failed test 6'