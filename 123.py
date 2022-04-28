class Solution:
    def findRepeatNumber(self, nums):
        for i in range(len(nums)):

            while nums[i] != i:

                tmp=nums[i]
                nums[i]=nums[nums[i]]
                nums[nums[i]]=tmp

                if nums[i] == nums[nums[i]]:
                    return nums[i]
a=Solution()
b=a.findRepeatNumber([2, 3, 1, 0, 2, 5, 3])

