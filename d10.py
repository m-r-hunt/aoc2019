from collections import defaultdict
import math

def visible(a, b, map):
    relx = b[0] - a[0]
    rely = b[1] - a[1]
    gcd = math.gcd(relx, rely)
    dx = relx / gcd
    dy = rely / gcd
    for i in range(1, gcd):
        p = (a[0] + i*dx, a[1] + i*dy)
        if map[p]:
            return False
    return True


def run():
    roids = []
    with open("d10input.txt", "r") as file:
        text = file.read()
        y = 0
        for line in text.split("\n"):
            x = 0
            for c in line:
                if c == "#":
                    roids.append((x, y))
                x += 1
            y += 1
    #print(roids)
    print(len(roids))

    roid_map = defaultdict(lambda: False)
    for roid in roids:
        roid_map[roid] = True

    roid_vis = []
    counts = []
    max_count = 0
    listener = (0, 0)
    for roid in roids:
        count = 0
        for other in roids:
            if roid == other:
                continue
            if visible(roid, other, roid_map):
                count += 1
        counts.append(count)
        if count > max_count:
            max_count = count
            listener = roid
    print(max(counts))

    print(listener)
    angle_roids = []
    for roid in roids:
        if roid == listener:
            continue
        angle = -math.atan2(roid[0] - listener[0], roid[1] - listener[1])
        angle_roids.append([angle, roid])
    angle_roids.sort(key=lambda r: r[0])
    print(angle_roids)

    destroyed_angle = -100
    destroyed = 0
    while True:
        while angle_roids[0][0] == destroyed_angle:
            # rotate
            angle_roids = angle_roids[1:] + angle_roids[:1]
        next_angle = angle_roids[0][0]
        
        candidates = [r for r in angle_roids if r[0] == next_angle]
        min_dist = 99999999
        to_dest = []
        for c in candidates:
            dist = math.sqrt((c[1][1] - listener[1])*(c[1][1] - listener[1]) + (c[1][0] - listener[0])*(c[1][0] - listener[0]))
            if dist < min_dist:
                min_dist = dist
                to_dest = c
        destroyed += 1
        print(to_dest)
        if destroyed == 200:
            print(to_dest[1][0]*100 + to_dest[1][1])
            break
        angle_roids.remove(to_dest)
        destroyed_angle = to_dest[0]


run()
