# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert(self, val):
        if self.head is None:
            self.head = ListNode(val)
        else:
            pointer = self.head
            while pointer.next:
                pointer = pointer.next
            pointer.next = ListNode(val)
        def reverse(self):
            prev = None
            current = self.head
            while current:
                next = current.next
                current.next = prev
                prev = current
                current = next
            self.head = prev

class Solution:
    def addTwoNumbers(self, l1:ListNode, l2:ListNode) -> ListNode:
        n1 = ''
        n2 = ''
        pointer = l1.next
        return


def main():
    l1 = LinkedList().insert(2).insert(4).insert(3)
    l2 = LinkedList().insert(5).insert(6).insert(4)
    print(Solution().addTwoNumbers(l1,l2))

if __name__ == "__main__":
    main()