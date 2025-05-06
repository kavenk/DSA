def reverse_array(s: list) -> list:

	
	i = 0
	j = len(s) - 1
	while (i < j):
		s[j],s[i] = s[i],s[j]
		i += 1
		j -= 1

	return s


if __name__=="__main__":
	s = ["h","e","l","l","o"]
	print(reverse_string(s))

