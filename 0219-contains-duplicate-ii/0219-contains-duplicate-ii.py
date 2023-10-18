class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dic = dict.fromkeys(nums)
        for i, num in enumerate(nums):
            if dic[num] == None:
                dic[num] = [i]
            else:
                dic[num].append(i)
        
        for val in dic.values():
            if len(val) >= 2:
                for i in range(len(val)):
                    for j in range(i+1, len(val)):
                        if abs(val[j]-val[i]) <= k:
                            return True
        return False