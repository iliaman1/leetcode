def divide(dividend: int, divisor: int) -> int:
        result_sign = '' if dividend < 0 and divisor < 0 or dividend > 0 and divisor > 0 else '-'
        dividend = abs(dividend)
        divisor = abs(divisor)
        res = 0
        current_sum = 0
        while current_sum < dividend:
            if current_sum + divisor > dividend:
                break
            current_sum += divisor
            res += 1

        return int(result_sign+str(res))


print(divide(-2147483648, -1))
