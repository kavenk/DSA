
def missing_number(nums: list[int]) -> int:
    
    num_set = set(range(len(nums) + 1))
    print(num_set)
    for num in nums:
        if num in num_set:
            num_set.remove(num)
    return num_set.pop() 

if __name__=="__main__":
    nums = [9,6,4,2,3,5,7,0,1]
    print(missing_number(nums))
    