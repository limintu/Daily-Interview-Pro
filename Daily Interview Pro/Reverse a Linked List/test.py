import unittest

from solution import ListNode, Solution

class MyTestCase(unittest.TestCase):
    def testIterative(self):
        testHead = ListNode(4)
        p = testHead
        p.next = ListNode(3)
        p = p.next
        p.next = ListNode(2)
        p = p.next
        p.next = ListNode(1)
        p = p.next
        p.next = ListNode(0)

        self.customAssertEqual(testHead, Solution().reverseIteratively(testHead))
    def testRecursive(self):
        testHead = ListNode(4)
        p = testHead
        p.next = ListNode(3)
        p = p.next
        p.next = ListNode(2)
        p = p.next
        p.next = ListNode(1)
        p = p.next
        p.next = ListNode(0)

        self.customAssertEqual(testHead, Solution().reverseRecursively(testHead))

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
