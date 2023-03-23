class Solution(object):
    def isPalindrome(self, x):
        if x < 0:
            return False
        lst = []
        i = 1
        while True:
            if x // 10 == 0:
                lst.append(x)
                break
            else:
                lst.append(x % 10)
                x = x // 10
            i += 1
        ind_n = 0
        ind_k = len(lst) - 1
        for i in range(len(lst) // 2):
            if ind_k <= ind_n:
                return True
            elif lst[ind_n] == lst[ind_k]:
                ind_n += 1
                ind_k -= 1
                continue
            else:
                return False
        return True


t = Solution()
print(t.isPalindrome())
