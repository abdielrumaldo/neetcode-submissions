class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = 0
        start = 0
        end = 0

        for i in range(len(nums)):
            if nums[i] != val:
                nums[start] = nums[end]
                start += 1
                end +=1
                count += 1
            elif nums[i] == val:
                end += 1
            elif end == len(nums):
                break
        return count