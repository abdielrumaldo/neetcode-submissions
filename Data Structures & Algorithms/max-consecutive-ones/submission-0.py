class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = 0
        count = 0
        for i in range(len(nums)):
            if nums[i] == 1 and i == (len(nums) - 1):
                count += 1
                res = max(res, count)
            elif nums[i] == 1:
                count += 1
            elif nums[i] == 0:
                res = max(res, count)
                count = 0
            
        return res