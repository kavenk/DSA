
def sub_array_sum(nums: list[int]) -> int:
    """sum = 0
    left = 0
    for i in range(len(nums)):
        sum += nums[i] * (i+1) * (len(nums) - i)
    return sum"""
    total_sum = 0
    for i in range(len(nums)):
        sum = 0
        for j in range(i,len(nums)):
            sum += nums[j]
            total_sum += sum
    return total_sum

if __name__=="__main__":
    nums = [1,2,3]
    print(sub_array_sum(nums))