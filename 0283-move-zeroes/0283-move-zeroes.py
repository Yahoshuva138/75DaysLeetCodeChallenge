class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return 
        k = 0
        for i, num in enumerate(nums):
            if num != 0:
                nums[k] = num
                k += 1
            
        for i in range(k, len(nums)):
            nums[i] = 0

        