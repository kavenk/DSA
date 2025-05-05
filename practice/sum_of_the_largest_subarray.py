
def sum_of_sub_array(nums: list[int],k: int) -> int:
    
    sum = 0
    final_sum = 0
    for i in range(k):
        sum += nums[i]
    final_sum = sum
    for i in range(k,len(nums)):
        sum += nums[i] - nums[i - k]
        final_sum = max(sum, final_sum)

    return final_sum

if __name__=="__main__":
    nums = [3,-1,4,12,-8,5,6]
    k = 4 

    print(sum_of_sub_array(nums,k))
   



