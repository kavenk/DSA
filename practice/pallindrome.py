def pallindrome(s: str)-> bool:
     
     i = 0
     n = len(s)
     j = n - 1

     while i < j:
        if s[i] != s[j]:
            return False
        else:
            i += 1
            j -= 1
     return True


if __name__=="__main__":
    s = "abcdba"
    print(pallindrome(s))
