def rot47_encoder(s):
    x = []
    for i in range(len(s)):
        j = ord(s[i])
        if j >= 33 and j <= 126:
            x.append(chr(33 + ((j + 14) % 94)))
        else:
            x.append(s[i])
    return ''.join(x)

s = "Rot-47"
print(rot47_encoder(s))
# output: *@E\cF
