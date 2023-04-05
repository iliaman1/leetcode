def multiply(num1: str, num2: str = '0') -> str:
    def to_int(str_number: str) -> int:
        multiplicator = 1
        current_index = len(str_number)-1
        res = 0
        while current_index >= 0:
            res += (ord(str_number[current_index]) - 48) * multiplicator
            current_index -= 1
            multiplicator *= 10
        return res

    return str(to_int(num1) * to_int(num2))


print(multiply('5', '2'))
