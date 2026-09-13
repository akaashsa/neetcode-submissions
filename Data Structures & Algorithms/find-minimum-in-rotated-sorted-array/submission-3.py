class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        n = len(nums)
        h= n-1
        mid = (l+h)//2

        while l<h:
            if nums[mid]<nums[mid+1] and nums[mid]<nums[mid-1]:
                return nums[mid]
            
            else:
                if nums[mid]>=nums[0]:
                    if nums[mid] > nums[n-1]:
                        l +=1
                    else:
                        h -=1

                
                else :

                    h -=1
            
            mid = (l+h)//2
        
        return nums[mid]
        

                