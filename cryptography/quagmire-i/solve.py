import string

Indicator_keyword = "HSCTF"
Plaintext_keyword = "CONNOLLYROCKS"
Indicator_position = "A"
Ciphertext = "LZXORNZBUYWNRARNOVGCLSQWJEFJFE"


def genStringStartWith(char):
    retval = ""
    for i in range(26):
        retval += chr((ord(char)-ord('A')+i)%26+ord('A'))
    return retval

s = genStringStartWith('V')

def getStraight(keyword):
    retval = ""
    for c in keyword+string.ascii_uppercase:
        if (c in retval)==False:
            retval+=c
    return retval

def getIndex(s, c):
    for i, _c in enumerate(s):
        if c==_c:
            return i
    return -1
    

keyword = getStraight(Plaintext_keyword)
print(keyword)
print()
maps = []
for char in Indicator_keyword:
    start = chr((ord(char)-ord('A')-getIndex(keyword,'A'))%26+ord('A'))
    print(genStringStartWith(start))
    maps.append(genStringStartWith(start))

print("flag{", end="")
for i, c in enumerate(Ciphertext):
    convertstring = maps[i%len(maps)]
    print(keyword[getIndex(convertstring, c)], end="")
print("}")