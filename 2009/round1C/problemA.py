from sys import stdin

#use lowest base possible
base = 2

N = int(stdin.readline())
for x in range(N):
    chars = []
    values = {}
    case = stdin.readline()
    #remove newline from string
    case = case[:-1]
    for i in case:
        if not (chars.__contains__(i)):
                chars.append(i)
    base = len(chars) 
    if (base == 1):
        base = 2
    values[chars[0]] = 1    
    if (len(chars) > 1):
        values[chars[1]] = 0
    for i in range(2, len(chars)):
        values[chars[i]] = i
    seconds = 0
    j = len(case)-1
    for c in case:
        seconds = seconds + values[c]*base**(j)
        j -= 1
    print("Case #" + str(x+1) + ": " + str(seconds))

