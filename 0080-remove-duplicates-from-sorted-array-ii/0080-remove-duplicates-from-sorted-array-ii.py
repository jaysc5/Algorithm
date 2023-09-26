class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0

        while i+2 < len(nums):
            if nums[i] == nums[i+2]:
                del nums[i+2]
            else:
                i += 1
        
        return len(nums)