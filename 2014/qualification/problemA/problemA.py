from sys import stdin

test_cases = int(stdin.readline())

for i in range(test_cases):
    match = 0
    matchval = 0
    arr1 = []
    arr2 = []
    q1 = int(stdin.readline())
    for j in range(4):
        arr1.append(stdin.readline().split())
    answer1 = arr1[q1-1]
    q2 = int(stdin.readline())
    for j in range(4):
        arr2.append(stdin.readline().split())
    answer2 = arr2[q2-1]
    for j in range(4):
        if (answer1[j] in answer2):
            match += 1
            matchval = answer1[j]
    if (match == 0):
        print("Case #" + str(i+1) + ": Volunteer cheated!")
    elif (match > 1):
        print("Case #" + str(i+1) + ": Bad magician!")
    else:
        print("Case #" + str(i+1) + ": " +str(matchval))
