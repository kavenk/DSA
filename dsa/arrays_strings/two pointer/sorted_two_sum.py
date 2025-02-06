"""
Example 2: Given a sorted array of unique integers and a target integer, return true if there exists a pair of numbers that sum to target, false otherwise. This problem is similar to Two Sum. (In Two Sum, the input is not sorted).

For example, given nums = [1, 2, 4, 6, 8, 9, 14, 15] and target = 13, return true because 4 + 9 = 13.
"""
def check_for_target(nums,sum):
    left = 0
    right = len(nums) - 1
    while left < right:
        curr = nums[left] + nums[right]
        if curr < sum:
            left += 1
        if curr > sum:
            right -= 1
        if curr == sum:
            return True
    return False

if __name__=="__main__":
    nums = [1, 2, 4, 6, 8, 9, 14, 15]
    sum = 1
    print(check_for_target(nums,sum))

        