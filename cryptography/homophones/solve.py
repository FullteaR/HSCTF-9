m = {
    "5":"E",
    "V":"W",
    "K":"I",
    "8":"Y",
    "C":"T",
    "N":"O",
    "R":"H",
    "Q":"J",
    "2":"O",
    "G":"O",
    "I":"K",
    "0":"M",
    "H":"R",
    "L":"N",
    "D":"V",
    "9":"I",
    "S":"E",
    "B":"R",
    "3":"D",
    "7":"S",
    "P":"S",
    "O":"T",
    "W":"E",
    "J":"C",
    "4":"P",
    "M":"G"
}
for e,c in zip("T1AXYZ6FUE", "ABSOLUTELY"):
        m[e] = c

with open("ct.txt", "r") as fp:
    lines = fp.readlines()

for line in lines:
    for char in line.strip():
        if char in m:
            print('\033[32m'+m[char]+'\033[0m', end="")
        else:
            print('\033[31m'+char+'\033[0m', end="")
    print()