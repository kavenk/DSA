def check_is_anagram(s: str, t: str) -> bool:

    character_set = {}
    if len(s) != len(t):
        return False
    for char in s:
        character_set[char] = character_set.get(char,0) + 1

    for char in t:
        if char not in character_set:
            return False
        if char in character_set:
            character_set[char] -= 1

        if character_set[char] < 0:
            return False

    return True


if __name__=="__main__":
    s = "anagram"
    t = "nagsaram"

    print(check_is_anagram(s,t))
