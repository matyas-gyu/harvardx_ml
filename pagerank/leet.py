class Solution(object):
    def maxAscendingSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        tracker = nums[0]
        tracker_list = []
        for i in range(1, len(nums), 1):
            if nums[i] > nums[i-1]:
                tracker += nums[i]
            else:
                tracker_list.append(tracker)
                tracker = nums[i]

        return tracker_list 

maxAscendingSum(self, [1,2,3,11,9])
