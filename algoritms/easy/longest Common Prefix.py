class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        base = strs[0]
        for i in range(len(strs)):
            temp = ''
            if len(base) == 0:
                break
            for j in range(min(map(len, strs))):
                if j < len(base) and strs[i][j] == base[j]:
                    temp += base[j]
                else:
                    break
            base = temp
        return base


s = ['123', '126', '121231239']


test = Solution()
print(test.longestCommonPrefix(s))
# def test(s):
#     base = s[0]
#     for i in range(len(s)):
#         temp = ''
#         if len(base) == 0:
#             break
#         for j in range(min(map(len, s))):
#             if j < len(base) and s[i][j] == base[j]:
#                 temp += base[j]
#         base = temp
#     print(base)
#
#
# test(s)
