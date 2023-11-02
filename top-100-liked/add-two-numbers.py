class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

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
    print(Solution().addTwoNumbers(l1=l1, l2=l2))

if __name__ == "__main__":
    main()