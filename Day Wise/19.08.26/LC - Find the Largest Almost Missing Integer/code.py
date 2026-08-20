from collections import defaultdict
class Solution(object):
    def largestInteger(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = defaultdict(int)
        n = len(nums)
        
        for i in range(n - k + 1):
            subarray = nums[i:i+k]
            unique_elements = set(subarray)
            for elem in unique_elements:
                count[elem] += 1
        
        almost_missing_integers = [num for num, cnt in count.items() if cnt == 1]
        
        if not almost_missing_integers:
            return -1
        
        return max(almost_missing_integers)