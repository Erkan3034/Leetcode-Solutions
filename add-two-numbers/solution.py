# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(0)  # sahte başlangıç node (baş referansı)
        current = dummy      # gezici pointer
        carry = 0            # elde

        # iki liste de bitene kadar veya elde kalana kadar devam et
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            total = val1 + val2 + carry
            carry = total // 10
            current.next = ListNode(total % 10)
            current = current.next

            # bir sonraki node'lara geç
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy.next
