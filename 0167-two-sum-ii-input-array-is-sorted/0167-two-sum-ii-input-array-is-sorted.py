class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        L,R=0,n-1
        while L<R:
            val=nums[L]+nums[R]
            if val==target:
                 return [L + 1, R + 1]
            elif val<target:
                  L+=1
            else:
                  R-=1            
        return [-1, -1]
        