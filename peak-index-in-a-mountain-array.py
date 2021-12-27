# https://leetcode.com/problems/peak-index-in-a-mountain-array/

class Solution(object):
    def peakIndexInMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        min, max = 0, len(arr)-1
        mid = min + (max-min)//2
        while( min < max):
            if (arr[mid] < arr[mid+1]):
                min = mid + 1
            else:
                max = mid
            mid = min + (max-min)//2
        
        return(min)
                
