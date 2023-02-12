string = "words and 987"

class Solution:
    def myAtoi(self, s: str) -> int:
        atoi = 0
        s = s.strip()
        if(s[0].isalpha()):
            return 0
        s = s.translate({ord(i): None for i in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ '})
        atoi = int(s)
        return atoi


if __name__ == "__main__":
    print(Solution().myAtoi(string))

