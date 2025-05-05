
def flip_k_zeros(nums: list[int],k: int) -> int:
    
    left = zero_count = sub_array_length = 0

    for right in range(len(nums)):
        if nums[right] == 0:
            zero_count += 1

        while zero_count > k:
            if nums[left] == 0:
                zero_count -= 1
                left += 1  
                sub_array_length = max(sub_array_length, right - left + 1)      
            else:
                left += 1
                sub_array_length = max(sub_array_length, right - left + 1)  
        
        
    return sub_array_length

if __name__=="__main__":
    nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
    k = 3
    print(flip_k_zeros(nums,k))