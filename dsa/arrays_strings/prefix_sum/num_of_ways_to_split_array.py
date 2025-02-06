"""
Given an integer array nums, find the number of ways to split the array into two parts so that the first section has a sum greater than or equal to the sum of the second section. The second section should have at least one number.

"""

def subarray_split_count(nums):

    prefix = [nums[0]]

    for i in range(1,len(nums)):
        prefix.append(nums[i] + nums[i-1])
    ans = 0
    for i in range(len(nums) - 1):
        left_section = prefix[i]
        right_section = prefix [-1] - prefix[i]
        if left_section >= right_section :
            ans += 1
    return ans


if __name__=="__main__":
    nums = [10,4,-8,7,-4,-1]
    print(subarray_split_count(nums))
