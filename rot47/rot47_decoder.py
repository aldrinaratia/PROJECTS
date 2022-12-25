### rot47 decoder 
def rot47(s):
    x = []
    for i in range(len(s)):
        j = ord(s[i])
        if j >= 33 and j <= 126:
            x.append(chr(33 + ((j + 14) % 94)))
        else:
            x.append(s[i])
    return ''.join(x)

# picoctf
secret = "A:4@r%uL`M-^M0c0AbcM-MFE055a4ce`eN"


print(rot47(secret))
