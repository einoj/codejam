from sys import stdin

test_cases = int(stdin.readline())

for i in range(test_cases):
    values = stdin.readline().split()
    C = float(values[0])
    F = float(values[1])
    X = float(values[2])
    best_time = False
    time = X/2.0
    new_time = 0
    curr_F = 2.0
    #I difine part, so i only have to do the X/(curr_F+F) division once
    #Thus saving some time
    part = 0
    while(not best_time):
        part = X/(curr_F+F)
        new_time += C/(curr_F)+part
        if (new_time < time):
            time = new_time
            new_time = new_time - part
            curr_F += F 
        else:
            best_time = True
    print("Case #" + str(i+1) + ": " +"{0:.7f}".format(time))
