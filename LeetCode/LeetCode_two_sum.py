class TwoSum:
    # Approach 1 - "Brute Force"

    # loop through each element of the list O(n)
    # then loop again through each element for the complement O(n)
    # this gives a time complexity of O(n)*O(n) = O(n^2), which is quite poor
    # however, the space complexity is great since we only need to store the calculations one at a time

    def approach1(self, nums, target):
        for i in range(len(nums)):  # time O(n)
            for j in range(len(nums)):  # time O(n)
                if target - nums[i] == nums[j] and i != j:
                    return [i, j]

    # Approach 2 - "Create dictionary, then iterate over it"

    # create a dictionary of key, value = index, element pairs from the list
    # this has a space complexity of O(n)
    # for each key, check if a complementary key exists in the dict
    # this has time complexity of O(1)*n = O(n), both in the best and worst cases

    def approach2(self, nums, target):
        nums_dict = {i: nums[i] for i in range(len(nums))}  # space O(n)
        for key, value in nums_dict.items():  # time O(n)
            if target - value in nums_dict.values():  # space O(1)
                if nums.index(value) != nums.index(target - value):
                    return [nums.index(value), nums.index(target - value)]  # time O(1)

    # Approach 3 - "While creating a dictionary, iterate over it"

    # as each index, element pair is being added, check if the complementary key exists
    # even though the dictionary is incomplete, at the worst, the penultimate key will be correct O(n-1)
    # at best, the first key will be correct O(1)
    # space complexity is still O(n) to store the new hash map

    def approach3(self, nums, target):
        nums_dict = {}
        for i in range(len(nums)):
            nums_dict[i] = nums[i]  # space O(n) at worst
            print(nums_dict)
            print(target - nums[i])
            if target - nums[i] in nums_dict.values():  # space O(1)
                if nums.index(nums[i]) != nums.index(target - nums[i]):
                    return [nums.index(nums[i]), nums.index(target - nums[i])]  # time O(1)*n at worst


# if __name__ == "main":
two_sum = TwoSum()
nums = [3, 3]
target = 6
#print(two_sum.approach1(nums, target))
# print(two_sum.approach2(nums, target))
print(two_sum.approach3(nums, target))
