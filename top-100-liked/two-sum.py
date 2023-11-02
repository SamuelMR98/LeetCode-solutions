class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        sorted_array = nums.copy()

        sorted_array.sort()
        l = 0
        r = len(nums) - 1
        ans = []

        for i in range(len(sorted_array)):
            if sorted_array[l] + sorted_array[r] == target:
                ans.append(nums.index(sorted_array[l]))
                nums[nums.index(sorted_array[l])] = "x"
                ans.append(nums.index(sorted_array[r]))
                return ans
            elif sorted_array[l] + sorted_array[r] > target:
                r-=1
            elif sorted_array[l] + sorted_array[r] < target:
                l+=1
        
        return ans
        

        

array = [3,2,4]
target = 6

def main():
    print(Solution().twoSum(array, target))

if __name__ == "__main__":
    main()