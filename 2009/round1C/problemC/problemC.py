from sys import stdin
#Bribe the Prisoners

def release(prison, tbr):
    middle = round(prison/2)
    tbrA = []
    tbrB = []
    smallest = prison
    for t in tbr:
        if (abs(middle-t) <= smallest):
            smallest = abs(middle-t)
            split = t
    a = split - 1
    b = prison  - split 
    for t in tbr:
        if (t < a+1):
            tbrA.append(t)
        elif (t > a+1):
            tbrB.append(t-(a+1))
   # a = p[0:int(smallest)-1] #lower array
   # b = prison[int(smallest):] #upper array
    coins = prison - 1
    if ((a > 0) and (len(tbrA) > 0)):
        coins += release(a, tbrA)
    if ((b > 0) and (len(tbrB) > 0)):
        coins += release(b, tbrB)
    return coins



num_cases = int(stdin.readline())

for i in range(num_cases):
    pq = stdin.readline().split()
    p = int(pq[0])
    q = int(pq[1])
    tbr = stdin.readline().split() #to be released
    tbr = [int(i) for i in tbr]
    coins = release(p, tbr)
    print("Case #" + str(i+1) +": " + str(coins))

