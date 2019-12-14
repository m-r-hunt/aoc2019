import math

def sgn(x):
    if x > 0:
        return 1
    elif x < 0:
        return -1
    else:
        return 0

def lcm(a, b):
    return int((a * b) / math.gcd(a, b))

def run():
    init_moons = [
        ([15, -2, -6], [0, 0, 0]),
        ([-5, -4, -11], [0, 0, 0]),
        ([0, -6, 0], [0, 0, 0]),
        ([5, 9, 6], [0, 0, 0]),
    ]
    moons = [([x for x in p], [y for y in v]) for p, v in init_moons]
    for i in range(1000):
        for pos, vel in moons:
            for opos, ovel in moons:
                vel[0] += sgn(opos[0] - pos[0])
                vel[1] += sgn(opos[1] - pos[1])
                vel[2] += sgn(opos[2] - pos[2])
        for pos, vel in moons:
            pos[0] += vel[0]
            pos[1] += vel[1]
            pos[2] += vel[2]
    totale = 0
    for pos, vel in moons:
        pe = 0
        for p in pos:
            pe += abs(p)
        ke = 0
        for v in vel:
            ke += abs(v)
        totale += pe * ke
    print(totale)

    moons = [([x for x in p], [y for y in v]) for p, v in init_moons]
    xvpr = None
    yvpr = None
    zvpr = None
    for i in range(1, 10000000):
        for pos, vel in moons:
            for opos, ovel in moons:
                vel[0] += sgn(opos[0] - pos[0])
                vel[1] += sgn(opos[1] - pos[1])
                vel[2] += sgn(opos[2] - pos[2])
        for pos, vel in moons:
            pos[0] += vel[0]
            pos[1] += vel[1]
            pos[2] += vel[2]
        if xvpr == None and (moons[0][0][0] == init_moons[0][0][0] and moons[0][1][0] == 0 and
            moons[1][0][0] == init_moons[1][0][0] and moons[1][1][0] == 0 and
            moons[2][0][0] == init_moons[2][0][0] and moons[2][1][0] == 0 and
            moons[3][0][0] == init_moons[3][0][0] and moons[3][1][0] == 0):
            print("xvelpos repeat", i)
            xvpr = i
        if yvpr == None and (moons[0][0][1] == init_moons[0][0][1] and moons[0][1][1] == 0 and
            moons[1][0][1] == init_moons[1][0][1] and moons[1][1][1] == 0 and
            moons[2][0][1] == init_moons[2][0][1] and moons[2][1][1] == 0 and
            moons[3][0][1] == init_moons[3][0][1] and moons[3][1][1] == 0):
            print("yvelpos repeat", i)
            yvpr = i
        if zvpr == None and (moons[0][0][2] == init_moons[0][0][2] and moons[0][1][2] == 0 and
            moons[1][0][2] == init_moons[1][0][2] and moons[1][1][2] == 0 and
            moons[2][0][2] == init_moons[2][0][2] and moons[2][1][2] == 0 and
            moons[3][0][2] == init_moons[3][0][2] and moons[3][1][2] == 0):
            print("zvelpos repeat", i)
            zvpr = i
        if xvpr != None and yvpr != None and zvpr != None:
            break
    print(lcm(lcm(xvpr, yvpr), zvpr))

run()
