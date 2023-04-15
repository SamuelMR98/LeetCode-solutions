s = 'foo'
t = 'bar'

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        if len(s) == 0:
            return True
        if s[0] == t[0]:
            return self.isIsomorphic(s[1:], t[1:])
        else:
            return self.isIsomorphic(s, t[1:])

if __name__ == "__main__":
    print(Solution().isIsomorphic(s,t))
