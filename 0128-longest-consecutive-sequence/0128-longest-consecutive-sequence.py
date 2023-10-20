class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        dic = {}

        for i, num in enumerate(sorted(set(nums))):
            if i == 0 or (num-1) not in dic:
                dic[num] = 1
            elif (num-1) in dic:
                dic[num] = dic.pop(num-1)
                dic[num] += 1
            elif num in dic:
                pass

        if dic == {}:
            return 0
        return max(dic.values())