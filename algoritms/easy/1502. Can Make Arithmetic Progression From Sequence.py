def canMakeArithmeticProgression(arr: list[int]) -> bool:
    arr.sort(reverse=True)
    d = arr[0] - arr[1]
    for index in range(len(arr) - 1):
        if arr[index] - arr[index + 1] != d:
            return False

    return True
