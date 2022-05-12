def is_palin(s):
    start = 0
    end = len(s) - 1

    while (start < end):
        if (s[start] != s[end]):
            return s, " is not a palindrome."
        start = start + 1
        end = end - 1
    return s, " is a palindrome."

s = "races"
print(is_palin(s)) 