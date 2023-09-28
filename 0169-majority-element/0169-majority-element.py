class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dic = {}
        result = []

        for num in nums:
            if num in dic:
                dic[num] += 1
            else:
                dic[num] = 1

        for key, value in sorted(dic.items(), reverse=True, key=lambda item:item[1]):
            if value > (len(nums)/2):
                result.append(key)
                
        return max(result)