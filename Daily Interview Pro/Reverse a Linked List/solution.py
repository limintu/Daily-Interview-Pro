class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseIteratively(self, head: ListNode) -> ListNode:
        if head is None:
            return

        p = head
        prev = None

        while p is not None:
            temp = p.next
            p.next = prev
            prev = p
            p = temp

        return prev

    def reverseRecursively(self, head):
        return self.helper(head, None)

    def helper(self, head, prev):
        if head is None:
            return prev

        temp = head.next
        head.next = prev
        prev = head
        head = temp

        return self.helper(head, prev)