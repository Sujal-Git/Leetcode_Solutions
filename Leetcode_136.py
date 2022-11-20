#Using Inbuilt Easy Function

class Solution(object):
    def singleNumber(self, nums):
        for i in range(0,len(nums)):
            time= nums.count(nums[i])
            if (time==1):
                return nums[i]
 


