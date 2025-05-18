






# on the 2nd loop i used x in sted if nums that is becuase they both had the 
# same amount of indexes. it better to use that actual value in loops . the actual vairable is nums.









# def TwoSum(nums, target):
#     for num1 in range(len(nums)):
#         for bum2 in range(num1 + 1, len(x)):
#             if nums[num1] + nums[bum2] == target:
#                 return [num1, bum2]


# x = [1, 3, 4, 5]
# nums = [2, 7, 11, 15]
# target = 9
# result = TwoSum(nums, target)
# print(result) 






# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].






class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        stored_number = {}
        for idx, num in enumerate(nums):
            number_needed = target - num
            if number_needed in stored_number:        # if the number is there in the loop then this happens"number_needed + num == target"
                return [stored_number[number_needed], idx]
            stored_number[num] = idx




nums = [2, 7, 11, 15]
target = 9

answer = Solution()
print(answer.twoSum(nums, target))










