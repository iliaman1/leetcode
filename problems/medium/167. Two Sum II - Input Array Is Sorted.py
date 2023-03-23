def two_sum(numbers: list[int], target: int) -> list[int]:
    for i in range(len(numbers)):
        left = i
        right = len(numbers) - 1

        while left < right:
            sum_of_two = numbers[left] + numbers[right]
            if sum_of_two < target:
                left += 1
            elif sum_of_two > target:
                right -= 1
            else:
                return [left + 1, right + 1]
