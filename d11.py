import intcode
from collections import defaultdict

def add_dir(dir, turn):
    dir += -1 if turn == 0 else 1
    if dir < 0:
        dir += 4
    if dir >= 4:
        dir -= 4
    assert(dir >= 0 and dir < 4)
    return dir

def run():
    init_memory = intcode.parse_input_to_memory("d11input.txt")

    ic = intcode.Intcode(init_memory)
    paint = defaultdict(int)
    dir = 0
    ic.set_input([])
    pos = (0, 0)
    while not ic.is_halted():
        ic.input.append(paint[pos])
        ic.run_to_output()
        if ic.is_halted():
            break
        paint_col = ic.output
        paint[pos] = paint_col
        ic.run_to_output()
        if ic.is_halted():
            break
        turn = ic.output
        dir = add_dir(dir, turn)
        if dir == 0:
            pos = (pos[0], pos[1]-1)
        elif dir == 1:
            pos = (pos[0]+1, pos[1])
        elif dir == 2:
            pos = (pos[0], pos[1]+1)
        elif dir == 3:
            pos = (pos[0]-1, pos[1])
        else: assert(False)
    print(len(paint))

    ic = intcode.Intcode(init_memory)
    paint = defaultdict(int)
    paint[(0, 0)] = 1
    dir = 0
    ic.set_input([])
    pos = (0, 0)
    while not ic.is_halted():
        ic.input.append(paint[pos])
        ic.run_to_output()
        if ic.is_halted():
            break
        paint_col = ic.output
        paint[pos] = paint_col
        ic.run_to_output()
        if ic.is_halted():
            break
        turn = ic.output
        dir = add_dir(dir, turn)
        if dir == 0:
            pos = (pos[0], pos[1]-1)
        elif dir == 1:
            pos = (pos[0]+1, pos[1])
        elif dir == 2:
            pos = (pos[0], pos[1]+1)
        elif dir == 3:
            pos = (pos[0]-1, pos[1])
        else: assert(False)

    minx = 999999
    miny = 999999
    maxx = 0
    maxy = 0
    for k in paint:
        if k[0] < minx:
            minx = k[0]
        if k[0] > maxx:
            maxx = k[0]
        if k[1] < miny:
            miny = k[1]
        if k[1] > maxy:
            maxy = k[1]
    for y in range(miny, maxy+1):
        line = ""
        for x in range(minx, maxx+1):
            line += "." if paint[(x, y)] == 0 else "#"
        print(line)

run()
