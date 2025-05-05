
def two_sum(nums: list[int], target: int)-> bool:

    n = len(nums)
    i = 0
    j = n - 1

    while i < j :
        sum = nums[i] + nums[j]
        if sum > target:
            j -= 1
        if sum < target:
            i += 1
        if sum == target:
            return True
    return False


if __name__=="__main__":
    nums = [1, 2, 4, 6, 8, 10, 14, 15] 
    target = 14
    print(two_sum(nums,target))