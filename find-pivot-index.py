# https://leetcode.com/problems/find-pivot-index/

class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        right_sum = 0
        for i in range(len(nums)):
            right_sum+=nums[i]
        
        left_sum = 0
        for j in range(len(nums)):
            right_sum = right_sum - nums[j]
            if (left_sum == right_sum):
                return(j)
            left_sum = left_sum + nums[j]
        
        return -1
