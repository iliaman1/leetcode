def rotate(nums: list[int], k: int) -> None:
    k = k if len(nums) > k else k % len(nums)
    for _ in range(k):
        nums.insert(0, nums.pop())
