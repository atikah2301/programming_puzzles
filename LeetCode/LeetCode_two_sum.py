# Easy difficulty

class Solution:
    ## This version of the code is memory efficient but has time complexity O(n^2)
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        output = []
        for i in range(len(nums)):
            bond = target - nums[i]
            if bond in nums and nums.index(bond) != i:
                output.append(i)
                output.append(nums.index(bond))
                return output

    # ## This version of the code has complexity O(n) but uses more memory (incomplete)
    # def twoSum(self, nums: list[int], target: int) -> list[int]:
    #     nums_dict = dict(zip(nums, range(len(nums))))
    #     output = []
    #     for i in range(len(nums)):
    #         bond = target - nums[i]
    #         if bond in nums_dict:
    #             if nums_dict[bond] != i:
    #                 output.append(i)
    #                 output.append(nums.index(bond))
    #                 return output

solution = Solution()
nums = [3,3]
target = 6
answer = solution.twoSum(nums, target)
print(answer)