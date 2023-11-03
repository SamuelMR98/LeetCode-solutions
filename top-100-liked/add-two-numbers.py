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
    ans = []
    def addTwoNumbers(self, l1:list, l2:list) -> list:
        n1 = ''.join(str(e) for e in l1)
        n2 = ''.join(str(e) for e in l2)
        sum = int(n1) + int(n2)
        sum = str(sum)
        return list(sum)
    
l1 = [2,4,3]
l2 = [5,6,4]

def main():
    l1 = LinkedList().insert(2).insert(4).insert(3)
    l2 = LinkedList().insert(5).insert(6).insert(4)
    print(Solution().addTwoNumbers(l1,l2))

if __name__ == "__main__":
    main()