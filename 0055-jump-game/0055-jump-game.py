class Solution:
    def canJump(self, nums: List[int]) -> bool:
        idx = 0
        for num in nums:
            if idx < 0:
                return False
            idx = max(num, idx)
            idx -= 1
        return True