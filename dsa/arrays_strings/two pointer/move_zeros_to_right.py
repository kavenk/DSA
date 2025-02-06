"""
Move Zeroes
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.
Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]
"""

def move_zeros(nums: list[int]) -> list[int]:
    zeros = 0
    i = 0
    n = len(nums)
    while i < n:
        if nums[i] == 0:
            zeros += 1
            nums.pop(i)
            n -= 1
        i += 1
    return (nums + [0]*zeros)
if __name__=="__main__":
    nums = [0,1,0,3,12]
    print(move_zeros(nums))
