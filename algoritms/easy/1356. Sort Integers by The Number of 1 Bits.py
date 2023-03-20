def sort_by_bits(arr: list[int]) -> list[int]:
    return sorted(arr, key=lambda x: (bin(x).count('1'), x))
