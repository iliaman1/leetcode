class Solution:
    def sum_square_numb(self, number) -> int:
        number = str(number)
        res_sum = 0
        for num in number:
            res_sum += int(num) ** 2
        return res_sum

    def is_happy(self, number: int) -> bool:
        used_numbers = []
        current_number = number
        while current_number not in used_numbers:
            if current_number == 1:
                return True
            used_numbers.append(current_number)
            current_number = self.sum_square_numb(current_number)

        return False


#решение через строку
# class Solution:
#     def isHappy(self, n: int) -> bool:
#         s = str(n)
#         l = []
#         while s != '1':
#             c = 0
#             for i in s:
#                 c += (int(i) ** 2)
#             if c in l:
#                 return 0
#             l.append(c)
#             s = str(c)
#         return 1


#решение через арфметику
# class Solution:
#     def isHappy(self, n: int) -> bool:
#         def digitSquareSum(n):
#             sum = 0
#             while n > 0:
#                 digit = n % 10
#                 sum += digit ** 2
#                 n //= 10
#             return sum
#
#         seen = set()
#         current = n
#         while current != 1 and current not in seen:
#             seen.add(current)
#             current = digitSquareSum(current)
#         return current == 1
