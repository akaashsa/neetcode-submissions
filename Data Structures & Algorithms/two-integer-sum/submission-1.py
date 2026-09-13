class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        
        i = 0
        length = len(nums)
        indices = {nums[x]: x for x in range(0,length)}
        while i<length:
            indices[i] = target-nums[i]
            if indices[i] in indices.keys() and i!=indices[indices[i]]:

                return sorted([i,indices[indices[i]]])
            i += 1
            

        return 0
