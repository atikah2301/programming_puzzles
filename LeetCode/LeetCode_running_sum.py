class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sum = 0 
        running_sum = []
        for i in range(len(nums)):   
            sum += nums[i]
            running_sum.append(sum)           
        return running_sum


    def runningSum2(self, nums: List[int]) -> List[int]:
        for i in range(1, len(nums)):
            nums[i] += nums[i-1]
        return nums