def plusOne(digits: list[int]) -> list[int]:
    res = digits[::-1]
    for index, element in enumerate(res):
        if element != 9:
            res[index]+=1
            break
        elif index == len(res)-1:
            res[index] = 0
            res.append(0)
        else:
            res[index] = 0
    return res[::-1]


if __name__ == '__main__':
    assert plusOne([1, 7, 3, 6, 5, 6]) == [1, 7, 3, 6, 5, 7], 'failed test 1'
    assert plusOne([1,2,3]) == [1,2,4], 'failed test 1'
    assert plusOne([4,3,2,1]) == [4,3,2,2], 'failed test 1'
    assert plusOne([9]) == [1, 0], 'failed test 1'

# class Solution(object):
#     def plusOne(self, digits):
#         """
#         :type digits: List[int]
#         :rtype: List[int]
#         """
#         return map(int,str(int(''.join(map(str, digits))) + 1))

# def plusOne(digits):
#     num = 0
#     for i in range(len(digits)):
#     	num += digits[i] * pow(10, (len(digits)-1-i))
#     return [int(i) for i in str(num+1)]