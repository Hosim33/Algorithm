word=list(input())
for i in range(len(word)):
    tmp = ord(word[i])-3
    if tmp < ord('A'):
        tmp += 26
    print(chr(tmp), end='')
