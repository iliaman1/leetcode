def rotate(nums: list[int], k: int) -> None:
    k = k if len(nums) > k else k % len(nums)
    for _ in range(k):
        nums.insert(0, nums.pop())


# leetcode propystil
def rotate1(nums: list[int], k: int) -> None:
    k = k % len(nums)
    nums.reverse()
    nums[:k] = reversed(nums[:k])
    nums[k:] = reversed(nums[k:])


# without cycle
def rotate2(nums: list[int], k: int) -> None:
    k = k % len(nums)
    nums = nums[-k:] + nums[:-k]
