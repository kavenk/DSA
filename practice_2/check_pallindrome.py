
def pallindrome(s):
	
	n = len(s)
	i = 0 
	j = n-1
	while (i <= j):
		if s[i] != s[j]:
			return False
		else:
			i += 1
			j -= 1
	return True


if __name__=="__main__":
	s = 'racecar'
	print(pallindrome(s))
	

