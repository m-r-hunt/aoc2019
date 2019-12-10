def trace(line):
    points = set()
    times = {}
    pos = (0, 0)
    steps = 0
    for move in line:
        dir = move[0]
        dx = (0, 0)
        if dir == "U":
            dx = (0, -1)
        elif dir == "D":
            dx = (0, 1)
        elif dir == "L":
            dx = (-1, 0)
        elif dir == "R":
            dx = (1, 0)
        else:
            print("Wtf")
        dist = int(move[1:])
        for i in range(dist):
            steps += 1
            pos = (pos[0] + dx[0], pos[1] + dx[1])
            points.add(pos)
            if not pos in times:
                times[pos] = steps
    return points, times

def run():
    line1 = []
    line2 = []
    with open("d3input.txt", "r") as file:
        text = file.read()
        lines = text.split("\n")
        line1 = lines[0].split(",")
        line2 = lines[1].split(",")
    points1, times1 = trace(line1)
    points2, times2 = trace(line2)
    mindist = 999999
    mintime = 99999999
    for point in points1 & points2:
        dist = abs(point[0]) + abs(point[1])
        if dist < mindist:
            mindist = dist
        time = times1[point] + times2[point]
        if time < mintime:
            mintime = time
    print(mindist)
    print(mintime)


run()
