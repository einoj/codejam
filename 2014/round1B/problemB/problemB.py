from sys import stdin

test_cases = int(stdin.readline())

svar = {}

for i in range(test_cases):
    ting = stdin.readline()
    ting = ting.split()
    A = int(ting[0]) 
    B =int(ting[1])
    K =int(ting[2])
    a = 0
    b = 0
    A1 = A
    B1 = B
    total = 0
    for j in svar:
        at = int(j.split()[0])
        bt = int(j.split()[1])
        kt = int(j.split()[2])
        if ((at <= A and bt <= B) and (at > a and bt > b) and kt <= K):
            a = at
            b = bt
            A1 = A+1
            B1 = B+1
            total = svar[j]
    print(total)
    for n in range(a,A1):
        for m in range(b,B1):
            if (n&m < K):
                print("test")
                total += 1
            else:
                break
    svar[str(A) + " " + str(B) + " " + str(K)] = total
    print("Case #" + str(i+1) + ": " + str(total))
