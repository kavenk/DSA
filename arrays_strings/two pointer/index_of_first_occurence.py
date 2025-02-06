def strStr(haystack: str, needle: str) -> int:
        i = j = 0
        print(haystack[i:i+len(needle)])
        while i <= (len(haystack) - len(needle)) and j <= len(haystack):
            if haystack[i:i+len(needle)] == needle:
                return i
            else:
                 i+=1
                 j +=1
        return -1

if __name__=="__main__":
    haystack = "a"
    needle = "a"
    print(strStr(haystack,needle))