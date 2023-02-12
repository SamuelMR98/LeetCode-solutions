from typing import List

nums = [2,1,-1]

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        ref = sum(nums)
        pivot = 0
        for i in range(len(nums)):
            ref -= nums[i]
            if pivot == ref:
                return i
            pivot += nums[i]
        return -1            

if __name__ == "__main__":
    print(Solution().pivotIndex(nums))