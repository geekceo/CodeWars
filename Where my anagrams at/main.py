def anagrams(word, words):
    return [check for check in words if sorted(word) == sorted(check)]