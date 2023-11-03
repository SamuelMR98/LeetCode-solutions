class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0: return 0
        longest = 0
        start = 0
        end = 0
        while end < len(s):
            if s[end] in s[start:end]:
                start += 1
            else:
                end += 1
                longest = max(longest, end-start)
        return longest
    
def main():
    print(Solution().lengthOfLongestSubstring("abcabcbb"))

if __name__ == "__main__":
    main()