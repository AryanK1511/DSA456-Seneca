def is_palindrome(word, start=0, end=None):
    if end is None:
        end = len(word) - 1

    if start >= end:
        return True

    if word[start] == word[end]:
        return is_palindrome(word, start + 1, end - 1)

    return False