#Center of Gravity
from sys import stdin
from numpy import sqrt

class Firefly ():
    def __init__(self, fireflyNum, x, y, z, vx, vy ,vz):
        self.fireflyNum = fireflyNum
        self.x = x
        self.y = y
        self.z = z
        self.vx = vx
        self.vy = vy
        self.vz = vz

    def timestep(self):
        self.x += self.vx
        self.y += self.vy
        self.z += self.vz
    
    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def getZ(self):
        return self.z

def centerOfGravity(flies):
    point = []
    xc = 0.0
    yc = 0.0
    zc = 0.0
    N = len(flies)
    for fly in flies:
        xc += fly.getX()
        yc += fly.getY()
        zc += fly.getZ()
    xc = xc/N
    yc = yc/N
    zc = zc/N
    point.append(xc)
    point.append(yc)
    point.append(zc)
    return point



num_cases = int(stdin.readline())

case_cnt = 0
time = 0
is_new_case = True
num_fireflies = 0
fireflies = []
num = 1
for line in stdin:
    if is_new_case:
        num_fireflies = int(line)
        is_new_case = False
        fireflies = []
        case_cnt = 0
        time = 0
    else:
        line = line[:-1] # remove newline 
        fireflies.append(Firefly(case_cnt,int(line.split()[0]),int(line.split()[1]),int(line.split()[2]),int(line.split()[3]),int(line.split()[4]),int(line.split()[5])))
        case_cnt += 1
        if (case_cnt == num_fireflies):
            prev_center = 15001
            center = 15000
            while (center <= prev_center and time <= 100):
                prev_center = center
                point = centerOfGravity(fireflies)
                center = sqrt(point[0]**2 + point[1]**2 + point[2]**2)
                for fly in fireflies:
                    fly.timestep()
                time += 1
            is_new_case = True
            # python3: print("Case #" + str(num) + ": " + str(prev_center) + " " + str(time-2))
            print "Case #%d: %.8f %.8f" % (num, prev_center, time-2)
