romanToInteger = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
}
class Solution:
    def romanToInt(self, s: str) -> int:
        groups = [s[i:i+3] for i in range(0, len(s), 3)]
        integer = 0
        for g in groups:
            res = 0
            lenght = len(g)
            
            if lenght == 3:
                int_1 = romanToInteger[g[0]]
                int_2 = romanToInteger[g[1]]
                int_3 = romanToInteger[g[2]]
                if int_3 > int_2 and int_3 > int_1:
                    res = int_3 - int_2 - int_1
                if int_3 > int_2 and int_3 <= int_1:
                    res = int_1 + (int_3 - int_2)
                else:
                    res = int_1 + int_2 + int_3
            if lenght == 2:
                int_1 = romanToInteger[g[0]]
                int_2 = romanToInteger[g[1]]
                if int_2 > int_1:
                    res = int_2 - int_1
                else:
                    res = int_1 + int_1
            if lenght == 1:
                int_1 = romanToInteger[g[0]]
                res = int_1
                
            integer += res
                       
        return integer

def main():
    print(Solution().romanToInt("MCMXCIV"))

if __name__ == "__main__":
    main()