"""
Given an array of positive integers nums and an integer k, find the length of the longest subarray whose sum is less than or equal to k

"""


def longest_sub_array(nums,k):
    left = current = ans = 0
    
    for right in range(len(nums)):
        current += nums[right]
        while current > k:
            current -= nums[left]
            left += 1
        ans = max(ans, right - left + 1)
    return ans


if __name__=="__main__":
    nums = [3,1,3,9,4,2,1,1,5]
    k = 8
    print(longest_sub_array(nums,k))