class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = len(nums)
        for i in range(len(nums)):
            if val in nums:
                nums.pop(nums.index(val))
                k -= 1