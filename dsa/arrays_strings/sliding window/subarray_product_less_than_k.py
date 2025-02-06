"""
Given an array of positive integers nums and an integer k, return the number of subarrays where the product of all the elements in the subarray is strictly less than k.

For example, given the input nums = [10, 5, 2, 6], k = 100, the answer is 8. The subarrays with products less than k are:

[10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6]

"""

def subarray_less_than(nums,k):

    left = 0
    count = 0
    current = 1
    for right in range(len(nums)):
        current *= nums[right]
        while current >= k:
            current //= nums[left]
            left += 1
        count += right - left + 1
    return count

    
if __name__=="__main__":
    nums = [10, 5, 2, 6]
    k = 100
    print(subarray_less_than(nums,k))


