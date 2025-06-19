import re

def reverse(S):
    temp = []

    str = S.split()
    for i in range(len(str)):
        temp.append(str[i][::-1])
    print(" ".join(temp))

S = input()

if '<' in S:
    tag = []
    while('<' in S):
        m = re.search('<(.+?)>', S)
        sub = m.group()
        tag.append(sub)
        S = S.replace(sub, "")
    print(tag)

reverse(S)

