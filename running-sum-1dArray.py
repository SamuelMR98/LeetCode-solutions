from typing import List
nums = [1,1,1,1,1]

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        runningSum = []
        for i in nums:
            if len(runningSum) == 0:
                runningSum.append(i)
            else:
                runningSum.append(runningSum[-1] + i)
        return runningSum    


if __name__ == "__main__":
    print(Solution().runningSum(nums))  
    