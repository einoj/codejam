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

    def getVx(self):
        return self.vx

    def getVy(self):
        return self.vy

    def getVz(self):
        return self.vz

def centerOfGravityandMotion(flies):
    point = []
    xc = 0.0
    yc = 0.0
    zc = 0.0
    vxc = 0.0
    vyc = 0.0
    vzc = 0.0
    N = len(flies)
    for fly in flies:
        xc += fly.getX()
        yc += fly.getY()
        zc += fly.getZ()
        vxc += fly.getVx()
        vyc += fly.getVy()
        vzc += fly.getVz()
    xc = xc/N
    yc = yc/N
    zc = zc/N
    vxc = vxc/N
    vyc = vyc/N
    vzc = vzc/N
    point.append(xc)
    point.append(yc)
    point.append(zc)
    point.append(vxc)
    point.append(vyc)
    point.append(vzc)
    return point



num_cases = int(stdin.readline())

case_cnt = 0
time = 0
is_new_case = True
num_fireflies = 0
fireflies = []
num = 0
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
            point = centerOfGravityandMotion(fireflies)
            #check for 0 division
            if (point[3]**2+point[4]**2+point[5]**2 < 1e-9):
                #t = 0 is min
                t = 0
                center = sqrt(point[0]**2 + point[1]**2 + point[2]**2)
            else:
                t = (point[0]*point[3] +point[1]*point[4] + point[2]*point[5])/(-point[3]**2-point[4]**2-point[5]**2)
                if (t < 0):
                    t = 0
                    center = sqrt(point[0]**2 + point[1]**2 + point[2]**2)
                else:
                    center = sqrt((point[0]+point[3]*t)**2 + (point[1]+point[4]*t)**2 + (point[2]+point[5]*t)**2)
            is_new_case = True
            num += 1
            # python3: print("Case #" + str(num) + ": " + str(prev_center) + " " + str(time-2))
            #print "Case #%d: %.8f %.8f" % (num, prev_center, time-2)
            print("Case #{}: {:.8f} {:.8f}".format(num,center,t))
