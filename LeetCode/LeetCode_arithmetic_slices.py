class Solution:
    def numberOfArithmeticSlices(self, nums: list[int]) -> int:
        # My solution - better than 98% of submissions in time complexity
        # However, the code is not as readable
        if len(nums) < 3:
            return 0
        count_slices = 0
        diff = nums[1] - nums[0]
        length = 2
        for i in range(2, len(nums)):
            current_diff = nums[i] - nums[i - 1]
            if current_diff == diff:
                length += 1
            else:
                if length >= 3:
                    for j in range(1, length - 1):
                        count_slices += j
                diff = current_diff
                length = 2
        if length >= 3:
            for j in range(1, length - 1):
                count_slices += j
        return count_slices

        # Alternative solution - only better than  51% of submissions in time complexity

        # Reason is due to checking length and adding to count_slices at each iteration,
        # instead of doing this after each sub_array
        # resulting in more frequent checks using an if statement, which generally is a slow operation
        # as it opens up the possibility of branching

        # if len(nums) < 3:
        #     return 0
        # count_slices = 0
        # diff = nums[1] - nums[0]
        # length = 2
        # for i in range(2, len(nums)):
        #     current_diff = nums[i] - nums[i-1]
        #     if current_diff == diff:
        #         length += 1
        #         if length >= 3:
        #             count_slices += length - 2
        #     else:
        #         diff = current_diff
        #         length = 2
        # return count_slices

if __name__ == '__main__':
    sol = Solution()
    nums = [1,2,3,8,9,10]
    ans = sol.numberOfArithmeticSlices(nums)
    print(ans)