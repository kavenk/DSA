
def longest_sub_array(nums: list[int],k: int) -> int:
    i = sum = sub_array_length = 0
    n = len(nums)
    
    for j in range(n):
        sum += nums[j]
        while sum > k:
            sum -= nums[i]
            i += 1
            if sub_array_length > j - i + 1:
                sub_array_length = sub_array_length
            else:
                sub_array_length = j - i + 1
            
    return sub_array_length
    
if __name__=="__main__":
    nums = [3, 1, 2, 7, 4, 2, 1, 1, 5] 
    k = 8            
    print(longest_sub_array(nums,k))
