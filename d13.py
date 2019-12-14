import intcode

def run():
    memory = intcode.parse_input_to_memory("d13input.txt")
    memory[0] = 2
    ic = intcode.Intcode(memory)
    screen = {}
    blocks = 0
    max_x = 0
    max_y = 0
    score = 0
    paddle_x = 0
    ball_x = 0
    while not ic.is_halted():
        ic.run_to_output()
        if ic.needs_input:
            for y in range(max_y+1):
                line = ""
                for x in range(max_x+1):
                    if (x, y) in screen:
                        tile = screen[(x, y)]
                        if tile == 0:
                            line += " "
                        elif tile == 1:
                            line += "|"
                        elif tile == 2:
                            line += "#"
                        elif tile == 3:
                            line += "-"
                        elif tile == 4:
                            line += "o"
                    else:
                        line += " "
                #print(line)
            #print(ball_x, paddle_x)
            #screen = {}
            if ball_x < paddle_x:
                #print("left")
                ic.add_input(-1)
            elif ball_x > paddle_x:
                #print("right")
                ic.add_input(1)
            else:
                #print("neutral")
                ic.add_input(0)
            #input()
            continue
        x = ic.output
        if x > max_x:
            max_x = x
        ic.run_to_output()
        y = ic.output
        if y > max_y:
            max_y = y
        ic.run_to_output()
        block = ic.output
        #print(x, y, block)
        if x != -1:
            screen[(x, y)] = block
        if x == -1:
            score = block
            print(score)
        if block == 3:
            paddle_x = x
        elif block == 4:
            ball_x = x
    print(score)

run()
