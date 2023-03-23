# one line solution
def permute(nums: list[int]) -> list[list[int]]:

    return [nums] if len(nums) == 1 else [
        [value] + result
        for index, value in enumerate(nums)
        for result in permute(nums[:index] + nums[index + 1:])]


# if len(nums) == 1:
    #     return [nums]
    # for index, value in enumerate(nums):
    #     for result in permute(nums[:index] + nums[index + 1:]):
    #         results.append([value] + result)
