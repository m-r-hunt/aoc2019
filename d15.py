import intcode
import math

def print_map(map, x, y):
    minx = 9999
    miny = 9999
    maxx = -9999
    maxy = -9999
    for cx, cy in map:
        minx = min(minx, cx)
        miny = min(miny, cy)
        maxx = max(maxx, cx)
        maxy = max(maxy, cy)
    for yy in range(miny, maxy+1):
        line = ""
        for xx in range(minx, maxx+1):
            if xx == x and yy == y:
                line += "@"
            elif (xx, yy) in map:
                line += map[(xx, yy)]
            else:
                line += " "
        print(line)



def run():
    memory = intcode.parse_input_to_memory("d15input.txt")
    ic = intcode.Intcode(memory)
    map = {(0, 0): "."}
    x = 0
    y = 0
    dir = "w"
    found_o2 = False
    while True:
        nx = x
        ny = y
        if dir == "w":
            ic.add_input(1)
            ny -= 1
        elif dir == "s":
            ic.add_input(2)
            ny += 1
        elif dir == "a":
            ic.add_input(3)
            nx -= 1
        elif dir == "d":
            ic.add_input(4)
            nx += 1
        ic.run_to_output()
        result = ic.output
        if result == 0:
            map[(nx, ny)] = "#"
            if dir == "w":
                dir = "d"
            elif dir == "d":
                dir = "s"
            elif dir == "s":
                dir = "a"
            elif dir == "a":
                dir = "w"
        elif result == 1:
            x = nx
            y = ny
            map[(x, y)] = "."
            if dir == "w":
                dir = "a"
            elif dir == "a":
                dir = "s"
            elif dir == "s":
                dir = "d"
            elif dir == "d":
                dir = "w"
        elif result == 2:
            x = nx
            y = ny
            print("Found o2!")
            map[(x, y)] = "o"
            found_o2 = True
            o2x = x
            o2y = y
        if x == 0 and y == 0 and found_o2:
            break
    print_map(map, x, y)

    queue = [(0, 0)]
    visited = {(0, 0): 0}
    while len(queue) > 0:
        x, y = queue[0]
        cost = visited[(x, y)]
        queue = queue[1:]
        if map[(x, y)] == "o":
            print(cost)
            break
        if (x+1, y) not in visited and map[(x+1, y)] != "#":
            queue.append((x+1, y))
            visited[(x+1, y)] = cost+1
        if (x-1, y) not in visited and map[(x-1, y)] != "#":
            queue.append((x-1, y))
            visited[(x-1, y)] = cost+1
        if (x, y-1) not in visited and map[(x, y-1)] != "#":
            queue.append((x, y-1))
            visited[(x, y-1)] = cost+1
        if (x, y+1) not in visited and map[(x, y+1)] != "#":
            queue.append((x, y+1))
            visited[(x, y+1)] = cost+1

    queue = [(o2x, o2y)]
    oxygenated = {(o2x, o2y): 0}
    max_time = 0
    while len(queue) > 0:
        x, y = queue[0]
        cost = oxygenated[(x, y)]
        max_time = max(max_time, cost)
        queue = queue[1:]
        if (x+1, y) not in oxygenated and map[(x+1, y)] != "#":
            queue.append((x+1, y))
            oxygenated[(x+1, y)] = cost+1
        if (x-1, y) not in oxygenated and map[(x-1, y)] != "#":
            queue.append((x-1, y))
            oxygenated[(x-1, y)] = cost+1
        if (x, y-1) not in oxygenated and map[(x, y-1)] != "#":
            queue.append((x, y-1))
            oxygenated[(x, y-1)] = cost+1
        if (x, y+1) not in oxygenated and map[(x, y+1)] != "#":
            queue.append((x, y+1))
            oxygenated[(x, y+1)] = cost+1
    print(max_time)


run()
