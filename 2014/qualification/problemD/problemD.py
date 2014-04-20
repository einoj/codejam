from sys import stdin

test_cases = int(stdin.readline())

def burnblock(blocklist, block):
    i = 0
    for j in blocklist:
        if (j == block):
            blocklist.pop(i)
            break
        i += 1

for i in range(test_cases):
    print("Case #" +str(i+1) + ": ", end ="")
    blocks = int(stdin.readline())
    naomi = stdin.readline().split()
    ken = stdin.readline().split()
    ken2 = list(ken)
    naomi2 = list(naomi)
    points_naomi = 0
    for i in range(blocks):
        min_ken = min(ken)
        min_naomi = min(naomi)
        if (min_naomi > min_ken):
            naomi_choose = min_naomi
            ken_choose = min_ken
            burnblock(ken,ken_choose)
            burnblock(naomi,naomi_choose)
            points_naomi += 1
        else:
            #naomi_told = float(max_ken) - 0.000001
            naomi_choose = min_naomi
            ken_choose = max(ken)
            burnblock(ken,ken_choose)
            burnblock(naomi,naomi_choose)
    print(points_naomi,end=" ")
    points_naomi = 0
    for i in range(blocks):
        naomi_choose = max(naomi2)
        if (naomi_choose > max(ken2)):
            burnblock(ken2,min(ken2))
            burnblock(naomi2, max(naomi2))
            points_naomi += 1
        else:
            burnblock(ken2,max(ken2))
            burnblock(naomi2, max(naomi2))
    print(points_naomi)
