number = int(input())

class Solution:
    def isPalindrome(self, x: int) -> bool:
        n = str(x)
        palindrome = Solution.reverse(n)       
        if n == palindrome:
            return True
        else:
            return False
    
    def reverse(s):
        return s[::-1]

if __name__ == "__main__":
    print(Solution().isPalindrome(number))
