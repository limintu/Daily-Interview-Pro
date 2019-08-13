import unittest

from solution import ListNode, Solution


class MyTestCase(unittest.TestCase):
    def test1(self):
        l1 = ListNode(2)
        l1.next = ListNode(4)
        l1.next.next = ListNode(3)

        l2 = ListNode(5)
        l2.next = ListNode(6)
        l2.next.next = ListNode(4)

        ans = ListNode(7)
        ans.next = ListNode(0)
        ans.next.next = ListNode(8)

        self.customAssertEqual(Solution().addTwoNumbers(l1, l2), ans)

    def customAssertEqual(self, expected, actual):
        l1, l2 = expected, actual
        while l1 is not None and l2 is not None:
            if l1.val != l2.val:
                return False
            l1 = l1.next
            l2 = l2.next

        if l1 is not None or l2 is not None:
            return False

        return True;

if __name__ == '__main__':
    unittest.main()
