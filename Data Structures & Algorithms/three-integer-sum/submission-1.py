class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        k = 0
        res = []
        nums.sort()
        for k in range(0,len(nums)-2):
            if k > 0 and nums[k] == nums[k - 1]:
                continue
            
            i = k+1
            j = len(nums)-1
            
            while i< j:


                if nums[k]==-1*(nums[i]+nums[j]):
                    res.append([nums[k],nums[i],nums[j]])
                    i+=1
                    j-=1
                    while i<j and nums[i]==nums[i-1]:
                        i+=1
                
                elif nums[k] > -1*(nums[i]+nums[j]):
                    j -=1

                else:
                    i +=1
                
                

        
        return res

