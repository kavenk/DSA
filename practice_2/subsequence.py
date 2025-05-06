def is_subsequence(s,t):
	n = len(s)
	m = len(t)
	i = j = 0
	ans = ''
	while (i < n and j < m):
		if s[i] == t[j]:
			ans += s[i]
			i += 1
			j += 1
		else:
			j += 1
	return s == ans

if __name__=="__main__":
	s = 'aced'
	t = 'abcde'
	print(is_subsequence(s,t))


