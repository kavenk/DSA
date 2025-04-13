"""
Given an array of integers nums and an integer target, return indices of two numbers such that they add up to target. You cannot use the same index twice.
"""

def twoSum(nums: list[int], target: int) -> list[int]:
    """
    Time complexity: O(n)
    Space complexity: O(n)
    
    num_to_index = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_to_index:
            return [num_to_index[complement], i]
        num_to_index[num] = i
    return []

    """
    nums_dict = {}
    for i in range(len(nums)):
        num = nums[i]
        complement = target - num
        if complement in nums_dict:
            return [i,nums_dict[complement]]
        nums_dict[num] = i
    return [-1,-1]

# Example usage
if __name__ == "__main__":
    nums = [2, 8, 11, 15]
    target = 9
    result = twoSum(nums, target)
    print(result)  # Output: [0, 1]