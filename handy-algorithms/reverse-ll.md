# Reverse a Linked List

1. Initialize three pointers `prev` as `NULL`, `curr` as `head` and `next` as `NULL`.

2. Iterate through the linked list. In loop, do following.
   1. Before changing `next` of `curr`, store `next` node.
    `next = curr->next`
   2. Now change `next` of `curr`. This is where actual reversing happens.
    `curr->next = prev`
   3. Update `prev` as `curr` and `curr` as `next`.
    `prev = curr`
    `curr = next`

```python
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        curr = self.head
        while (curr is not None):
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        self.head = prev
        return prev
```