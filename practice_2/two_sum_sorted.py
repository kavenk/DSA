def two_sum_sorted(nums,target):
	n = len(nums)
	i = 0
	j = n - 1

	while ( i <= j ):

		sum = nums[i] + nums[j]

		if sum < target:
			i += 1
		elif sum > target:
			j -= 1
		else:
			return True
	return False


if __name__=="__main__":
	nums = [1,2,4,6,8,9,14,15]
	target = 25

	print(two_sum_sorted(nums,target))
