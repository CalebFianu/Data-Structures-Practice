def compress(s):
    compressed = s[0]
    count = 1

    for i in range(1, len(s)):
        if(s[i] == compressed[-1]):
            count = count + 1
        else:
            compressed = compressed + str(count) + s[i]
            count = 1
    return compressed + str(count)

s = "aaabbbc"
print(compress(s))