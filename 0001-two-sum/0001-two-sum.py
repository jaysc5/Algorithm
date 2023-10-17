class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {num : i for i, num in enumerate(nums)}
        
        for i, num in enumerate(nums):
            if (target-num) in dic and i != dic[target-num]:
                return [i, dic[target-num]]
