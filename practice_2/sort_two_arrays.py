
def sort_arrays(arr1, arr2):
	n = len(arr1)
	m = len(arr2)
	i = j = 0
	sorted = []

	while ( i < n and j < m):
		if arr1[i] <= arr2[j]:
			sorted.append(arr1[i])
			i += 1
		else:
			sorted.append(arr2[j])
			j += 1

	while (i < n):
		sorted.append(arr1[i])
		i += 1

	while (j < m):
		sorted.append(arr2[j])
		j += 1

	return sorted


if __name__=="__main__":

	arr1 = [1,4,7,20]
	arr2 = [3,5,6]

	print(sort_arrays(arr1,arr2))
