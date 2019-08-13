class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode(0)
        p = head
        carry = 0
        while l1 is not None or l2 is not None:
            sumup = carry
            if l1 is not None:
                sumup += l1.val
                l1 = l1.next
            if l2 is not None:
                sumup += l2.val
                l2 = l2.next
            p.next = ListNode(sumup % 10)
            carry = sumup // 10
            p = p.next

        if carry != 0:
            p.next = ListNode(carry)

        return head.next
