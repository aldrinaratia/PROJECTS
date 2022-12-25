### rot47 decoder and encoder
def rot47(s):
    x = []
    for i in range(len(s)):
        j = ord(s[i])
        if j >= 33 and j <= 126:
            x.append(chr(33 + ((j + 14) % 94)))
        else:
            x.append(s[i]) 
    print("".join(x))


decode = "#@E\cf"
encode = "Rot-47"

rot47(decode)
rot47(encode)
