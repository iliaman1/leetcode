class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        res = []
        while head:
            res.append(head.val)
            head = head.next

        if len(res) < 2:
            return True

        return res == res[::-1]