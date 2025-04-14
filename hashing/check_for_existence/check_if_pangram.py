def check_if_pangram(s: str) -> bool:
    """
    Check if the input string is a pangram or not.

    A pangram is a sentence that contains every letter of the alphabet at least once.
    For example, "The quick brown fox jumps over the lazy dog" is a pangram.

    :param s: The input string to check.
    :return: True if the string is a pangram, False otherwise.
    """
    s_set = set(s) 
    result = set()

    if len(s_set) >= 26:
        for char in s:
            if char not in result:
                result.add(char)
        return len(s_set) == len(result)
    
    return False


if __name__=="__main__":
    print(check_if_pangram("The quick brown fox jumps over the lazy dog"))  # True
    print(check_if_pangram("Hello World"))  # False
    print(check_if_pangram("Pack my box with five dozen liquor jugs."))  # True
    print(check_if_pangram("Amazingly few discotheques provide jukeboxes."))  # True
    print(check_if_pangram("jwtucoucmdfwxxqnxzkaxoglszmfrcvjoiunqqausaxxaaijyqdqgvdnqcaihwilqkpivenpnekioyqujrdrovqrlxovcucjqzjsxmllfgndfprctxvxwlzjtciqxgsxfwhmuzqvlksyuztoetyjugmswfjtawwaqmwyxmvo"))  # False
        